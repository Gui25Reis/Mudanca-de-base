# Programa -> Conversão de bases (qualquer uma)   -   Gui Reis - Mack (31920918)
# 19 linhas

alfabeto = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

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
    if result[ind] > 9:                                      # Se for o número for uma letra (10,11..)
        valor_letra = 10
        for ind_alf in range(26):
            if result[ind] == valor_letra:                   # Quando o número for o mesmo valor da letra
                print(alfabeto[ind_alf].upper(), end = '')   # Printa a letra (maiúscula) correspondente ao valor .
                break                                        # Para o loop pois já achou a letra
            valor_letra += 1                                 # A cada loop que passa, add +1 no valor da letra
    else:                                                    # Se não tiver letra, printa o número
        print(result[ind], end = '')




# Funções prontas de conversão:

# Bin() ->  Muda o número para base 2
#   -> bin(3)           - print: 0o11
#   -> f'{10:b}'        - print: 11
#   -> format(10, 'b')  - print: 11

# Oct() ->  Muda o número para base 8
#   -> oct(255)         - print: 0o12
#   -> '%o' % 10        - print: 12 
#   -> f'{10:o}'        - print: 12
#   -> format(10, 'o')  - print: 12

# Hex() ->  Muda o número para base 16
#   -> hex(255)         - print: 0xff
#   -> '%x' % 255       - print: ff 
#   -> '%X' % 255       - print: FF 
#   -> f'{10:x}'        - print: ff
#   -> format(10, 'x')  - print: ff