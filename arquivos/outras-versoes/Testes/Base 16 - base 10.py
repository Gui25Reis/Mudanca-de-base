print("ATENÇÃO: Coloque os valores das letras")
print("A=10, B=11, C=12, D=13, E=14, F=15")

p1 = int(input("P1: ", ))
p2 = int(input("P2: ", ))
p3 = int(input("P3: ", ))
p4 = int(input("P4: ", ))
p5 = int(input("P5: ", ))
p6 = int(input("P6: ", ))


x1 = p1*1
x2 = p2*16
x3 = p3*16**2
x4 = p4*16**3
x5 = p5*16**4
x6 = p6*16**5


print(x1,x2,x3,x4,x5,x6) 

cal = x1+x2+x3+x4+x5+x6

print("Base 2 -> base 10 =", cal)

