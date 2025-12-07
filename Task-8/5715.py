from itertools import *

cnt = 0
x = 15
alph = sorted('кпб')
ans = []
while x !=0:

    for val in product(alph, repeat=x):
        val = ''.join(val)

        if val.count('б') < val.count('п') < val.count('к'):
            c = val.count('к')
            p = val.count('п')
            b = val.count('б')
            new_val = ''
            while c != 0:
                new_val += 'к'
                c = c - 1
            while p != 0:
                new_val += 'п'
                p = p - 1
            while b != 0:
                new_val += 'б'
                b = b - 1

            ans.append(new_val)

    x = x - 1






print(len(set(ans)))
