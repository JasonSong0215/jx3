num = 10

class ClassName(object):
    '''
         class docs string
    '''
    num = 1

    def __init__(self):
        print('This is a init func')
        global num  # 使用global 可以访问到全局变量
        num += 10
        print('gloal num:', num)
        ClassName.num += 1
        print('ClassName.num:', ClassName.num)

    def func(self):
        global num  # 使用global 可以访问到全局变量
        num += 10
        print('ClassName.num:', ClassName.num)

    def start(self):
        self.func()




if __name__ == '__main__':
    ClassName()
    print(num)
    ClassName().func()
    print(num)
    ClassName().start()
    print(num)


