# dask-for-ml
PoC for using Dask Worker Resources as simple Deep Learning training Resource Manager

#### Installation
Recreate the Conda Environment from `conda.yml`.

#### Starting the cluster:
`start-dask.sh` 
You'll need tmux installed and not sure this works out of box. Make sure you understand what it does.

#### Scheduling a standalone python file
`task.py MEM_NEEDED GPU_NEEDED RUN_LENGTH`.

This is launching a task which uses `MEM_NEEDED` MEM, `GPU_NEEDED` GPU, and idles out for `RUN_LENGTH` secs. It uses `idle.py` behind the hoods. `idle.py` is our machine learning training script in this scenario/

#### Listing Running tasks
```
from distributed import Client
client = Client('127.0.0.1:8786')
client.processing()
```
#### Terminating a running task
Doesn't seem to be possible.
See https://github.com/dask/dask/issues/1183

