import hy 
import sys
from icecream import ic
from pathlib import Path
import yaml
import os
from fire import Fire 
from enum import Enum
import docker 

client = docker.from_env()

STATE = {
    'containers': []
}

def container(image, name = None, cmd = None):
    client.containers.run(image = image, command = cmd, name = name)
    
def main(main_config_file):
    """
    Run containers from main config file
    """
    with open(main_config_file) as f:
        stream = hy.read_many(f)
        for expr in stream:
            hy.eval(expr)        

if __name__ == '__main__':
    Fire(main)