from pyapi.core.spawn_processes import (
    spawn_worldsoop_process,
    spawn_worldsoop_processes,
    await_processes,
)

def test_process_spawning():
    p = spawn_worldsoop_process(args=("> /tmp/tempdata.txt",))
    if p is not None:
        p.join()


def test_multiple_processes_spawning():
    p = spawn_worldsoop_processes(10, args=("> /tmp/tempdata.txt",))
    await_processes(p)