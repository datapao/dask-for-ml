#!/usr/bin/env python

from distributed import Client
import sys


def run_training(sec):
    import subprocess
    subprocess.run(["python", "idle.py", str(sec)])

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("task.py MEM GPU IDLE_SEC")
    resources = {'MEM': int(sys.argv[1]), 'GPU': int(sys.argv[2])}
    idle_secs = int(sys.argv[3])
    task_name = "task mem:{}, gpu:{}, idle_secs:{}".format(sys.argv[1], sys.argv[2], sys.argv[3])

    print(f"starting {task_name}")

    client = Client('127.0.0.1:8786')
    run = client.submit(run_training, idle_secs,  resources=resources, key=task_name)
    run.result()
(dask) ubuntu@ip-172-31-16-39:~/dask-dl$ cat idle.py
import time
import sys

if len(sys.argv) > 1:
    sleep_time = int(sys.argv[1])
else:
    sleep_time = 10

print("idle.py: Sleeping {} sec...".format(sleep_time));
time.sleep(sleep_time);
print("idle.py: Done");