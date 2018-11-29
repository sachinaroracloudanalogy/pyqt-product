# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_collection/models_addNew.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class ModelAddNewWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ModelAddNewWindow, self).__init__(parent)
        self.setWindowTitle("Financial Product Analysis Tool - Model:Add new")
        self.ui = Ui_MainWindow(self)


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 572)
        self.temp_window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 67, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 251, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 40, 51, 17))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(480, 40, 141, 25))
        self.comboBox.setObjectName("comboBox")
        self.groupBox_timeseries = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_timeseries.setGeometry(QtCore.QRect(20, 70, 351, 131))
        self.groupBox_timeseries.setObjectName("groupBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_timeseries)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 20, 351, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_timeseries)
        self.listWidget.setGeometry(QtCore.QRect(-5, 50, 351, 81))
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        self.groupBox_model_parameters = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_model_parameters.setGeometry(QtCore.QRect(390, 70, 231, 131))
        self.groupBox_model_parameters.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_model_parameters)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 71, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_model_parameters)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_model_parameters)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 71, 17))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_model_parameters)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 30, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_model_parameters)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 60, 113, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_model_parameters)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 90, 113, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.btn_evaluate_model = QtWidgets.QPushButton(self.centralwidget)
        self.btn_evaluate_model.setGeometry(QtCore.QRect(20, 210, 291, 25))
        self.btn_evaluate_model.setObjectName("pushButton")
        self.btn_recommend_model = QtWidgets.QPushButton(self.centralwidget)
        self.btn_recommend_model.setGeometry(QtCore.QRect(330, 210, 291, 25))
        self.btn_recommend_model.setObjectName("pushButton_2")
        self.groupBox_modelEvaluation = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_modelEvaluation.setGeometry(QtCore.QRect(20, 240, 601, 151))
        self.groupBox_modelEvaluation.setObjectName("groupBox_3")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_17.setGeometry(QtCore.QRect(360, 60, 71, 25))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_15.setGeometry(QtCore.QRect(360, 90, 71, 25))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_7.setGeometry(QtCore.QRect(60, 60, 71, 25))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_19.setGeometry(QtCore.QRect(510, 90, 71, 25))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_21.setGeometry(QtCore.QRect(510, 60, 71, 25))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_14.setGeometry(QtCore.QRect(360, 30, 71, 25))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_20.setGeometry(QtCore.QRect(510, 120, 71, 25))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_13.setGeometry(QtCore.QRect(210, 60, 71, 25))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_6.setGeometry(QtCore.QRect(60, 30, 71, 25))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_18.setGeometry(QtCore.QRect(510, 30, 71, 25))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_10 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 41, 17))
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_8.setGeometry(QtCore.QRect(60, 90, 71, 25))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_13 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_13.setGeometry(QtCore.QRect(170, 120, 41, 17))
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_9.setGeometry(QtCore.QRect(60, 120, 71, 25))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_9.setGeometry(QtCore.QRect(20, 90, 41, 17))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_14.setGeometry(QtCore.QRect(170, 90, 41, 17))
        self.label_14.setObjectName("label_14")
        self.label_11 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_11.setGeometry(QtCore.QRect(170, 60, 41, 17))
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 41, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 41, 17))
        self.label_8.setObjectName("label_8")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_11.setGeometry(QtCore.QRect(210, 90, 71, 25))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_10.setGeometry(QtCore.QRect(210, 30, 71, 25))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_16.setGeometry(QtCore.QRect(360, 120, 71, 25))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_modelEvaluation)
        self.lineEdit_12.setGeometry(QtCore.QRect(210, 120, 71, 25))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_12 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_12.setGeometry(QtCore.QRect(170, 30, 41, 17))
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_15.setGeometry(QtCore.QRect(310, 60, 41, 17))
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_17.setGeometry(QtCore.QRect(310, 120, 41, 17))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_18.setGeometry(QtCore.QRect(310, 90, 41, 17))
        self.label_18.setObjectName("label_18")
        self.label_16 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_16.setGeometry(QtCore.QRect(310, 30, 41, 17))
        self.label_16.setObjectName("label_16")
        self.label_20 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_20.setGeometry(QtCore.QRect(460, 30, 41, 17))
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_22.setGeometry(QtCore.QRect(460, 90, 41, 17))
        self.label_22.setObjectName("label_22")
        self.label_21 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_21.setGeometry(QtCore.QRect(460, 120, 41, 17))
        self.label_21.setObjectName("label_21")
        self.label_19 = QtWidgets.QLabel(self.groupBox_modelEvaluation)
        self.label_19.setGeometry(QtCore.QRect(460, 60, 41, 17))
        self.label_19.setObjectName("label_19")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(20, 400, 67, 17))
        self.label_23.setObjectName("label_23")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 420, 601, 61))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(20, 500, 151, 25))
        self.btn_back.setObjectName("pushButton_3")
        self.btn_add_another = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_another.setGeometry(QtCore.QRect(250, 500, 151, 25))
        self.btn_add_another.setObjectName("pushButton_4")
        self.btn_save_return = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_return.setGeometry(QtCore.QRect(470, 500, 151, 25))
        self.btn_save_return.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Product Analysis Tool - Model:Add new"))
        self.label.setText(_translate("MainWindow", "Add a new Model : "))
        self.label_2.setText(_translate("MainWindow", "Name : "))
        self.label_3.setText(_translate("MainWindow", "Type : "))
        self.groupBox_timeseries.setTitle(_translate("MainWindow", "Based Time Series : "))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "  Search"))
        self.groupBox_model_parameters.setTitle(_translate("MainWindow", "Model Parameters"))
        self.label_4.setText(_translate("MainWindow", "PARAM. 1 : "))
        self.label_5.setText(_translate("MainWindow", "PARAM. 2 : "))
        self.label_6.setText(_translate("MainWindow", "PARAM. 3 : "))
        self.btn_evaluate_model.setText(_translate("MainWindow", "Evaluate Model"))
        self.btn_recommend_model.setText(_translate("MainWindow", "Recommend Model"))
        self.groupBox_modelEvaluation.setTitle(_translate("MainWindow", "Model Evaluation"))
        self.label_10.setText(_translate("MainWindow", "ME4:"))
        self.label_13.setText(_translate("MainWindow", "ME8:"))
        self.label_9.setText(_translate("MainWindow", "ME3:"))
        self.label_14.setText(_translate("MainWindow", "ME7:"))
        self.label_11.setText(_translate("MainWindow", "ME6:"))
        self.label_7.setText(_translate("MainWindow", "ME1:"))
        self.label_8.setText(_translate("MainWindow", "ME2:"))
        self.label_12.setText(_translate("MainWindow", "ME5:"))
        self.label_15.setText(_translate("MainWindow", "ME10:"))
        self.label_17.setText(_translate("MainWindow", "ME12:"))
        self.label_18.setText(_translate("MainWindow", "ME11:"))
        self.label_16.setText(_translate("MainWindow", "ME9:"))
        self.label_20.setText(_translate("MainWindow", "ME13:"))
        self.label_22.setText(_translate("MainWindow", "ME15:"))
        self.label_21.setText(_translate("MainWindow", "ME16:"))
        self.label_19.setText(_translate("MainWindow", "ME14:"))
        self.label_23.setText(_translate("MainWindow", "Memo : "))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.btn_add_another.setText(_translate("MainWindow", "Add Another"))
        self.btn_save_return.setText(_translate("MainWindow", "Save and Return"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
#
