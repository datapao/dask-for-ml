#!/usr/bin/env bash
tmux new-session -d 'dask-scheduler --host 0.0.0.0'
tmux split-window -v 'dask-worker localhost:8786 --resources "GPU=1,MEM=20"'
tmux split-window -h
tmux new-window 'dask-worker localhost:8786 --resources "GPU=10,MEM=2"'
tmux -2 attach-session -d
