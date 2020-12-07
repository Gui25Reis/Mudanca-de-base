# Programa -> COnversão de bases (qualquer uma)   -   Gui Reis - Mack (31920918)
# 42 linhas

num_str = str(input('Número: ')).lower()
bi = int(input('Base inicial: '))
bf = int(input('Base final: '))

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

conversao = 0
base_decimal = len(num_str) - 1                         # Expoente da base inicial (que multiplica o número para conversão de base).

### Lógica do algorítmo:
# Na 1ª parte, faz a conversão de qualquer base para a base 10.
# Na 2ª parte, faz a conversão da base 10 para a desejada. 

# 1ª Parte:
for numero in range (len(num_str)):
    valor_letra = 10

    if bi > 10 and num_str[numero] in alfabeto:                     # Se o número for uma letra.
        for letra in range(26):
            if alfabeto[letra] == num_str[numero]:                  # Quando achar qual é a letra
                break
            else:
                valor_letra += 1                                    # A cada loop que passa, add +1 no valor da letra
        num_int = valor_letra                                       # Guarda na variável para usar na fórmula lá em baixo
    else:                                                           # Se não tiver nenhuma letra.        
        num_int = int(num_str[numero])                              # Muda de str para int, para fazer cálculo.

    conversao += num_int * (bi ** base_decimal)                     # Cáculo: vai somando os números q estão sendo multiplicados pelas bases.
    base_decimal -= 1                                               # Cada loop que passa muda a base


# 2ª Parte:
cont = 0                                
result = []                                                         # Lista para guardar os resultados (os restos)

if bf != 10:                                                        # O número ja está na base 10.
    while cont != 2:
        conta = conversao // bf                                     # Fica dividindo pelo quociente (pega o resultado (inteiro))
        conta = str(conta)
        result.append(conversao % bf)                               # Add na lista
        conversao = conversao // bf                                 # Substitui pelo quociente obtido.

        if conversao < bf:                                          # Condição para parar o loop
            cont += 1

    for ind_list in range ( len(result)-1, -1 , -1 ):               # Printar o resultado
        if result[ind_list] > 9:                                    # Se for o número for uma letra (10,11..)
            valor_letra = 10
            for ind_alf in range(26):
                if result[ind_list] == valor_letra:                 # Quando o número for o mesmo valor da letra
                    print(alfabeto[ind_alf].upper(), end = '')      # Printa a letra (maiúscula) correspondente ao valor .
                    break                                           # Para o loop pois já achou a letra
                else:
                    valor_letra += 1                                # A cada loop que passa, add +1 no valor da letra
        else:                                                       # Se não tiver letra, printa o número
            print(result[ind_list], end = '')
else:
    print(conversao)