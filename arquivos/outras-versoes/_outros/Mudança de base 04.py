print('Resultdo: a partir do 1º zero do quociente')
print('Máx. 15 dígitos')
print()
bi = int(input("Base inicial: ", ))
bf = int(input("Base final: ", ))

if bi == 2:
    print()
    print('Ex: 356 -> 000000000000356   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ')
    print('                             | | | | | | | | | | | | | | | ')
    p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15 = input('Digite o número, COM ESPAÇO: ', ). split()

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

    x1 = p15*1
    x2 = p14*bi
    x3 = p13*bi**2
    x4 = p12*bi**3
    x5 = p11*bi**4
    x6 = p10*bi**5
    x7 = p9*bi**6
    x8 = p8*bi**7
    x9 = p7*bi**8
    x10 = p6*bi**9
    x11 = p5*bi**10
    x12 = p4*bi**11
    x13 = p3*bi**12
    x14 = p2*bi**13
    x15 = p1*bi**14

    #print("Resultado das potências: ", x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15) 

    cal = x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+x15

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
    c21 = int(c20/bf)
    c22 = int(c21/bf)
    c23 = int(c22/bf)
    c24 = int(c23/bf)
    c25 = int(c24/bf)
    c26 = int(c25/bf)
    c27 = int(c26/bf)
    c28 = int(c27/bf)
    c29 = int(c28/bf)
    c30 = int(c29/bf)

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
    r21 = int(c20-(c21*bf))
    r22 = int(c21-(c22*bf))
    r23 = int(c22-(c23*bf))
    r24 = int(c23-(c24*bf))
    r25 = int(c24-(c25*bf))
    r26 = int(c25-(c26*bf))
    r27 = int(c26-(c27*bf))
    r28 = int(c27-(c28*bf))
    r29 = int(c28-(c29*bf))
    r30 = int(c29-(c30*bf))
    

    #if ( c20 and c19 and c18 and c17 and c16 and c15 and c14 and c13 and c12 and c11 and c10 and c9 and c8 and c7 and c6 and c5 and c4 and c3 and c2 and c1 != 0 ):
    print()
    print("Quociente:",c30,c29,c28,c27,c26,c25,c24,c23,c22,c21,c20,c19,c18,c17,c16,c15,c14,c13,c12,c11,c10,c9,c8,c7,c6,c5,c4,c3,c2,c1)
    print("Resultado:"  ,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1)
    print()

elif bi > 10:
    print()
    print('Ex: 356 -> 000000000000356   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ')
    print('                             | | | | | | | | | | | | | | | ')
    p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15 = input('Digite o número, COM ESPAÇO: ', ). split()

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

    x1 = p15*1
    x2 = p14*bi
    x3 = p13*bi**2
    x4 = p12*bi**3
    x5 = p11*bi**4
    x6 = p10*bi**5
    x7 = p9*bi**6
    x8 = p8*bi**7
    x9 = p7*bi**8
    x10 = p6*bi**9
    x11 = p5*bi**10
    x12 = p4*bi**11
    x13 = p3*bi**12
    x14 = p2*bi**13
    x15 = p1*bi**14

    #print("Resultado das potências: ", x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15) 

    cal = x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+x15

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
    c21 = int(c20/bf)
    c22 = int(c21/bf)
    c23 = int(c22/bf)
    c24 = int(c23/bf)
    c25 = int(c24/bf)
    c26 = int(c25/bf)
    c27 = int(c26/bf)
    c28 = int(c27/bf)
    c29 = int(c28/bf)
    c30 = int(c29/bf)

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
    r21 = int(c20-(c21*bf))
    r22 = int(c21-(c22*bf))
    r23 = int(c22-(c23*bf))
    r24 = int(c23-(c24*bf))
    r25 = int(c24-(c25*bf))
    r26 = int(c25-(c26*bf))
    r27 = int(c26-(c27*bf))
    r28 = int(c27-(c28*bf))
    r29 = int(c28-(c29*bf))
    r30 = int(c29-(c30*bf))
    

    #if ( c20 and c19 and c18 and c17 and c16 and c15 and c14 and c13 and c12 and c11 and c10 and c9 and c8 and c7 and c6 and c5 and c4 and c3 and c2 and c1 != 0 ):
    print()
    print("Quociente:",c30,c29,c28,c27,c26,c25,c24,c23,c22,c21,c20,c19,c18,c17,c16,c15,c14,c13,c12,c11,c10,c9,c8,c7,c6,c5,c4,c3,c2,c1)
    print("Resultado:"  ,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1)
    print()
    print("A=10 B=11 C=12 D=13 E=14 F=15")


