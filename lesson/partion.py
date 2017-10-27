from functools import partial
def revers(a):
    print (a[::-1])
def main():
    b = 'hello'
    func = partial(revers, b)
    operations = []
    operations.append(func)
    list(map(lambda f: f(), operations))
if __name__ == '__main__':
    main()