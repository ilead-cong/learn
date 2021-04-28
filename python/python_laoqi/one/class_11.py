##########################################
#生成器， 斐波那契数列
#########################################

import itertools

def fibs():
    prev, cuur = 0, 1
    while True:
        yield prev
        prev, cuur = cuur, prev + cuur

print(list(itertools.islice(fibs(), 10)))