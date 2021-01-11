######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS - All rights reserved

# -*- coding: utf-8 -*-


## Classe responsável pela criação da interface gráfica

## Bibliotecas necessárias:
# Arquivo local
import mudanca_base as md                               

# GUI
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QIcon


class Gui(QtWidgets.QMainWindow):
    ## Construtor: define a super classe e também a janela principal
    def __init__(self):                                 
        super(Gui, self).__init__()

        self.setWindowIcon(QIcon('images/icon.png'))                            # Define o ícone
        self.setWindowTitle(" ")                                                # Define o título (título vazio)
        self.setFixedSize(180, 270)                                             # Sempre vai ser esse tamanho
    
        self.gui_Ui()                                                           # Chama o método de construção da GUI

        self.res = ''                                                           # Atributo que guarda o texto mostrado ao usuário
        

    def gui_Ui(self):
        root = QtWidgets.QWidget(self)                                          # Área principal (root), onde tudo vai ser colocado dentro        
        root.setMaximumSize(QtCore.QSize(180, 270))                             # Define o tamanho máximo que ela chega
        self.setCentralWidget(root)                                             # Define como área central

    ## ------------------------------------------------------------------------------------------------
    ## Entrada do número:
        lb_Entrada = self.lbl("Número", 12, 10, 10, 151, 31, root)              # Cria a lbl com as coordenadas
        lb_Entrada.setAlignment(QtCore.Qt.AlignCenter)                          # Alinhamento: texto no centro

        self.ent_Entrada = QtWidgets.QTextEdit(root)                            # Cria a entrada de texto
        self.ent_Entrada.setGeometry(QtCore.QRect(10, 40, 161, 21))                 # Define a posição
        self.ent_Entrada.setMaximumSize(161, 21)                                    # Define o tamanho máximo da entrada
        self.ent_Entrada.setFont(QFont('Arial', 12))                                # Fonte
        self.ent_Entrada.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)   # Tira a barra de rolagem
        
    ## ------------------------------------------------------------------------------------------------
    ## Base inicial:
        lb_Inicial = self.lbl("Base inicial", 12, 10, 80, 91, 21, root)         # Cria a lbl com as coordenadas
        lb_Inicial.setAlignment(QtCore.Qt.AlignRight)                           # Alinhamento: texto na direita

        self.ent_Inicial = self.ent(12, 110, 80, 51, 21, root)                  # Cria a entrada de texto com as coordenadas

    ## ------------------------------------------------------------------------------------------------
    ## Base final:
        lb_Final = self.lbl("Base final", 12, 20, 110, 81, 21, root)            # Cria a lbl com as coordenadas
        lb_Final.setAlignment(QtCore.Qt.AlignRight)                             # Alinhamento: texto na direita

        self.ent_Final = self.ent(12, 110, 110, 51, 21, root)                   # Cria a entrada de texto com as coordenadas

    ## ------------------------------------------------------------------------------------------------
    ## Calcular:
        bt_Calcular = QtWidgets.QPushButton("Calcular", root)                   # Cria o botão
        bt_Calcular.setGeometry(QtCore.QRect(40, 150, 101, 23))                 # Define a posição
        bt_Calcular.clicked.connect(self.cal_pressed)                           # Add a ação dele

        self.lb_Resposta = QtWidgets.QTextBrowser(root)                         # Cria a saída de texto
        self.lb_Resposta.setGeometry(QtCore.QRect(10, 180, 161, 51))            # Define sua posição

    ## ------------------------------------------------------------------------------------------------
    ## Copyright:
        txt_Copyright = "COPYRIGHT © 2020 KINGS\nv1.1.0"                                # Texto copyright
        copyright_Txt = self.lbl(txt_Copyright, 7, 20, 235, 141, 31, root)      # Cria a lbl com as coordenadas
        copyright_Txt.setFont(QFont('Arial',7, QFont.Bold))                     # Fonte
        copyright_Txt.setAlignment(QtCore.Qt.AlignCenter)                       # Alinhamento: texto no centro


## ------------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------
### Funções gerais:

    # Cria todas as lbls
    def lbl(self, txt_, tam_, p1_, p2_, p3_, p4_, wid_):
        lb = QtWidgets.QLabel(txt_, wid_)                                       # Cria uma label
        lb.setGeometry(QtCore.QRect(p1_, p2_, p3_, p4_))                            # Define a posição
        lb.setFont(QFont('Arial', tam_))                                            # Define a fonte
        return lb                                                                   # Retorna a label

    # Cria as entradas numéricas
    def ent(self, tam_, p1_, p2_, p3_, p4_, wid_):
        ent = QtWidgets.QSpinBox(wid_)                                          # Cria uma entrada de números
        ent.setGeometry(QtCore.QRect(p1_, p2_, p3_, p4_))                           # Define a posição
        ent.setFont(QFont('Arial', tam_))                                           # Define a fonte
        ent.setMinimum(2)                                                           # Número mínimo
        ent.setMaximum(36)                                                          # Número máximo
        return ent                                                                  # Retorna a entrada

    # Caso aconteça algum erro esse método eh chamado
    def error(self):
        self.ent_Entrada.setStyleSheet(
                            "QTextEdit {background-color: rgb(255, 127, 127);}")    # Cor de fundo fica vermelho

        self.res = "Número inválido!\n\n" + self.res                                # Mensagem de número inválido
        
    # Pegar os dados de entrada
    def cal_pressed(self):
        num = self.ent_Entrada.toPlainText()                                        # Pega a entrada (número)
        bi = int(self.ent_Inicial.text())                                           # Base inicial
        bf = int(self.ent_Final.text())                                             # Base final
        mudan = md.Mudan_Base(num, bi, bf)                                          # Instancia um objeto da classe mudança de base
        if (mudan.is_possible()):                                                   # Verifica se eh possivel
            self.res = f"O número {num} [{bi} -> {bf}] = {mudan.result()}\n\n" + self.res           # Adiciona o resultado
            self.ent_Entrada.setStyleSheet("QTextEdit {background-color: rgb(255, 255, 255);}")     # Deixa o fundo branco
        else: self.error()                                                          # Se não for possível chama o erro

        self.ent_Inicial.setValue(2)                                                # Deixa os valores como padrão
        self.ent_Final.setValue(2)                                                  
        self.ent_Entrada.setText('')                                                
        self.lb_Resposta.setText(self.res)                                          # Mostra o resultado ao usuário

        del mudan                                                                   # Deleta o objeto instânciado