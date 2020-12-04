# Programa -> Conversão de bases (qualquer uma)   -   Gui Reis - Mack (31920918)
# 10 linhas

while True:
    num_str = str(input('Número: ')).lower()
    bi = int(input('Base inicial: '))
    bf = int(input('Base final: '))

    # 1ª Parte: conversão de qualquer base para decimal
    num_dec = int(num_str, base= bi)                             # Coloca o número (str) e a base que ele está que já tranforma em decimal

    # 2ª Parte: conversão de decimal para a base desejada                         
    result = []                                                  # Lista para guardar os resultados (os restos)

    while num_dec != 0:
        result.append(num_dec % bf)                              # Add na lista
        num_dec = num_dec // bf                                  # Substitui pelo quociente obtido.

    for ind in range ( len(result)-1, -1 , -1 ):                 # Printar o resultado
        print(chr(55+result[ind]).upper() if result[ind] > 9 else result[ind], end = '')
    print("\n\n")