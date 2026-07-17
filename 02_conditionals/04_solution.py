fruitsOptions = ["Apple", "Banana", "Cherry", "Date"]


fruitStatus = ("Unripe", "Ripe", "Overripe")

fruitsColor = {
    "Apple" : {
        "Red" : fruitStatus[1],
        "Green" : fruitStatus[0],
        "Yellow" : fruitStatus[2],
    },
    "Banana" : {
        "Green" : fruitStatus[0],
        "Yellow" : fruitStatus[1],
        "Brown" : fruitStatus[2],
    },
    "Cherry" : {
        "Red" : fruitStatus[1],
    },
    "Date" : {
        "Brown" : fruitStatus[2],
    }
}

userFruitInput = 1
# userFruitColorInput = 1

# if (userFruitInput > len(fruitsOptions)) and userFruitInput > 0 :
#     print("Please choose in given options")
#     exit()
# targetFruit = fruitsOptions[userFruitInput - 1]

# if (userFruitColorInput > len(fruitsColor[targetFruit])) and userFruitInput > 0 :
#     print("Please choose in given options")
#     exit()

targetFruit = fruitsOptions[userFruitInput - 1]
targetFruitColor = "Green"
# print(fruitsColor[targetFruit])
fruitColorValue = fruitsColor[targetFruit][targetFruitColor]
# targetFruitColors = fruitsColor[targetFruit][fruitColorValue]


print(fruitColorValue)
# print(targetFruitColors)






