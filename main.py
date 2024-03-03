import hy 
import sys
from icecream import ic
from pathlib import Path
import yaml
import os
from fire import Fire 
from enum import Enum

from configfunc import *

def main(main_config_file):
    """
    Run containers from main config file
    """
    with open(main_config_file) as f:
        stream = hy.read_many(f)
        for expr in stream:
            hy.eval(expr)        

    ic(CONFIG_STATE)

if __name__ == '__main__':
    Fire(main)