import sys
import time


def func(x):
    return x * x 
func1 = lambda x: x*x
func2 = lambda x, y: x if x > y else y

value = ( lambda x, y: x if x > y else y)(10, 20)


def func(callback, a, b):
    return callback(a, b)


# fp = open('data.txt', 'w')
# print("pythons is good", file = fp)

with open('data.txt', 'w') as fp:
    print('this is SPARTA', file=fp)
print("the end")

for i in range(5):
    print(i, end=' ', flush=True)
    time.sleep(1)
