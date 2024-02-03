from pathlib import Path
from pyapi.core.config_builder import WorldsoopConfig, dump_temporary_yaml
from pyapi.core.spawn_processes import (
    WorldsoopProcessArgs,
    run_worldsoop_process,
    spawn_worldsoop_processes_from_configs,
)


def test_process_running(
    stochadex_settings_config,
    stochadex_implementations_config,
):
    settings_file = dump_temporary_yaml(stochadex_settings_config)
    implementations_file = dump_temporary_yaml(stochadex_implementations_config)
    _ = run_worldsoop_process(
        WorldsoopProcessArgs(
            settings=Path(settings_file.name),
            implementations=Path(implementations_file.name),
            stdout=Path("/tmp/tempdata.txt"),
        ),
    )
    settings_file.close()
    implementations_file.close()


def test_multiple_processes_spawning(
    stochadex_settings_config,
    stochadex_implementations_config,
):
    spawn_worldsoop_processes_from_configs(
        2,
        [
            WorldsoopConfig(
                settings=stochadex_settings_config,
                implementations=stochadex_implementations_config,
            )
            for _ in range(5)
        ],
    )
