"""
Test docker lib
"""
import dockerlib as dl
from icecream import ic

cli = dl.init()

cont = dl.get(cli, 'pg')
ic(cont)
if cont is not None:
    dl.remove(cont)
# ic(dl.prune(cli))

cont = dl.start(cli, ic(dl.ContainerDesc(name = 'pg', image = 'postgres',
    env = [dl.EnvVar(key = 'POSTGRES_PASSWORD', val = 'test1234')])))

"""
Test pubsub
"""
import pubsub as ps
from icecream import ic

ps.init()

try:
    ic(ps.subscribe_topic('src1', 'topic1', lambda x: x))

    ps.add_topic('src1', 'topic1')
    ic(ps.subscribe_topic('src1', 'topic1', lambda x: ic(x)))
    ic(ps.subscribe_topic('src1', 'topic1', lambda x: ic('second callback', x)))
    ps.publish_message('src1', 'topic1', 'message1')
    ps.publish_message('src1', 'topic1', 'message2')
    ps.publish_message('src1', 'topic1', 'message3')
except:
    pass
finally:
    ps.exit()
