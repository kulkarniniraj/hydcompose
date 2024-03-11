# hyconfig
A python and hylang based configuration generator tool. Configuration can be written in lisp syntax with basic functions provided by python processor.

## Source overview:
- `main.py`: main entry point. pareses config file, creates list of container_descriptors
and builds dependecy tree

- `tree.py`: dependency tree utility functions

- `dockerlib.py`: All container related data structure. Also contains docker interface functions

- `pubsub.py`: pub-sub model for creating and subscribing to docker (and custom) events

- `configfunc.py`: configuration parser. Builds configuration dict and returns to main
