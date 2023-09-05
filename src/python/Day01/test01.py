def write(a,b,c):
    print(a); print(b); print(c)
write("ddd", "ccc","sds")

def write1(*args):
    print(args)
write('a', 'aa', 'aaaa')

def write(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"kwargs.get('{key}'):{value}")
              
write(a= 'sds', b= ';23', c= '12312')



poe = lambda x : x*x if x<20 else x*2
print(poe(100))