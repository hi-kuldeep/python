input_str = 'Raahu'

for char in input_str:
    if input_str.count(char) == 1:
        print("First non-repeated character is ", char)
        break
    
