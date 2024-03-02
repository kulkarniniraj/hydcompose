import docker
from pydantic import BaseModel
from typing import List
from icecream import ic

type Client = docker.DockerClient
type Container = docker.models.containers.Container

class ContainerPort(BaseModel):
    host: int 
    container: int 

class ContainerVol(BaseModel):
    host: str 
    container: str

class EnvVar(BaseModel):
    key: str
    val: str

class ContainerDesc(BaseModel):
    name: str 
    image: str
    command: str = ''
    ports: List[ContainerPort] = []
    volumes: List[ContainerVol] = []
    env: List[EnvVar] = []

def init() -> Client:
    client = docker.from_env()
    return client

def start(client: Client, desc: ContainerDesc) -> Container:
    cont = client.containers.run(desc.image,
                      name = desc.name,
                      command = desc.command,
                      ports = _process_ports(desc.ports),
                      volumes = _process_volumes(desc.volumes),
                      environment = _process_env_vars(desc.env),
                      detach = True)
    
    return cont

def get(client: Client, name: str) -> Container | None:
    try:
        return client.containers.get(name)
    except Exception as e:
        # ic(e)
        return None

def stop(cont: Container): 
    cont.stop()

def remove(cont: Container):
    # cont.stop()
    cont.remove(force = True)
    
def prune(client: Client) -> int:
    """
    Returns count of pruned containers
    """
    client.containers.prune()

def _process_ports(ports: List[ContainerPort]) -> dict:
    out = {}
    for port in ports:
        out[port.container] = port.host
    return out

def _process_volumes(vols: List[ContainerVol]) -> list:
    out = []
    for vol in vols:
        out.append(f'{vol.host}:{vol.container}')
    return out

def _process_env_vars(env_vars: List[EnvVar]) -> dict:
    out = {}
    for e in env_vars:
        out[e.key] = e.val

    return out