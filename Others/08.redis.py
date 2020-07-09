import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
print(type(r))

num=r.get('num')
print(type(num),num)

all_key = r.keys('*')
print(type(all_key),all_key)

exists=r.exists('xiaowang')
print(type(exists),exists)

r.rpush('pyl1','7','b','f','k','96')

print(r.lrange('pyl1',0,-1))
print(r.rpop('pyl1'))
print(r.lrange('pyl1',0,-1))

print(r.ltrim('pyl1',0,1))
print(r.lrange('pyl1',0,-1))

# pipe = r.pipeline()
# 打包发送

with r.pipeline() as pipe:
	pipe.multi()
	pipe.incr("num")
	pipe.incr("num")
	values = pipe.execute()

# watch key 乐观锁



