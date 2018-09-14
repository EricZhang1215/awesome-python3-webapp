import www.orm
from www.models import User, Blog, Comment
import asyncio

async def test(loop):
    await www.orm.create_pool(loop,user='root', password='root', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    #yield from u.save()

    await u.save()

async def find(loop):
    await www.orm.create_pool(loop, user='root', password='root', database='awesome')
    rs = await User.findAll()
    print('查找测试： %s' % rs)

# for x in test():
#     pass

loop = asyncio.get_event_loop()
loop.run_until_complete(find(loop))
loop.run_forever()
