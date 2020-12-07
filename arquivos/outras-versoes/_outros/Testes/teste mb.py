bi = int(input("Base inicial: ", ))
bf = int(input("Base final: ", ))

num = int(input('Digite o número: ', ))

div_1 = int(num/(10**11))
res_1 = int(num%(10**11))

div_2 = int(res_1/(10**10))
res_2 = int(res_1%(10**10))

div_3 = int(res_2/(10**9))
res_3 = int(res_2%(10**9))

div_4 = int(res_3/(10**8))
res_4 = int(res_3%(10**8))

div_5 = int(res_4/(10**9))
res_5 = int(res_4%(10**9))

div_6 = int(res_5/(10**8))
res_6 = int(res_5%(10**8))

div_7 = int(res_6/(10**7))
res_7 = int(res_6%(10**7))

div_8 = int(res_7/(10**6))
res_8 = int(res_7%(10**6))

div_9 = int(res_8/(10**5))
res_9 = int(res_8%(10**5))

div_10 = int(res_9/(10**4))
res_10 = int(res_9%(10**4))

div_11 = int(res_10/(10**3))
res_11 = int(res_10%(10**3))

div_12 = int(res_11/(10**2))
res_12 = int(res_11%(10**2))

div_13 = int(res_12/10)
res_13 = int(res_12%10)

div_14 = int(res_13/1)
res_14 = int(res_13%1)



m1_bi = div_14*1
m2_bi = div_13*bi
m3_bi = div_12*bi**2
m4_bi = div_11*bi**3
m5_bi = div_10*bi**4
m6_bi = div_9*bi**5
m7_bi = div_8*bi**6
m8_bi = div_7*bi**7
m9_bi = div_6*bi**8
m10_bi = div_5*bi**9
m11_bi = div_4*bi**10
m12_bi = div_3*bi**11
m13_bi = div_2*bi**12
m14_bi = div_1*bi**13 

#print(m1_bi, m2_bi, m3_bi, m4_bi, m5_bi, m6_bi, m7_bi, m8_bi, m9_bi, m10_bi, m11_bi, m12_bi, m13_bi, m14_bi)

soma_mult = m1_bi + m2_bi + m3_bi + m4_bi + m5_bi + m6_bi + m7_bi + m8_bi + m9_bi + m10_bi + m11_bi + m12_bi + m13_bi + m14_bi        

print("Base:",bi," -> Base: 10 =", soma_mult)
















