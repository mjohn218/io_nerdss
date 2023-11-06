# Form implementation generated from reading ui file 'advanced_options_parse_pdb.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogParseParam(object):
    def setupUi(self, DialogParseParam):
        DialogParseParam.setObjectName("DialogParseParam")
        DialogParseParam.resize(640, 480)
        self.pushButtonApply = QtWidgets.QPushButton(parent=DialogParseParam)
        self.pushButtonApply.setGeometry(QtCore.QRect(230, 290, 80, 25))
        self.pushButtonApply.setObjectName("pushButtonApply")
        self.pushButtonCancel = QtWidgets.QPushButton(parent=DialogParseParam)
        self.pushButtonCancel.setGeometry(QtCore.QRect(330, 290, 80, 25))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.layoutWidget = QtWidgets.QWidget(parent=DialogParseParam)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 80, 173, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.layoutWidget1 = QtWidgets.QWidget(parent=DialogParseParam)
        self.layoutWidget1.setGeometry(QtCore.QRect(340, 80, 110, 171))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditCutoff = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.lineEditCutoff.setObjectName("lineEditCutoff")
        self.verticalLayout_2.addWidget(self.lineEditCutoff)
        self.lineEditThreshold = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.lineEditThreshold.setObjectName("lineEditThreshold")
        self.verticalLayout_2.addWidget(self.lineEditThreshold)
        self.lineEditStretch = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.lineEditStretch.setObjectName("lineEditStretch")
        self.verticalLayout_2.addWidget(self.lineEditStretch)

        self.retranslateUi(DialogParseParam)
        QtCore.QMetaObject.connectSlotsByName(DialogParseParam)

    def retranslateUi(self, DialogParseParam):
        _translate = QtCore.QCoreApplication.translate
        DialogParseParam.setWindowTitle(_translate("DialogParseParam", "Parse PDB parameters"))
        self.pushButtonApply.setText(_translate("DialogParseParam", "Apply"))
        self.pushButtonCancel.setText(_translate("DialogParseParam", "Cancel"))
        self.label.setText(_translate("DialogParseParam", "Cutoff distance (Å)"))
        self.label_2.setText(_translate("DialogParseParam", "Residue count threshold"))
        self.label_3.setText(_translate("DialogParseParam", "Stretch factor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogParseParam = QtWidgets.QDialog()
    ui = Ui_DialogParseParam()
    ui.setupUi(DialogParseParam)
    DialogParseParam.show()
    sys.exit(app.exec())
