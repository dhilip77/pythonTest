n = int(input())
x = int(n)
y = 1
while((x - y) > (0.000001)):
	x = int((x+y)/2)
	y = n/x
	print("value of ",x,"Value of",y)
print(x)