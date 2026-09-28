for number in range(1,21,):
    if number%5 == 0:
        divisible = "divisible by 5"
    else:
        divisible = "not divisible by 5"
    if number%2 == 0:
        even = "is even"
    else:
        even = "is odd"
    print(f"{number} {even} and is {divisible}")
#ends in 5 or 0 then divisible by five
