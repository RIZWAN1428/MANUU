minimum = int(input("Enter minimum value: "))
maximum = int(input("Enter maximum value: "))

print("Prime numbers between",minimum,"and",maximum,"are:")

for num in range(minimum,maximum + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
