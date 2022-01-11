from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(472, 422)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 441, 281))
        self.listWidget.setObjectName("listWidget")
        self.Title = QtWidgets.QLineEdit(Form)
        self.Title.setGeometry(QtCore.QRect(30, 80, 151, 21))
        self.Title.setObjectName("Title")
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setGeometry(QtCore.QRect(230, 20, 131, 81))
        self.searchButton.setObjectName("searchButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(translate("Form", "Каталог библиотеки"))
        self.searchButton.setText(translate("Form", "Искать"))
        self.comboBox.setItemText(0, translate("Form", "Автор"))
        self.comboBox.setItemText(1, translate("Form", "Название"))