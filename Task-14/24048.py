#23
from string import printable

u = 100000
for p in range(33, 100):
    print(p)
    if (20*p**2 + 24*p**1 + 29*p**0) + (16*p**6 + 24*p**5 + 21*p**4 + 24*p**3 + 13*p**2 + 23*p**1 + 18*p**0) == (22*p**4 + 14*p**3 + 14*p**2 + 24*p**1 + 32*p**0) * (1*p**2 + 0*p**1 + 0*p**0) - 20194023088:
        print(p)
        u = min(u, p)
print(25*u**2 + 30*u**1 + 27*u**0)

#int('KOT', int(p, 36)) + int('GOLODNI', int(p, 36)) == int('MEEOW', int(p, 36)) * int('100', int(p, 36))