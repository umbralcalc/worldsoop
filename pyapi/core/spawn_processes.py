import os
from multiprocessing import Process


def run_worldsoop_binary(*args, **kwargs):
    cmd = "./bin/worldsoop"
    for arg in args:
        cmd += f" {arg}"
    for k, v in kwargs.items():
        cmd += f" --{k} {v}"
    os.system(cmd)


def spawn_worldsoop_process(*args, **kwargs) -> Process:
    p = Process(target=run_worldsoop_binary, *args, **kwargs)
    p.start()


def spawn_worldsoop_processes(num: int, *args, **kwargs) -> list[Process]:
    processes: list[Process] = []
    for _ in range(num):
        processes.append(spawn_worldsoop_process(*args, **kwargs))
    return processes


def await_processes(processes: list[Process]): 
    for process in processes:
        if process is None:
            continue
        process.join()

