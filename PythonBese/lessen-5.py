# работа с библиотекой

# подключение библиотеки
import random
print(random.randint(1,100))

# подключение библиотеки через псевдоним
import random as r
print(r.randint(1,300))

# подключение одной команды из библиотеки
from random import  randint
print(randint(1,400))

# подключение одной команды из библиотеки через псевдоним
from random import  randint as ri
print(ri(1,400))

# подключение двух команд из библиотеки
from random import  randint, choice
print(randint(1,400), choice([7,5,4,3,8]))

# подключение двух команд из библиотеки через псевдонимы
from random import  randint as ri, choice as sh
print(ri(1,400), sh([3,4,3,4,5,3,4]))

# подключение всех команд из библиотеки
from random import*
print(randint(1,400), choice([2,3,4]))
