print('Resultdo: a partir do 1º zero do quociente')
print('Máx. 15 dígitos')
print()
a = int(input("Base inicial: ", ))
b = int(input("Base final: ", ))
if a != 2:
    print()
    n = int(input('Número, SEM ESPAÇO: ', ))
    print()
    d1 = int(n/(10**14))
    r1 = int(n%(10**14))
    d2 = int(r1/(10**13))
    r2 = int(r1%(10**13))
    d3 = int(r2/(10**12))
    r3 = int(r2%(10**12))
    d4 = int(r3/(10**11))
    r4 = int(r3%(10**11))
    d5 = int(r4/(10**10))
    r5 = int(r4%(10**10))
    d6 = int(r5/(10**9))
    r6 = int(r5%(10**9))
    d7 = int(r6/(10**8))
    r7 = int(r6%(10**8))
    d8 = int(r7/(10**7))
    r8 = int(r7%(10**7))
    d9 = int(r8/(10**6))
    r9 = int(r8%(10**6))
    d10 = int(r9/(10**5))
    r10 = int(r9%(10**5))
    d11 = int(r10/(10**4))
    r11 = int(r10%(10**4))
    d12 = int(r11/(10**3))
    r12 = int(r11%(10**3))
    d13 = int(r12/10**2)
    r13 = int(r12%10**2)
    d14 = int(r13/10)
    r14 = int(r13%10)
    d15 = int(r14/1)
    r15 = int(r14%1)
    s1=(d15*1)+(d14*a)+(d13*a**2)+(d12*a**3)+(d11*a**4)+(d10*a**5)+(d9*a**6)+(d8*a**7)+(d7*a**8)+(d6*a**9)+(d5*a**10)+(d4*a**11)+(d3*a**12)+(d2*a**13)+(d1*a**14)         
    print("Base:",a,"-> Base: 10 =", s1)
    c1 = int(s1/b)
    c2 = int(c1/b)
    c3 = int(c2/b)
    c4 = int(c3/b)
    c5 = int(c4/b)
    c6 = int(c5/b)
    c7 = int(c6/b)
    c8 = int(c7/b)
    c9 = int(c8/b)
    c10 = int(c9/b)
    c11 = int(c10/b)
    c12 = int(c11/b)
    c13 = int(c12/b)
    c14 = int(c13/b)
    c15 = int(c14/b)
    c16 = int(c15/b)
    c17 = int(c16/b)
    c18 = int(c17/b)
    c19 = int(c18/b)
    c20 = int(c19/b)
    c21 = int(c20/b)
    c22 = int(c21/b)
    c23 = int(c22/b)
    c24 = int(c23/b)
    c25 = int(c24/b)
    c26 = int(c25/b)
    c27 = int(c26/b)
    c28 = int(c27/b)
    c29 = int(c28/b)
    c30 = int(c29/b)
    r1 = int(s1-(c1*b))
    r2 = int(c1-(c2*b))
    r3 = int(c2-(c3*b))
    r4 = int(c3-(c4*b))
    r5 = int(c4-(c5*b))
    r6 = int(c5-(c6*b))
    r7 = int(c6-(c7*b))
    r8 = int(c7-(c8*b))
    r9 = int(c8-(c9*b))
    r10 = int(c9-(c10*b))
    r11 = int(c10-(c11*b))
    r12 = int(c11-(c12*b))
    r13 = int(c12-(c13*b))
    r14 = int(c13-(c14*b))
    r15 = int(c14-(c15*b))
    r16 = int(c15-(c16*b))
    r17 = int(c16-(c17*b))
    r18 = int(c17-(c18*b))
    r19 = int(c18-(c19*b))
    r20 = int(c19-(c20*b))
    r21 = int(c20-(c21*b))
    r22 = int(c21-(c22*b))
    r23 = int(c22-(c23*b))
    r24 = int(c23-(c24*b))
    r25 = int(c24-(c25*b))
    r26 = int(c25-(c26*b))
    r27 = int(c26-(c27*b))
    r28 = int(c27-(c28*b))
    r29 = int(c28-(c29*b))
    r30 = int(c29-(c30*b))
    print()
    print("Quociente:",c30,c29,c28,c27,c26,c25,c24,c23,c22,c21,c20,c19,c18,c17,c16,c15,c14,c13,c12,c11,c10,c9,c8,c7,c6,c5,c4,c3,c2,c1)
    print("Resultado:"  ,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1)
    print()
