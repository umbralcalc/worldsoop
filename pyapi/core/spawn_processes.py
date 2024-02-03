import subprocess

from pathlib import Path
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
from tempfile import _TemporaryFileWrapper
from pyapi.core.config_builder import WorldsoopConfig, dump_temporary_yaml


@dataclass
class WorldsoopProcessArgs:
    settings: Path
    implementations: Path
    dashboard: Path | None = None
    extras: list[str] | None = None


def run_worldsoop_process(args: WorldsoopProcessArgs) -> str:
    cmd = ["./bin/worldsoop"]
    cmd += ["--settings", args.settings.as_posix()]
    cmd += ["--implementations", args.implementations.as_posix()]
    if args.dashboard:
        cmd += ["--dashboard", args.dashboard.as_posix()]
    if args.extras:
        cmd += args.extras
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise Exception(f"Go process error: {e.returncode}, Output: {e.output}")


def _update_futures_with_spawned_process(
    futures,
    index: int,
    config: WorldsoopConfig,
    executor: ThreadPoolExecutor,
):
    settings_file = dump_temporary_yaml(config.settings)
    implementations_file = dump_temporary_yaml(config.implementations)
    args = WorldsoopProcessArgs(
        settings=Path(settings_file.name),
        implementations=Path(implementations_file.name),
    )
    dashboard_file: _TemporaryFileWrapper | None = None
    if config.dashboard:
        dashboard_file = dump_temporary_yaml(config.dashboard)
        args.dashboard = Path(dashboard_file.name)
    futures[executor.submit(run_worldsoop_process, args)] = (
        index,
        settings_file,
        implementations_file,
        dashboard_file,
    )


def spawn_worldsoop_processes_from_configs(
    max_workers: int,
    configs: list[WorldsoopConfig],
):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for i, config in enumerate(configs):
            _update_futures_with_spawned_process(
                futures,
                i,
                config,
                executor,
            )

        for future in as_completed(futures):
            (
                i,
                settings_file,
                implementations_file,
                dashboard_file,
            ) = futures[future]
            settings_file.close()
            implementations_file.close()
            if dashboard_file:
                dashboard_file.close()
            try:
                result = future.result()
            except Exception as e:
                print(f"Go process {i} failed!\nError: {str(e)}")
