num=int(input("Enter the number: "))
num1=0
num2=1
i=2
if num<= 0:
	print ("Enter a positive integer..")
elif num== 1:
	print ("Fibonacci series up to",num,":")
	print (num1)
else:
	print ("Fibonacci series up to",num,":")
	print (num1)
	print (num2)
	while i<num:
		num3=num1+num2
		print (num3)
		num1=num2
		num2=num3
		i=i+1
