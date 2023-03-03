# Programa para verificar si un número es de cuatro dígitos y positivo

print("-----------------------------------------------")
print("-----------------Tarea No3---------------------")
print("-----------------------------------------------")

#Imput

n=int(input("Dígite un número: "))
y=n//1000
x=(n*-1)//1000
#Processing y output

if y>=1 and y<10:
    print("-----------------------------------------------")
    print(str(n) + " es positivo y tiene cuatro dígitos")
    print("-----------------------------------------------")
else:
    if y>=0 and y<1:
        print("-----------------------------------------------")
        print(str(n) + " es positivo pero, no es de cuatro dígitos")
        print("-----------------------------------------------")
    else:
        if x>=1 and x<10:
            print("-----------------------------------------------")
            print(str(n) + " es negativo pero, es de cuatro dígitos")
            print("-----------------------------------------------")
        else:
            print("-----------------------------------------------")
            print(str(n) + " es negativo y no es de cuatro dígitos")
            print("-----------------------------------------------")
