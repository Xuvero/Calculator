import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

class mainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        ###Input That You Make The Account###
        self.windowAccountInput()

        ###Label That Show The Answer###
        self.windowAnswerInput()

        ###Buttons With the Number To Type###
        self.windowNumberButtons()

        ###The Other Buttons Like Delete Everything or "C"###
        self.diferentCaracterButtons()

        ###Normal Accounts Buttons Like Times(x) or Plus(+)###
        self.normalAcountsButtons()

        ###Function That Load The Window###
        self.loadWindow()

    ########################################Frontend Part of The Application########################################
    def loadWindow (self):
        ###Window Configurations###
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle('Calculator')
        self.setGeometry(250, 55, 300, 450)
        self.setStyleSheet('background-color: #202020;')
        self.setMaximumSize(300, 450)
        self.setMinimumSize(300, 450)
        self.show()

    def windowAccountInput (self):
        ###Here You Make The Accounts###
        self.mainInput = QLineEdit(self)
        self.mainInput.move(5, 5)
        self.mainInput.resize(290, 115)
        self.mainInput.setStyleSheet('background-color: #202020; color: white; font-size: 40px;')
        self.mainInput.setAlignment(Qt.AlignRight)

    def windowAnswerInput (self):
        ###Show The Answers Label###
        self.answerInput = QLineEdit(self)
        self.answerInput.move(5, 125)
        self.answerInput.resize(290, 70)
        self.answerInput.setStyleSheet('background-color: #202020; color: white;')
        self.answerInput.setReadOnly(True)
        self.answerInput.setAlignment(Qt.AlignRight)

    def windowNumberButtons (self):
        ###Button Number Zero###
        self.zeroButton = QPushButton(self)
        self.zeroButton.setText('0')
        self.zeroButton.move(75, 400)
        self.zeroButton.resize(75, 50)
        self.zeroButton.setStyleSheet('background-color: #202020; color: white;')
        self.zeroButton.clicked.connect(self.writeTheNumberZero)

        ###Button Number One###
        self.oneButton = QPushButton(self)
        self.oneButton.setText('1')
        self.oneButton.move(0, 250)
        self.oneButton.resize(75, 50)
        self.oneButton.setStyleSheet('background-color: #202020; color: white;')
        self.oneButton.clicked.connect(self.writeTheNumberOne)

        ###Button Number Two###
        self.twoButton = QPushButton(self)
        self.twoButton.setText('2')
        self.twoButton.move(75, 250)
        self.twoButton.resize(75, 50)
        self.twoButton.setStyleSheet('background-color: #202020; color: white;')
        self.twoButton.clicked.connect(self.writeTheNumberTwo)

        ###Button Number Tree###
        self.treeButton = QPushButton(self)
        self.treeButton.setText('3')
        self.treeButton.move(150, 250)
        self.treeButton.resize(75, 50)
        self.treeButton.setStyleSheet('background-color: #202020; color: white;')
        self.treeButton.clicked.connect(self.writeTheNumberTree)

        ###Button Number Four###
        self.fourButton = QPushButton(self)
        self.fourButton.setText('4')
        self.fourButton.move(0, 300)
        self.fourButton.resize(75, 50)
        self.fourButton.setStyleSheet('background-color: #202020; color: white;')
        self.fourButton.clicked.connect(self.writeTheNumberFour)

        ###Button Number Five###
        self.fiveButton = QPushButton(self)
        self.fiveButton.setText('5')
        self.fiveButton.move(75, 300)
        self.fiveButton.resize(75, 50)
        self.fiveButton.setStyleSheet('background-color: #202020; color: white;')
        self.fiveButton.clicked.connect(self.writeTheNumberFive)

        ###Button Number Six###
        self.sixButton = QPushButton(self)
        self.sixButton.setText('6')
        self.sixButton.move(150, 300)
        self.sixButton.resize(75, 50)
        self.sixButton.setStyleSheet('background-color: #202020; color: white;')
        self.sixButton.clicked.connect(self.writeTheNumberSix)

        ###Button Number Seven###
        self.sevenButton = QPushButton(self)
        self.sevenButton.setText('7')
        self.sevenButton.move(0, 350)
        self.sevenButton.resize(75, 50)
        self.sevenButton.setStyleSheet('background-color: #202020; color: white;')
        self.sevenButton.clicked.connect(self.writeTheNumberSeven)

        ###Button Number Eight###
        self.eightButton = QPushButton(self)
        self.eightButton.setText('8')
        self.eightButton.move(75, 350)
        self.eightButton.resize(75, 50)
        self.eightButton.setStyleSheet('background-color: #202020; color: white;')
        self.eightButton.clicked.connect(self.writeTheNumberEight)

        ###Button Number Nine###
        self.nineButton = QPushButton(self)
        self.nineButton.setText('9')
        self.nineButton.move(150, 350)
        self.nineButton.resize(75, 50)
        self.nineButton.setStyleSheet('background-color: #202020; color: white;')
        self.nineButton.clicked.connect(self.writeTheNumberNine)

    def diferentCaracterButtons (self):
        ###Delete Button###
        self.deleteButton = QPushButton(self)
        self.deleteButton.setText('C')
        self.deleteButton.move(0, 200)
        self.deleteButton.resize(75, 50)
        self.deleteButton.setStyleSheet('background-color: #D90429; color: black;')
        self.deleteButton.clicked.connect(self.writeDelete)

        ###Percent Button###
        self.percentButton = QPushButton(self)
        self.percentButton.setText('%')
        self.percentButton.move(150, 200)
        self.percentButton.resize(75, 50)
        self.percentButton.setStyleSheet('background-color: #202020; color: #89fc00;')
        self.percentButton.clicked.connect(self.writePercent)

        ###Parentheses Button###
        self.parenthesesButton = QPushButton(self)
        self.parenthesesButton.setText('()')
        self.parenthesesButton.move(75, 200)
        self.parenthesesButton.resize(75, 50)
        self.parenthesesButton.setStyleSheet('background-color: #202020; color: #89fc00;')
        self.parenthesesButton.clicked.connect(self.writeParentheses)

        ###Comma Button###
        self.commaButton = QPushButton(self)
        self.commaButton.setText('.')
        self.commaButton.move(150, 400)
        self.commaButton.resize(75, 50)
        self.commaButton.setStyleSheet('background-color: #202020; color: white;')
        self.commaButton.clicked.connect(self.writeComma)

        ###Negative Button###
        self.negativeButton = QPushButton(self)
        self.negativeButton.setText('+/-')
        self.negativeButton.move(0, 400)
        self.negativeButton.resize(75, 50)
        self.negativeButton.setStyleSheet('background-color: #202020; color: white;')
        self.negativeButton.clicked.connect(self.writeNegative)

        ###Equal Button###
        self.equalButton = QPushButton(self)
        self.equalButton.setText('=')
        self.equalButton.move(225, 400)
        self.equalButton.resize(75, 50)
        self.equalButton.setStyleSheet('background-color: #89fc00; color: black;')
        self.equalButton.clicked.connect(self.writeEqualButton)

    def normalAcountsButtons (self):
        ###Division Button###
        self.divisionButton = QPushButton(self)
        self.divisionButton.setText('÷')
        self.divisionButton.move(225, 250)
        self.divisionButton.resize(75, 50)
        self.divisionButton.setStyleSheet('background-color: #202020; color: #89fc00;')
        self.divisionButton.clicked.connect(self.writeDivision)

        ###Minus Button###
        self.minusButton = QPushButton(self)
        self.minusButton.setText('-')
        self.minusButton.move(225, 350)
        self.minusButton.resize(75, 50)
        self.minusButton.setStyleSheet('background-color: #202020; color: #89fc00;')
        self.minusButton.clicked.connect(self.writeMinus)

        ###Times Button###
        self.timesButton = QPushButton(self)
        self.timesButton.setText('x')
        self.timesButton.move(225, 200)
        self.timesButton.resize(75, 50)
        self.timesButton.setStyleSheet('background-color: #202020; color: #89fc00;')
        self.timesButton.clicked.connect(self.writeTimes)

        ###Plus Button###
        self.plusButton = QPushButton(self)
        self.plusButton.setText('+')
        self.plusButton.move(225, 300)
        self.plusButton.resize(75, 50)
        self.plusButton.setStyleSheet('background-color: #202020; color: #89fc00;')
        self.plusButton.clicked.connect(self.writePlus)

    ########################################Backend of The Application########################################
    def writeTheNumberZero (self):
        ###Number Zero###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '0')

    def writeTheNumberOne (self):
        ###Number One###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '1')

    def writeTheNumberTwo (self):
        ###Number Two###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '2')

    def writeTheNumberTree (self):
        ###Number Tree###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '3')

    def writeTheNumberFour (self):
        ###Number Four###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '4')

    def writeTheNumberFive (self):
        ###Number Five###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '5')

    def writeTheNumberSix (self):
        ###Number Six###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '6')

    def writeTheNumberSeven (self):
        ##Number Seven###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '7')

    def writeTheNumberEight (self):
        ###Number Eight###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '8')

    def writeTheNumberNine (self):
        ###Number Nine###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '9')

    def writeComma (self):
        ###Comma###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '.')

    def writeNegative (self):
        ###Negative###
        self.text = self.mainInput.text()
        self.mainInput.setText('-' + self.text)

    def writePlus (self):
        ###Plus###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '+')

    def writeMinus (self):
        ###Minus###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '-')

    def writeParentheses (self):
        ###Plus###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '()')

    def writePercent (self):
        ###Minus###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '%')

    def writeTimes (self):
        ###Times###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '*')

    def writeDivision (self):
        ###Division###
        self.text = self.mainInput.text()
        self.mainInput.setText(self.text + '/')

    def writeDelete (self):
        ###Delete###
        self.text = self.mainInput.text()
        self.mainInput.setText('')
        self.answerInput.setText('')
    
    def writeEqualButton (self):
        ###Try to do equal if is not possible do the except###
        try:
            self.getAccount = self.mainInput.text() 
            self.ans = eval(self.getAccount) 
            self.answerInput.setText(str(self.ans))

        except:
            self.answerInput.setText('Incorrect Expression.')


application = QApplication(sys.argv)
loadMainWindow = mainWindow()
sys.exit = QMainWindow(application.exec_())
