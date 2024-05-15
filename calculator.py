from PyQt6 import QtCore, QtGui, QtWidgets
from functools import partial
from re import split

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setEnabled(True)
        Calculator.setFixedWidth(211)
        Calculator.setFixedHeight(320) 
        Calculator.title = ('Calculator')     
        QtWidgets.QMainWindow.setWindowTitle(Calculator, "Calculator")

        self.btn_1 = QtWidgets.QPushButton(parent=Calculator)
        self.btn_1.setGeometry(QtCore.QRect(10, 110, 41, 41))
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(parent=Calculator)
        self.btn_2.setGeometry(QtCore.QRect(60, 110, 41, 41))
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(parent=Calculator)
        self.btn_3.setGeometry(QtCore.QRect(110, 110, 41, 41))
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(parent=Calculator)
        self.btn_4.setGeometry(QtCore.QRect(10, 160, 41, 41))
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(parent=Calculator)
        self.btn_5.setGeometry(QtCore.QRect(60, 160, 41, 41))
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(parent=Calculator)
        self.btn_6.setGeometry(QtCore.QRect(110, 160, 41, 41))
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(parent=Calculator)
        self.btn_7.setGeometry(QtCore.QRect(10, 210, 41, 41))
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(parent=Calculator)
        self.btn_8.setGeometry(QtCore.QRect(60, 210, 41, 41))
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(parent=Calculator)
        self.btn_9.setGeometry(QtCore.QRect(110, 210, 41, 41))
        self.btn_9.setObjectName("btn_9")
        self.btn_per = QtWidgets.QPushButton(parent=Calculator)
        self.btn_per.setGeometry(QtCore.QRect(10, 60, 41, 41))
        self.btn_per.setObjectName("btn_per")
        self.btn_multipl = QtWidgets.QPushButton(parent=Calculator)
        self.btn_multipl.setGeometry(QtCore.QRect(60, 60, 41, 41))
        self.btn_multipl.setObjectName("btn_multipl")
        self.btn_minus = QtWidgets.QPushButton(parent=Calculator)
        self.btn_minus.setGeometry(QtCore.QRect(110, 60, 41, 41))
        self.btn_minus.setObjectName("btn_minus")
        self.btn_plus = QtWidgets.QPushButton(parent=Calculator)
        self.btn_plus.setGeometry(QtCore.QRect(160, 60, 41, 41))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_clear = QtWidgets.QPushButton(parent=Calculator)
        self.btn_clear.setGeometry(QtCore.QRect(160, 110, 41, 41))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_result = QtWidgets.QPushButton(parent=Calculator)
        self.btn_result.setGeometry(QtCore.QRect(160, 160, 41, 91))
        self.btn_result.setObjectName("btn_result")
        self.btn_0 = QtWidgets.QPushButton(parent=Calculator)
        self.btn_0.setGeometry(QtCore.QRect(10, 260, 91, 41))
        self.btn_0.setObjectName("btn_0")
        self.btn_coma = QtWidgets.QPushButton(parent=Calculator)
        self.btn_coma.setGeometry(QtCore.QRect(110, 260, 41, 41))
        self.btn_coma.setObjectName("btn_coma")
        
        self.label = QtWidgets.QLabel(parent=Calculator)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.label.setStyleSheet("border:1px solid black\n")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignRight)
        self.label.setText("")
        self.label.setObjectName("label")

# fentieket a QT Designer generálta; módosítások benne általam:
# - fixáltam az ablakot, ne lehessen nagyítani/kicsinyíteni
# - a label alignmentjét állítottam vízszintesen jobbra és függőlegesen középre
# - két import született még, a PARTIAL és SPLIT függvények szükségessé váltak (googliztam, most találkoztam velük először)

