from pydantic import ValidationError
from icecream import ic

import dockerlib as dl

CONFIG_STATE = {
    'containers': [dl.Stub(name = 'root_stub')]
}

def container(image, name, cmd = '', ports = [], volumes = [],
              env = [], depends_on = [ {'name':'root_stub'} ]):
    o_container(image, name, cmd, ports, volumes, env, depends_on)
    
def o_container(image, name, cmd = '', ports = [], volumes = [],
              env = [], depends_on = []):
    try:
        desc = dl.ContainerDesc(
            name = name,
            image = image,
            command = cmd,
            ports = [dl.ContainerPort(**port) for port in ports],
            volumes = [dl.ContainerVol(**vol) for vol in volumes],
            env = [dl.EnvVar(**env_var) for env_var in env],
            depends_on = [dl.Dependency(**dep) for dep in depends_on]
        )
        
        CONFIG_STATE['containers'].append(desc)
    except ValidationError as e:
        ic(e.errors())
    
