mayor = 0
residuo = 0 
#1
#2
residuo = mayor % 2
if residuo == 0:
    print("El número", mayor, " es par porque su residuo es 0")
elif residuo != 0:
    print("El número", mayor, "es impar porque su residuo es ", residuo)
#3
n = 1
while n <= mayor:
    print(n)
    n = n + n
=======
num1 = int(input('Ingrese un número entero: '))
num2 = int(input('Ingrese otro número entero: '))
if num1 > num2:
    mayor = num1
    print('El número mayor es:', num1)
elif num2 > num1:
    mayor = num2
    print('El número mayor es:', num2)