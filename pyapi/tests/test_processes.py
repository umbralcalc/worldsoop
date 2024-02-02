from pyapi.core.config_builder import dump_temporary_yaml
from pyapi.core.spawn_processes import (
    spawn_worldsoop_process,
    spawn_worldsoop_processes,
    await_processes,
)

def test_process_spawning(
    stochadex_settings_config,
    stochadex_implementations_config,
):
    settings_file = dump_temporary_yaml(stochadex_settings_config)
    implementations_file = dump_temporary_yaml(
        stochadex_implementations_config
    )
    p = spawn_worldsoop_process(
        args=("> /tmp/tempdata.txt",),
        kwargs={
            "settings": settings_file.name,
            "implementations": implementations_file.name,
        },
    )
    if p is not None:
        p.join()
    settings_file.close()
    implementations_file.close()


def test_multiple_processes_spawning(
    stochadex_settings_config,
    stochadex_implementations_config,
):
    settings_file = dump_temporary_yaml(stochadex_settings_config)
    implementations_file = dump_temporary_yaml(
        stochadex_implementations_config
    )
    p = spawn_worldsoop_processes(
        5, 
        args=("> /tmp/tempdata.txt",),
        kwargs={
            "settings": settings_file.name,
            "implementations": implementations_file.name,
        },
    )
    await_processes(p)
    settings_file.close()
    implementations_file.close()