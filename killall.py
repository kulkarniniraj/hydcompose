import docker 
from icecream import ic

client = docker.from_env()

def main():
    for cont in client.containers.list(all = True):
        ic(f'Removing container', cont.name)
        cont.stop()
        cont.remove()

if __name__ == '__main__':
    main()
