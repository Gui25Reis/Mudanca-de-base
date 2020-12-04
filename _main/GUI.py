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

        self.setWindowIcon(QIcon('images/icon.png'))                                # Define o ícone
        self.setWindowTitle(" ")                                                    # Define o título (título vazio)
        self.setFixedSize(180, 290)                                                 # Sempre vai ser esse tamanho
    
        self.gui_Ui()                                                               # Chama o método de construção da GUI

        self.res = ''                                                               # Atributo que guarda o texto mostrado ao usuário
        

    def gui_Ui(self):
        self.root = QtWidgets.QWidget(self)                                         # Área principal (root), onde tudo vai ser colocado dentro        
        self.root.setMaximumSize(QtCore.QSize(180, 290))                            # Define o tamanho máximo que ela chega
        self.setCentralWidget(self.root)                                            # Define como área central

    ## ------------------------------------------------------------------------------------------------
    ## Entrada do número:
        self.lb_Entrada = self.lbl("Número", 12, 10, 10, 151, 31)                   # Cria a lbl com as coordenadas
        self.lb_Entrada.setAlignment(QtCore.Qt.AlignCenter)                         # Alinhamento: texto no centro

        self.ent_Entrada = QtWidgets.QTextEdit(self.root)                           # Cria a entrada de texto
        self.ent_Entrada.setGeometry(QtCore.QRect(10, 40, 161, 21))                 # Define a posição
        self.ent_Entrada.setMaximumSize(161, 21)                                    # Define o tamanho máximo da entrada
        self.ent_Entrada.setFont(QFont('Arial', 12))                                # Fonte
        self.ent_Entrada.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)   # Tira a barra de rolagem
        
    ## ------------------------------------------------------------------------------------------------
    ## Base inicial:
        self.lb_Inicial = self.lbl("Base inicial", 12, 10, 80, 91, 21)              # Cria a lbl com as coordenadas
        self.lb_Inicial.setAlignment(QtCore.Qt.AlignRight)                          # Alinhamento: texto na direita

        self.ent_Inicial = self.ent(12, 110, 80, 51, 21)                            # Cria a entrada de texto com as coordenadas

    ## ------------------------------------------------------------------------------------------------
    ## Base final:
        self.lb_Final = self.lbl("Base final", 12, 20, 110, 81, 21)                 # Cria a lbl com as coordenadas
        self.lb_Final.setAlignment(QtCore.Qt.AlignRight)                            # Alinhamento: texto na direita

        self.ent_Final = self.ent(12, 110, 110, 51, 21)                             # Cria a entrada de texto com as coordenadas

    ## ------------------------------------------------------------------------------------------------
    ## Calcular:
        self.bt_Calcular = QtWidgets.QPushButton("Calcular", self.root)             # Cria o botão
        self.bt_Calcular.setGeometry(QtCore.QRect(40, 150, 101, 23))                # Define a posição
        self.bt_Calcular.clicked.connect(self.cal_pressed)                          # Add a ação dele

        self.lb_Resposta = QtWidgets.QTextBrowser(self.root)                        # Cria a saída de texto
        self.lb_Resposta.setGeometry(QtCore.QRect(10, 180, 161, 51))                # Define sua posição

    ## ------------------------------------------------------------------------------------------------
    ## Copyright:
        self.txt_Copyright = "COPYRIGHT © 2020 KINGS\nAll rights reserved"          # Texto copyright
        self.copyright_Txt = self.lbl(self.txt_Copyright, 7, 20, 240, 141, 31)      # Cria a lbl com as coordenadas
        self.copyright_Txt.setFont(QFont('Arial',7, QFont.Bold))                    # Fonte
        self.copyright_Txt.setAlignment(QtCore.Qt.AlignCenter)                      # Alinhamento: texto no centro


## ------------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------
### Funções gerais:

    # Cria todas as lbls
    def lbl(self, txt_, tam_, p1_, p2_, p3_, p4_):
        lb = QtWidgets.QLabel(txt_, self.root)                                      # Cria uma label
        lb.setGeometry(QtCore.QRect(p1_, p2_, p3_, p4_))                            # Define a posição
        lb.setFont(QFont('Arial', tam_))                                            # Define a fonte
        return lb                                                                   # Retorna a label

    # Cria as entradas numéricas
    def ent(self, tam_, p1_, p2_, p3_, p4_):
        ent = QtWidgets.QSpinBox(self.root)                                         # Cria uma entrada de números
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
        self.num = self.ent_Entrada.toPlainText()                                   # Pega a entrada (número)

        bi = int(self.ent_Inicial.text())                                           # Base inicial
        bf = int(self.ent_Final.text())                                             # Base final
        mudan = md.Mudan_Base(self.num, bi, bf)                                     # Chama a classe de mudança de base
        if (mudan.is_possible()):                                                   # Verifica se eh possivel
            self.res = f"O número {self.num} [{bi} -> {bf}] = {mudan.result()}\n\n" + self.res      # Adiciona o resultado
            self.ent_Entrada.setStyleSheet("QTextEdit {background-color: rgb(255, 255, 255);}")     # Deixa o fundo branco
        else: self.error()                                                          # Se não for possível chama o erro

        self.ent_Entrada.setText('')                                                # Deixa a entrada vazia
        self.lb_Resposta.setText(self.res)                                          # Mostra o resultado ao usuário