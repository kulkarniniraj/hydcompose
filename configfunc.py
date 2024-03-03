from pydantic import ValidationError
from icecream import ic

import dockerlib as dl

CONFIG_STATE = {
    'containers': []
}

def container(image, name, cmd = '', ports = [], volumes = [],
              env = []):    
    try:
        desc = dl.ContainerDesc(
            name = name,
            image = image,
            command = cmd,
            ports = [dl.ContainerPort(**port) for port in ports],
            volumes = [dl.ContainerVol(**vol) for vol in volumes],
            env = [dl.EnvVar(**env_var) for env_var in env]
        )
        
        CONFIG_STATE['containers'].append(desc)
    except ValidationError as e:
        ic(e.errors())
    
