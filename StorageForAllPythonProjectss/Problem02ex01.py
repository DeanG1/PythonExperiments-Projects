import math

first = int(input())
second = int(input())
third = int(input())
result = first + second + third
minutes = result // 60
second = result % 60
minutes = math.floor(minutes)

if second < 10:
        print(f"{minutes}:0{second}")
else:
        print(f"{minutes}:{second}")