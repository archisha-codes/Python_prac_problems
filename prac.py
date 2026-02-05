r= range(10)
r=iter(r)
while True:
    try:
        d=next(r)
    print(d)
except stopIteration as e :
break