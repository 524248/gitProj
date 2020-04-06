from mainTest import MainClass

m = MainClass()
result = m.func_1(1, 2)
print('main: result={}'.format(result))

# get buffer and print it for testing or review
pB = m.loadBuf()
print('main: pB={}'.format(pB))