else:
    print()
    num = int(input('Digite o número, SEM ESPAÇO: ', ))
    print()
    
#Separando por dezenas, centenas..

    div_1 = int(num/(10**14))
    res_1 = int(num%(10**14))

    div_2 = int(res_1/(10**13))
    res_2 = int(res_1%(10**13))

    div_3 = int(res_2/(10**12))
    res_3 = int(res_2%(10**12))

    div_4 = int(res_3/(10**11))
    res_4 = int(res_3%(10**11))

    div_5 = int(res_4/(10**10))
    res_5 = int(res_4%(10**10))

    div_6 = int(res_5/(10**9))
    res_6 = int(res_5%(10**9))

    div_7 = int(res_6/(10**8))
    res_7 = int(res_6%(10**8))

    div_8 = int(res_7/(10**7))
    res_8 = int(res_7%(10**7))

    div_9 = int(res_8/(10**6))
    res_9 = int(res_8%(10**6))

    div_10 = int(res_9/(10**5))
    res_10 = int(res_9%(10**5))

    div_11 = int(res_10/(10**4))
    res_11 = int(res_10%(10**4))

    div_12 = int(res_11/(10**3))
    res_12 = int(res_11%(10**3))

    div_13 = int(res_12/10**2)
    res_13 = int(res_12%10**2)

    div_14 = int(res_13/10)
    res_14 = int(res_13%10)

    div_15 = int(res_14/1)
    res_15 = int(res_14%1)


#Transformando pra base de 10:

    m1_bi = div_15*1
    m2_bi = div_14*bi
    m3_bi = div_13*bi**2
    m4_bi = div_12*bi**3
    m5_bi = div_11*bi**4
    m6_bi = div_10*bi**5
    m7_bi = div_9*bi**6
    m8_bi = div_8*bi**7
    m9_bi = div_7*bi**8
    m10_bi = div_6*bi**9
    m11_bi = div_5*bi**10
    m12_bi = div_4*bi**11
    m13_bi = div_3*bi**12
    m14_bi = div_2*bi**13
    m15_bi = div_1*bi**14 

    #print(m1_bi, m2_bi, m3_bi, m4_bi, m5_bi, m6_bi, m7_bi, m8_bi, m9_bi, m10_bi, m11_bi, m12_bi, m13_bi, m14_bi)

    soma_mult = m1_bi + m2_bi + m3_bi + m4_bi + m5_bi + m6_bi + m7_bi + m8_bi + m9_bi + m10_bi + m11_bi + m12_bi + m13_bi + m14_bi + m15_bi + m15_bi       

    print("Base:",bi," -> Base: 10 =", soma_mult)

#Da base 10 pra base escolhida:

    b = (soma_mult)

    c1 = int(b/bf)
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
    c21 = int(c20/bf)
    c22 = int(c21/bf)
    c23 = int(c22/bf)
    c24 = int(c23/bf)
    c25 = int(c24/bf)
    c26 = int(c25/bf)
    c27 = int(c26/bf)
    c28 = int(c27/bf)
    c29 = int(c28/bf)
    c30 = int(c29/bf)

    r1 = int(b-(c1*bf))
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
    r21 = int(c20-(c21*bf))
    r22 = int(c21-(c22*bf))
    r23 = int(c22-(c23*bf))
    r24 = int(c23-(c24*bf))
    r25 = int(c24-(c25*bf))
    r26 = int(c25-(c26*bf))
    r27 = int(c26-(c27*bf))
    r28 = int(c27-(c28*bf))
    r29 = int(c28-(c29*bf))
    r30 = int(c29-(c30*bf))
    

    #if ( c20 and c19 and c18 and c17 and c16 and c15 and c14 and c13 and c12 and c11 and c10 and c9 and c8 and c7 and c6 and c5 and c4 and c3 and c2 and c1 != 0 ):
    print()
    print("Quociente:",c30,c29,c28,c27,c26,c25,c24,c23,c22,c21,c20,c19,c18,c17,c16,c15,c14,c13,c12,c11,c10,c9,c8,c7,c6,c5,c4,c3,c2,c1)
    print("Resultado:"  ,r30,r29,r28,r27,r26,r25,r24,r23,r22,r21,r20,r19,r18,r17,r16,r15,r14,r13,r12,r11,r10,r9,r8,r7,r6,r5,r4,r3,r2,r1)
    print()

if bf > 10:
    print("A=10 B=11 C=12 D=13 E=14 F=15")

input()