# -------------------------- SAJÁT BLOKK KEZDETE --------------------------
        self.buttons = {self.btn_0 : '0',
                        self.btn_1 : '1',
                        self.btn_2 : '2',
                        self.btn_3 : '3',
                        self.btn_4 : '4',
                        self.btn_5 : '5',
                        self.btn_6 : '6',
                        self.btn_7 : '7',
                        self.btn_8 : '8',
                        self.btn_9 : '9',
                        self.btn_clear : '',
                        self.btn_coma : ',',
                        self.btn_per : '/',
                        self.btn_plus : '+',
                        self.btn_multipl : '*',
                        self.btn_result : '',
                        self.btn_minus : '-'}
        
        for key in self.buttons: # gombok stílusának /színének/ beállítása
            self.set_stylesheet(key)

        self.operators = ('/', '+', '*', '-', ',') # műveleti jelek (tizedesvesszővel)
        self.text_to_calculate = '' # a LABEL-en megjelenő string, amit az '=' gomb megnyomásával feldogoz a számológép

        for key in self.buttons: # szignál -> UPDATE_LABEL függvény, mint referencia, de argumentumnként megkapja a gombhoz tartozó karaktert is
            key.clicked.connect(partial(self.update_label, key))

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def set_stylesheet(self, item): # gomb stílus metódus
        item.setStyleSheet("QPushButton { background-color: LightGray; border-style:solid }"
                           "QPushButton:pressed { background-color: gray; border-style:solid }")

    def update_label(self, btn): # LABEL string update metódus
        # ha még nincs karakter a kijelzőn, akkor csak '-' gomb vagy szám nyomható
        if self.text_to_calculate == '' and (btn == self.btn_minus or self.buttons[btn].isnumeric()): 
            self.text_to_calculate += self.buttons[btn]
        
        # ha már van karakter a kijelzőn: 1) két műveleti jel, tizedesvessző nem nyomható egymás után; 2) egy számban csak egy tizedesvessző lehet
        elif self.text_to_calculate != '' and \
            not (self.buttons[btn] in self.operators and self.text_to_calculate[-1] in self.operators) and \
            not (btn == self.btn_coma and self.number_with_coma(self.text_to_calculate)):
            self.text_to_calculate += self.buttons[btn]

        # CLEAR gomb
        if btn == self.btn_clear:
            self.text_to_calculate = ''
        
        self.label.setText(self.text_to_calculate)
        
        # '=' gomb kezelése és a CALCULATE függvény meghívása (akkor nyomható, ha van valami a kijelzőn és nem műveleti jel az utolsó karakter)
        if btn == self.btn_result and self.text_to_calculate != '' and self.text_to_calculate[-1] not in self.operators:
            result = self.calculate(self.text_to_calculate)
            self.label.setText(result)
            self.text_to_calculate=''

    @staticmethod
    def number_with_coma(text_to_calculate): # TRUE, ha az utolsó felvitt szám tartalmaz már tizedesvesszőt
        text_separated = split(r'([/*+-])', text_to_calculate)
        if ',' in text_separated[-1]:
            return True
        return False

    @staticmethod
    def calculate(text_to_calculate): # kalkulátor; argumentum: a kijelzőn szerepő string
        if '/0' in text_to_calculate:
            return 'Error: divison with zero!'
        
        text_to_calculate = text_to_calculate.replace(',', '.') # tizedesvessző cseréje pontra
        text_separated = split(r'([/*+-])', text_to_calculate) # string split
        if text_to_calculate[0] == '-': # ha minusszal kezdődik a split-elendő string, akkor a lista 0. indexén egy üres string szerepel (?); itt törlöm
            text_separated.pop(0)

        for idx, item in enumerate(text_separated): # a kivonás műveletnél a kivonandó szám (jelenleg még string) negatív előjelet kap
            if item == '-':
                text_separated[idx+1] = '-' + text_separated[idx+1]

        while '-' in text_separated: # '-' karakter eltávolítása a listából
            text_separated.remove('-')
        while '+' in text_separated: # '+' karakter eltávolítása a listából
            text_separated.remove('+')

        for idx, item in enumerate(text_separated): # float-tá alakít minden elemet kivéve a '/' és '*' műveleti jeleket (a számokat, negatív számokat, tizedes számokat)
            if item.isnumeric() or ('.' in item) or ('-' in item):
                text_separated[idx] = float(item)

        # szorzás és osztás elvégzése sorrendben (a for ciklus minden művelet után újra indul, mert a POP függvény zavarja az iterálást)
        while ('*' in text_separated) or ('/' in text_separated): 
            for idx, item in enumerate(text_separated):
                if type(item) == str and (item == '*' or item =='/'):
                    if item == '*':
                        value = text_separated[idx-1] * text_separated[idx+1]
                        # a két tényezőt és a műveleti jelet lecseréli a szorzás eredményével
                        text_separated[(idx-1)] = value
                        text_separated.pop(idx)
                        text_separated.pop(idx)
                        break
                    elif item == '/':
                        value = text_separated[idx-1] / text_separated[idx+1]
                        text_separated[(idx-1)] = value
                        text_separated.pop(idx)
                        text_separated.pop(idx)
                        break

        result = 0
        for item in text_separated: # a végére már csak float objektumok maradtak a listában, amit már csak össze kell adni
            result += item

        return str(result)
# -------------------------- SAJÁT BLOKK VÉGE --------------------------

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.btn_1.setText(_translate("Calculator", "1"))
        self.btn_2.setText(_translate("Calculator", "2"))
        self.btn_3.setText(_translate("Calculator", "3"))
        self.btn_4.setText(_translate("Calculator", "4"))
        self.btn_5.setText(_translate("Calculator", "5"))
        self.btn_6.setText(_translate("Calculator", "6"))
        self.btn_7.setText(_translate("Calculator", "7"))
        self.btn_8.setText(_translate("Calculator", "8"))
        self.btn_9.setText(_translate("Calculator", "9"))
        self.btn_per.setText(_translate("Calculator", "/"))
        self.btn_multipl.setText(_translate("Calculator", "*"))
        self.btn_minus.setText(_translate("Calculator", "-"))
        self.btn_plus.setText(_translate("Calculator", "+"))
        self.btn_clear.setText(_translate("Calculator", "Clear"))
        self.btn_result.setText(_translate("Calculator", "="))
        self.btn_0.setText(_translate("Calculator", "0"))
        self.btn_coma.setText(_translate("Calculator", ","))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QWidget()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec())
