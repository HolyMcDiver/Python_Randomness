x = int(input("Δώσε έναν τριψήφιο αριθμό: "))
x1= x/100 #find first digit
yp = x%100 #find the last 2 digits
x2 = yp/10 #find second digit
x3 = yp%10 #find third digit
y = x1+x2+x3 #use all 3 digits for addition
print y # print sum
# profit!
