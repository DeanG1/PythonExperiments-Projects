# По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е
# да напишете програма, с която ще разберете дали имате достатъчно време да изгледате епизода.
# По време на почивката отделяте време за обяд и време за отдих.
# Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход
# От конзолата се четат 3 реда:
# 1.	Име на сериал – текст
# 2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
# 3.	Продължителност на почивката  – цяло число в диапазона [10… 120]

from math import ceil

serialName = input()
episodeTime = int(input())
breakTime = int(input())

lunchTime = breakTime * 1/8
restTime = breakTime * 1/4
leftTime = breakTime - lunchTime - restTime
neededTime = abs(episodeTime - leftTime)



if leftTime >= episodeTime:
    print(f"You have enough time to watch {serialName} and left with {ceil(neededTime)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serialName}, you need {ceil(neededTime)} more minutes.")