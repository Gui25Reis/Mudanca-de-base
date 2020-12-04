print("Modo de colocar o número (máx. de 11 dígitos) -> exemplo: 356 -> 0 0 0 0 0 0 0 0 3 5 6.")
print('O resultdo começa com o número abaixo do "zero" do quociente')
bi = int(input("Base inicial: ", ))
bf = int(input("Base final: ", ))

p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11 = input('Digite o número]: ', ). split()

p1 = int(p1)
p2 = int(p2)
p3 = int(p3)
p4 = int(p4)
p5 = int(p5)
p6 = int(p6)
p7 = int(p7)
p8 = int(p8)
p9 = int(p9)
p10 = int(p10)
p11 = int(p11)

x1 = p11*1
x2 = p10*bi
x3 = p9*bi**2
x4 = p8*bi**3
x5 = p7*bi**4
x6 = p6*bi**5
x7 = p5*bi**6
x8 = p4*bi**7
x9 = p3*bi**8
x10 = p2*bi**9
x11 = p1*bi**10

#print("Resultado das potências: ", x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11) 

cal = x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11

print("Base:",bi," -> Base: 10 =", cal)

a = (cal)

c1 = int(a/bf)
c2 = int(c1/bf)
c3 = int(c2/bf)
c4 = int(c3/bf)
c5 = int(c4/bf)
c6 = int(c5/bf)
c7 = int(c6/bf)
c8 = int(c7/bf)
c9 = int(c8/bf)
c10 = int(c9/bf)
c11 = int(c10/bf)
c12 = int(c11/bf)
c13 = int(c12/bf)
c14 = int(c13/bf)
c15 = int(c14/bf)
c16 = int(c15/bf)
c17 = int(c16/bf)
c18 = int(c17/bf)
c19 = int(c18/bf)
c20 = int(c19/bf)

r1 = int(a-(c1*bf))
r2 = int(c1-(c2*bf))
r3 = int(c2-(c3*bf))
r4 = int(c3-(c4*bf))
r5 = int(c4-(c5*bf))
r6 = int(c5-(c6*bf))
r7 = int(c6-(c7*bf))
r8 = int(c7-(c8*bf))
r9 = int(c8-(c9*bf))
r10 = int(c9-(c10*bf))
r11 = int(c10-(c11*bf))
r12 = int(c11-(c12*bf))
r13 = int(c12-(c13*bf))
r14 = int(c13-(c14*bf))
r15 = int(c14-(c15*bf))
r16 = int(c15-(c16*bf))
r17 = int(c16-(c17*bf))
r18 = int(c17-(c18*bf))
r19 = int(c18-(c19*bf))
r20 = int(c19-(c20*bf))

#if ( c20 and c19 and c18 and c17 and c16 and c15 and c14 and c13 and c12 and c11 and c10 and c9 and c8 and c7 and c6 and c5 and c4 and c3 and c2 and c1 != 0 ):
print("Quociente:",c20,c19,c18,c17,c16,c15,c14,c13,c12,c11,c10,c9,c8,c7,c6,c5,c4,c3,c2,c1)
print("Resultado:"  ,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1)

print("A=10 B=11 C=12 D=13 E=14 F=15")
input()
