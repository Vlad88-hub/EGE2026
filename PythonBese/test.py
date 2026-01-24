import random
import time

random.seed(time.time_ns())

fruits = ["яблоко", "банан", "апельсин", "киви"]
fruit = random.choice(fruits)
print(f"Случайный фрукт: {fruit}")