if (a == 2 and a > 10):
    print()
    print('Ex: 356 -> 000000000000356   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ')
    print('                             | | | | | | | | | | | | | | | ')
    p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15 = input('Número, COM ESPAÇO: ', ). split()
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
    p12 = int(p12)
    p13 = int(p13)
    p14 = int(p14)
    p15 = int(p15)
    s2 = (p15*1)+(p14*a)+(p13*a**2)+(p12*a**3)+(p11*a**4)+(p10*a**5)+(p9*a**6)+(p8*a**7)+(p7*a**8)+(p6*a**9)+(p5*a**10)+(p4*a**11)+(p3*a**12)+(p2*a**13)+(p1*a**14)
    print("Base:",a," -> Base: 10 =", s2)
    c1 = int(s2/b)
    c2 = int(c1/b)
    c3 = int(c2/b)
    c4 = int(c3/b)
    c5 = int(c4/b)
    c6 = int(c5/b)
    c7 = int(c6/b)
    c8 = int(c7/b)
    c9 = int(c8/b)
    c10 = int(c9/b)
    c11 = int(c10/b)
    c12 = int(c11/b)
    c13 = int(c12/b)
    c14 = int(c13/b)
    c15 = int(c14/b)
    c16 = int(c15/b)
    c17 = int(c16/b)
    c18 = int(c17/b)
    c19 = int(c18/b)
    c20 = int(c19/b)
    c21 = int(c20/b)
    c22 = int(c21/b)
    c23 = int(c22/b)
    c24 = int(c23/b)
    c25 = int(c24/b)
    c26 = int(c25/b)
    c27 = int(c26/b)
    c28 = int(c27/b)
    c29 = int(c28/b)
    c30 = int(c29/b)
    r1 = int(s2-(c1*b))
    r2 = int(c1-(c2*b))
    r3 = int(c2-(c3*b))
    r4 = int(c3-(c4*b))
    r5 = int(c4-(c5*b))
    r6 = int(c5-(c6*b))
    r7 = int(c6-(c7*b))
    r8 = int(c7-(c8*b))
    r9 = int(c8-(c9*b))
    r10 = int(c9-(c10*b))
    r11 = int(c10-(c11*b))
    r12 = int(c11-(c12*b))
    r13 = int(c12-(c13*b))
    r14 = int(c13-(c14*b))
    r15 = int(c14-(c15*b))
    r16 = int(c15-(c16*b))
    r17 = int(c16-(c17*b))
    r18 = int(c17-(c18*b))
    r19 = int(c18-(c19*b))
    r20 = int(c19-(c20*b))
    r21 = int(c20-(c21*b))
    r22 = int(c21-(c22*b))
    r23 = int(c22-(c23*b))
    r24 = int(c23-(c24*b))
    r25 = int(c24-(c25*b))
    r26 = int(c25-(c26*b))
    r27 = int(c26-(c27*b))
    r28 = int(c27-(c28*b))
    r29 = int(c28-(c29*b))
    r30 = int(c29-(c30*b))
    print()
    print("Quociente:",c30,c29,c28,c27,c26,c25,c24,c23,c22,c21,c20,c19,c18,c17,c16,c15,c14,c13,c12,c11,c10,c9,c8,c7,c6,c5,c4,c3,c2,c1)
    print("Resultado:"  ,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1)
    print()
if b > 10:
        print("A=10 B=11 C=12 D=13 E=14 F=15")
input()
