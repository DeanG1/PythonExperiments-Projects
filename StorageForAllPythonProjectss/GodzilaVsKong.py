# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]


movieBudget = float(input())
statistNum = int(input())
priceForClothesPerStatist = float(input())

decoration = movieBudget * 0.10
totalPriceForClothes = priceForClothesPerStatist * statistNum
if statistNum > 150:
    totalPriceForClothes = totalPriceForClothes - totalPriceForClothes * 0.10

finalPriceForMovie = decoration + totalPriceForClothes
moneyLeft = abs(movieBudget - finalPriceForMovie)
if finalPriceForMovie > movieBudget:
    print("Not enough money!")
    print(f"Wingard needs {moneyLeft:.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {moneyLeft:.2f} leva left.")
