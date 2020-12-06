######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS - All rights reserved


## Classe responsável por fazer a mudança de bases!

class Mudan_Base:
    ## Construtor: define os atributos (chamada por parâmetro)
    def __init__(self, num_:str, bi_:int, bf_:int):
        self.num_str = num_.lower()                         # Número a ser convertido
        self.bi = bi_                                       # Base Inicial
        self.bf = bf_                                       # Base Final

    ## Método que tranforma em decimal
    def to_decimal(self):                                   # 1ª Parte: conversão de qualquer base para decimal
        return int(self.num_str, base = self.bi)            # Retorna a mudança

    ## Método que tranforma de decimal pra base final
    def to_baseFinal(self):                                 # 2ª Parte: conversão de decimal para a base desejada                         
        num_dec = self.to_decimal()
        self.res = []                                       # Lista para guardar os resultados (os restos)
        while num_dec != 0:
            self.res.append(num_dec % self.bf)              # Add na lista
            num_dec = num_dec // self.bf                    # Substitui pelo quociente obtido.
    
    ## Verifica se o número pertence a base inicial
    def is_possible(self):
        try:                                                # Try: tenta converter o número pra decimal
            self.to_decimal()                               
            return True                                     # True: todos os números são da base inicial
        except: return False                                # False: Se tiver algum número que não seja da base inicial

    ## Cria o resultado
    def result(self):
        if self.bf == 10 :                                  # Se a base final for 10
            return self.to_decimal()                        # Retorna apenas a 1ª parte (n eh necessário continuar)

        self.to_baseFinal()                                 # Se não faz a 2ª parte
        res_str = ''                                        # String para armazenar o resultado
        for ind in range (len(self.res)-1, -1 , -1):        # Loop: pega os números convertidos de trás pra frente
            if self.res[ind] > 9:                           # Se for o número for uma letra (10,11..)
                res_str += chr(55+self.res[ind]).upper()    # Acha a letra correspondente
            else:                                           # Se não tiver letra
                res_str += str(self.res[ind])               # Apenas add o próprio número
        return res_str                                      # Retorna o resultado