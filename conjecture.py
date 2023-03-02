import numpy as np
g = np.random.randint(0,1000)

rg = 8
print("your remaining guesses : 8")
a = int(input("please guess a number between one and one thousnd : "))
for i in range(8) :
    if a == g :
        print("you win!\nnumber was {}".format(g))
        break
    elif a > g :
        rg -= 1
        print("your guess is more than the desired number")
        a = int(input("please guess a number between one and one thousnd : "))
    elif a < g :
        rg -= 1
        print("your guess is less than the desired number")
        a = int(input("please guess a number between one and one thousnd : "))
    print("your remaining guesses : {}".format(rg))
    if rg == 0 and a == g :
        print("you win!\nnumber was {}".format(g))
    elif rg == 0 and a != g :
        print("you lose!\ndesired number was {}".format(g))