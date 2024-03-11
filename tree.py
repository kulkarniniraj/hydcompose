from pydantic import BaseModel
from typing import List, Dict
from collections import defaultdict

import dockerlib as dl

class TreeNode(BaseModel):
    container_desc: dl.ContainerDesc | dl.Stub
    parents: List['TreeNode'] = []
    # {event: [children]} mapping
    children: Dict = defaultdict(lambda: list()) 
    
def create_dep_tree(container_lst: List[dl.ContainerDesc | dl.Stub]) -> Dict:
    """
    Main API: takes container descriptor list and returns dependency tree
    """
    node_dict = create_node_dict(container_lst)
    for container in container_lst:
        add_node_deps(container.name, node_dict)

    return node_dict

def create_node_dict(container_lst: List[dl.ContainerDesc | dl.Stub]) -> Dict[str, TreeNode]:
    out = {}
    for node in container_lst:
        out[node.name] = TreeNode(container_desc = node)

    return out

def add_node_deps(container_name: str, node_dict: Dict[str, TreeNode]):
    node = node_dict[container_name]
    for dep in node.container_desc.depends_on:
        parent_node = node_dict[dep.name]

        node.parents.append(parent_node)
        parent_node.children[dep.event].append(node)

def print_node(node: TreeNode):
    print(f'name: {node.container_desc.name}')
    print(f'parents: {[x.container_desc.name for x in node.parents]}')
    print(f'children: ')
    for event in node.children:
        print(f'\tevent: {event} childrent: ' + 
              f'{[x.container_desc.name for x in node.children[event]]}')
