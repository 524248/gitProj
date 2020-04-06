from mainTest import MainClass

m = MainClass()
result = m.func_1(1, 2)
print('main: result={}'.format(result))

pB = m.loadBuf()
print('main: pB={}'.format(pB))
