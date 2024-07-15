# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 463)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 651, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.Model = QtWidgets.QWidget()
        self.Model.setObjectName("Model")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.Model)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -11, 651, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonGenerateNerdssInput = QtWidgets.QPushButton(parent=self.Model)
        self.pushButtonGenerateNerdssInput.setGeometry(QtCore.QRect(219, 350, 231, 25))
        self.pushButtonGenerateNerdssInput.setObjectName("pushButtonGenerateNerdssInput")
        self.splitter_2 = QtWidgets.QSplitter(parent=self.Model)
        self.splitter_2.setGeometry(QtCore.QRect(210, 50, 221, 25))
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButtonParse = QtWidgets.QPushButton(parent=self.splitter_2)
        self.pushButtonParse.setObjectName("pushButtonParse")
        self.pushButtonAdvance = QtWidgets.QPushButton(parent=self.splitter_2)
        self.pushButtonAdvance.setObjectName("pushButtonAdvance")
        self.openGLWidgetStructure = QtWidgets.QWidget(parent=self.Model)
        self.openGLWidgetStructure.setGeometry(QtCore.QRect(110, 100, 411, 241))
        self.openGLWidgetStructure.setObjectName("openGLWidgetStructure")
        self.splitter = QtWidgets.QSplitter(parent=self.Model)
        self.splitter.setGeometry(QtCore.QRect(110, 10, 411, 25))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lineEditFilePath = QtWidgets.QLineEdit(parent=self.splitter)
        self.lineEditFilePath.setObjectName("lineEditFilePath")
        self.pushButtonBrowseFile = QtWidgets.QPushButton(parent=self.splitter)
        self.pushButtonBrowseFile.setObjectName("pushButtonBrowseFile")
        self.tabWidget.addTab(self.Model, "")
        self.Simulation = QtWidgets.QWidget()
        self.Simulation.setObjectName("Simulation")
        self.pushButtonInstallNERDSS = QtWidgets.QPushButton(parent=self.Simulation)
        self.pushButtonInstallNERDSS.setGeometry(QtCore.QRect(120, 10, 401, 25))
        self.pushButtonInstallNERDSS.setObjectName("pushButtonInstallNERDSS")
        self.label = QtWidgets.QLabel(parent=self.Simulation)
        self.label.setGeometry(QtCore.QRect(20, 70, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.Simulation)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 111, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditNERDSSExe = QtWidgets.QLineEdit(parent=self.Simulation)
        self.lineEditNERDSSExe.setGeometry(QtCore.QRect(130, 60, 361, 31))
        self.lineEditNERDSSExe.setObjectName("lineEditNERDSSExe")
        self.lineEditInputsFolder = QtWidgets.QLineEdit(parent=self.Simulation)
        self.lineEditInputsFolder.setGeometry(QtCore.QRect(130, 100, 361, 31))
        self.lineEditInputsFolder.setObjectName("lineEditInputsFolder")
        self.pushButtonSelectNERDSS = QtWidgets.QPushButton(parent=self.Simulation)
        self.pushButtonSelectNERDSS.setGeometry(QtCore.QRect(500, 60, 131, 31))
        self.pushButtonSelectNERDSS.setObjectName("pushButtonSelectNERDSS")
        self.pushButtonSelectInputs = QtWidgets.QPushButton(parent=self.Simulation)
        self.pushButtonSelectInputs.setGeometry(QtCore.QRect(500, 100, 131, 31))
        self.pushButtonSelectInputs.setObjectName("pushButtonSelectInputs")
        self.commandLinkButtonRunSimulation = QtWidgets.QCommandLinkButton(parent=self.Simulation)
        self.commandLinkButtonRunSimulation.setGeometry(QtCore.QRect(240, 170, 161, 41))
        self.commandLinkButtonRunSimulation.setObjectName("commandLinkButtonRunSimulation")
        self.progressBar = QtWidgets.QProgressBar(parent=self.Simulation)
        self.progressBar.setGeometry(QtCore.QRect(117, 220, 401, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.Simulation)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 270, 341, 111))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.commandLinkButtonKillSimulation = QtWidgets.QCommandLinkButton(parent=self.Simulation)
        self.commandLinkButtonKillSimulation.setGeometry(QtCore.QRect(460, 170, 177, 41))
        self.commandLinkButtonKillSimulation.setObjectName("commandLinkButtonKillSimulation")
        self.tabWidget.addTab(self.Simulation, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButtonVisualizeTraj = QtWidgets.QPushButton(parent=self.tab)
        self.pushButtonVisualizeTraj.setGeometry(QtCore.QRect(180, 10, 241, 51))
        self.pushButtonVisualizeTraj.setObjectName("pushButtonVisualizeTraj")
        self.pushButtonPlotCopyNum = QtWidgets.QPushButton(parent=self.tab)
        self.pushButtonPlotCopyNum.setGeometry(QtCore.QRect(180, 90, 241, 51))
        self.pushButtonPlotCopyNum.setObjectName("pushButtonPlotCopyNum")
        self.pushButtonPlotComplex = QtWidgets.QPushButton(parent=self.tab)
        self.pushButtonPlotComplex.setGeometry(QtCore.QRect(180, 180, 241, 51))
        self.pushButtonPlotComplex.setObjectName("pushButtonPlotComplex")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NERDSS"))
        self.pushButtonGenerateNerdssInput.setText(_translate("MainWindow", "Save NERDSS inputs"))
        self.pushButtonParse.setText(_translate("MainWindow", "Parse"))
        self.pushButtonAdvance.setText(_translate("MainWindow", "Advanced"))
        self.pushButtonBrowseFile.setText(_translate("MainWindow", "Select file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Model), _translate("MainWindow", "Model"))
        self.pushButtonInstallNERDSS.setText(_translate("MainWindow", "Install NERDSS on your local machine"))
        self.label.setText(_translate("MainWindow", "nerdss exe:"))
        self.label_2.setText(_translate("MainWindow", "inputs folder:"))
        self.pushButtonSelectNERDSS.setText(_translate("MainWindow", "Select nerdss"))
        self.pushButtonSelectInputs.setText(_translate("MainWindow", "Select inputs"))
        self.commandLinkButtonRunSimulation.setText(_translate("MainWindow", "Run Simulation"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Press the \'Run Simulation\' button to initiate the simulation. The progress bar will refresh every 10 seconds to reflect the current status."))
        self.commandLinkButtonKillSimulation.setText(_translate("MainWindow", "Kill Simulation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Simulation), _translate("MainWindow", "Simulation"))
        self.pushButtonVisualizeTraj.setText(_translate("MainWindow", "Visualize Traj"))
        self.pushButtonPlotCopyNum.setText(_translate("MainWindow", "Plot Copy Number"))
        self.pushButtonPlotComplex.setText(_translate("MainWindow", "Plot Complex"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())