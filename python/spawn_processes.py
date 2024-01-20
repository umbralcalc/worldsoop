import os
from multiprocessing import Process


def run_worldsoop_binary(name: str):
    print(name)
    os.system("./bin/worldsoop")


def spawn_worldsoop_process() -> Process:
    p = Process(target=run_worldsoop_binary, args=('bob',))
    p.start()


def main(num: int):
    processes: list[Process] = []
    for _ in range(num):
        processes.append(spawn_worldsoop_process())
    
    for process in processes:
        if process is None:
            continue
        process.join()


if __name__ == "__main__":
    main(5)

