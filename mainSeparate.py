import config  as cf

class BaseClass(object):
    def __init__(self):
        self.global_var_1 = 4
        self.global_var_2 = 2


    def func_1(self, x, y):
        r = x
        s = y
        print('func_1: r={}  s={}'.format(r, s))
        return r, s


    def func_2(self, z):
        t = z
        return


    def loadBuf(self):
        cf.pixBuf = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        return cf.pixBuf