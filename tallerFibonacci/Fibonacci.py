#Nazly Olmos - serie fibonacci
fibonacci = [0]
x = 0
y = 1
temp = 1
numero = int(input("Ingrese el numero para calcular la serie fibonacci: "))
while temp < numero:
	if temp  < numero:
		fibonacci.append(temp)
	temp = x + y
	x = y
	y = temp
		
print 'Serie Fibonacci: ', fibonacci