#In this program, it's concept is to take a decimal positive number and switch
#the degits around so if 45 was inputed, you would get 54. Please note that
#the result will give a working number, meaning that your output could be used further more.

#x = int(input("Input a decimal positive number please: "))
#if x<= 0:
#    print ("You inputed a wrong number. Prepare to die.")
#else:
#    x1 = x / 10
#    x2 = x % 10
#    x = x*10 +x2
#    print(x)

kek = int(input("Give me your soul: "))
kek_reverse = int(str(kek % 10) + str(int(kek / 10)))
print(kek_reverse)
print (kek_reverse + 1)
