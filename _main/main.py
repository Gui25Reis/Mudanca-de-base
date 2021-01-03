######    Gui Reis   -   guisreis25@gmail.com    ######    COPYRIGHT © 2020 KINGS - All rights reserved

## Arquivo main

## Bibliotecas:
# Sistema:
import sys

# Arquivo local
from GUI import *

# GUI:
from PyQt5.QtWidgets import QApplication
   
# main:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Gui()

    win.show()
    sys.exit(app.exec_())