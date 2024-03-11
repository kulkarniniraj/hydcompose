import hy 
import sys
from icecream import ic
from pathlib import Path
import yaml
import os
from fire import Fire 
from enum import Enum
from pprint import pprint, pformat

from configfunc import *
import tree


def main(main_config_file):
    """
    Run containers from main config file
    """
    with open(main_config_file) as f:
        stream = hy.read_many(f)
        for expr in stream:
            hy.eval(expr)        

    # pprint(CONFIG_STATE, depth = 2)


    node_dict = tree.create_dep_tree(CONFIG_STATE['containers'])

    for _, node in node_dict.items():
        tree.print_node(node)
        print()

if __name__ == '__main__':
    Fire(main)