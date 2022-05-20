import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class mainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        ###Input That You Make The Account And Show The Answer###
        self.windowAccountInput()

        ###Buttons With the Number To Type###
        self.windowNumberButtons()

        ###The Other Buttons Like Delete Everything or "C"###
        self.diferentCaracterButtons()

        ###Normal Accounts Buttons Like Times(x) or Plus(+)###
        self.normalAcountsButtons()

        ###Function That Load The Window###
        self.loadWindow()

    #######################################Frontend Part of The Application#######################################
    def loadWindow (self):
        ###Window Configurations###
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Calculator')
        self.setGeometry(250, 55, 290, 445)
        self.setStyleSheet('background-color: #151515;')
        self.setMaximumSize(290, 445)
        self.setMinimumSize(290, 445)
        self.show()

    def windowAccountInput (self):
        ###Here You Make The Accounts###
        self.mainInput = QLineEdit(self)
        self.mainInput.move(10, 10)
        self.mainInput.resize(270, 70)
        self.mainInput.setStyleSheet(
            '''
                QLineEdit{
                    border: none;
                    background-color: #151515;
                    color: white;
                    font-size: 25px;
                }
            '''
        )
        self.mainInput.setAlignment(Qt.AlignRight)

    def windowNumberButtons (self):
        ###Button Number Zero###
        self.zeroButton = QPushButton(self)
        self.zeroButton.setText('0')
        self.zeroButton.move(10, 375)
        self.zeroButton.resize(130, 60)
        self.zeroButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.zeroButton.clicked.connect(self.writeTheNumberZero)

        ###Button Number One###
        self.oneButton = QPushButton(self)
        self.oneButton.setText('1')
        self.oneButton.move(10, 165)
        self.oneButton.resize(60, 60)
        self.oneButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.oneButton.clicked.connect(self.writeTheNumberOne)

        ###Button Number Two###
        self.twoButton = QPushButton(self)
        self.twoButton.setText('2')
        self.twoButton.move(80, 165)
        self.twoButton.resize(60, 60)
        self.twoButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.twoButton.clicked.connect(self.writeTheNumberTwo)

        ###Button Number Tree###
        self.treeButton = QPushButton(self)
        self.treeButton.setText('3')
        self.treeButton.move(150, 165)
        self.treeButton.resize(60, 60)
        self.treeButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.treeButton.clicked.connect(self.writeTheNumberTree)

        ###Button Number Four###
        self.fourButton = QPushButton(self)
        self.fourButton.setText('4')
        self.fourButton.move(10, 235)
        self.fourButton.resize(60, 60)
        self.fourButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.fourButton.clicked.connect(self.writeTheNumberFour)

        ###Button Number Five###
        self.fiveButton = QPushButton(self)
        self.fiveButton.setText('5')
        self.fiveButton.move(80, 235)
        self.fiveButton.resize(60, 60)
        self.fiveButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.fiveButton.clicked.connect(self.writeTheNumberFive)

        ###Button Number Six###
        self.sixButton = QPushButton(self)
        self.sixButton.setText('6')
        self.sixButton.move(150, 235)
        self.sixButton.resize(60, 60)
        self.sixButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.sixButton.clicked.connect(self.writeTheNumberSix)

        ###Button Number Seven###
        self.sevenButton = QPushButton(self)
        self.sevenButton.setText('7')
        self.sevenButton.move(10, 305)
        self.sevenButton.resize(60, 60)
        self.sevenButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.sevenButton.clicked.connect(self.writeTheNumberSeven)

        ###Button Number Eight###
        self.eightButton = QPushButton(self)
        self.eightButton.setText('8')
        self.eightButton.move(80, 305)
        self.eightButton.resize(60, 60)
        self.eightButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.eightButton.clicked.connect(self.writeTheNumberEight)

        ###Button Number Nine###
        self.nineButton = QPushButton(self)
        self.nineButton.setText('9')
        self.nineButton.move(150, 305)
        self.nineButton.resize(60, 60)
        self.nineButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.nineButton.clicked.connect(self.writeTheNumberNine)

    def diferentCaracterButtons (self):
        ###Delete Button###
        self.deleteButton = QPushButton(self)
        self.deleteButton.setText('C')
        self.deleteButton.move(10, 95)
        self.deleteButton.resize(60, 60)
        self.deleteButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #D90429;
                    color: black;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #f20429;
                }

                QPushButton:pressed{
                    background-color: #A80429;
                }
            '''
            )
        self.deleteButton.clicked.connect(self.writeDelete)

        ###Parentheses Button###
        self.parenthesesButton = QPushButton(self)
        self.parenthesesButton.setText('()')
        self.parenthesesButton.move(80, 95)
        self.parenthesesButton.resize(60, 60)
        self.parenthesesButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: #89fc00;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.parenthesesButton.clicked.connect(self.writeParentheses)

        ###Percent Button###
        self.percentButton = QPushButton(self)
        self.percentButton.setText('%')
        self.percentButton.move(150, 95)
        self.percentButton.resize(60, 60)
        self.percentButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: #89fc00;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.percentButton.clicked.connect(self.writePercent)

        ###Comma Button###
        self.commaButton = QPushButton(self)
        self.commaButton.setText('.')
        self.commaButton.move(150, 375)
        self.commaButton.resize(60, 60)
        self.commaButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: white;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
            )
        self.commaButton.clicked.connect(self.writeComma)

        ###Equal Button###
        self.equalButton = QPushButton(self)
        self.equalButton.setText('=')
        self.equalButton.move(220, 375)
        self.equalButton.resize(60, 60)
        self.equalButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #89fc00;
                    color: black;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #9ffc1f;
                }

                QPushButton:pressed{
                    background-color: #8ddd00;
                }
            '''
            )
        self.equalButton.clicked.connect(self.writeEqualButton)
        
        shotcut = QShortcut(QKeySequence(Qt.Key_Return), self)
        shotcut.activated.connect(self.writeEqualButton)

    def normalAcountsButtons (self):
        ###Division Button###
        self.divisionButton = QPushButton(self)
        self.divisionButton.setText('÷')
        self.divisionButton.move(220, 165)
        self.divisionButton.resize(60, 60)
        self.divisionButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: #89fc00;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.divisionButton.clicked.connect(self.writeDivision)

        ###Minus Button###
        self.minusButton = QPushButton(self)
        self.minusButton.setText('-')
        self.minusButton.move(220, 235)
        self.minusButton.resize(60, 60)
        self.minusButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: #89fc00;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.minusButton.clicked.connect(self.writeMinus)

        ###Times Button###
        self.timesButton = QPushButton(self)
        self.timesButton.setText('x')
        self.timesButton.move(220, 95)
        self.timesButton.resize(60, 60)
        self.timesButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: #89fc00;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
        self.timesButton.clicked.connect(self.writeTimes)

        ###Plus Button###
        self.plusButton = QPushButton(self)
        self.plusButton.setText('+')
        self.plusButton.move(220, 305)
        self.plusButton.resize(60, 60)
        self.plusButton.setStyleSheet(
            '''
                QPushButton{
                    background-color: #202020;
                    color: #89fc00;
                    border-radius: 15px;
                }

                QPushButton:hover{
                    background-color: #252525;
                }

                QPushButton:pressed{
                    background-color: #151515;
                }
            '''
        )
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
    
    def writeEqualButton (self):
        ###Try to do equal if is not possible do the except###
        try:
            self.getAccount = self.mainInput.text() 
            self.ans = eval(self.getAccount) 
            self.mainInput.setText(str(self.ans))

        except:
            self.mainInput.setText('Incorrect Expression.')


application = QApplication(sys.argv)
loadMainWindow = mainWindow()
sys.exit = QMainWindow(application.exec())
