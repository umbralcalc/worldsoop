from pyapi.core.config_builder import dump_temporary_yaml
from pyapi.core.spawn_processes import (
    run_worldsoop_process,
    spawn_worldsoop_processes,
)


def test_process_running(
    stochadex_settings_config,
    stochadex_implementations_config,
):
    settings_file = dump_temporary_yaml(stochadex_settings_config)
    implementations_file = dump_temporary_yaml(stochadex_implementations_config)
    _ = run_worldsoop_process(
        *("> /tmp/tempdata.txt",),
        **{
            "settings": settings_file.name,
            "implementations": implementations_file.name,
        },
    )
    settings_file.close()
    implementations_file.close()


def test_multiple_processes_spawning(
    stochadex_settings_config,
    stochadex_implementations_config,
):
    settings_file = dump_temporary_yaml(stochadex_settings_config)
    implementations_file = dump_temporary_yaml(stochadex_implementations_config)
    spawn_worldsoop_processes(
        5,
        2,
        *("> /tmp/tempdata.txt",),
        **{
            "settings": settings_file.name,
            "implementations": implementations_file.name,
        },
    )
    settings_file.close()
    implementations_file.close()
