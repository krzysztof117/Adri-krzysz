import math

a=input("coeficiente del cuadrado:" )
b=input("coeficiente lineal:" )
c=input("coeficiente indep:" )

x1=((-1*b)+ math.sqrt(b*b-(4*a*c)) ) / 2*a
x2=((-1*b)+ math.sqrt(b*b-(4*a*c)) ) / 2*a

print("la raiz es:" , x1)