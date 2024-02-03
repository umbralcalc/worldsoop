import subprocess

from concurrent.futures import ThreadPoolExecutor, as_completed


def run_worldsoop_process(*args, **kwargs) -> str:
    cmd = ["./bin/worldsoop"]
    for arg in args:
        cmd += [f"{arg}"]
    for k, v in kwargs.items():
        cmd += [f"--{k}", f"{v}"]
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


def spawn_worldsoop_processes(
    num: int, 
    max_workers: int, 
    *args, 
    **kwargs
):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(run_worldsoop_process, *args, **kwargs): i 
            for i in range(num)
        }

        for future in as_completed(futures):
            i = futures[future]
            try:
                result = future.result()
            except Exception as e:
                print(f"Go process {i} failed!\nError: {str(e)}")
