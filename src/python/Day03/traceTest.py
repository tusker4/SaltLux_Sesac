def A():
    return 10/0


def B():
    return A()


def C():
    return B()

result = C()
print(result)


