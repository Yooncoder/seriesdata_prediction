# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../_uiFiles/Data_Predict1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(988, 813)
        self.gridLayout_7 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget, 8, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.result_gridLayout = QtWidgets.QGridLayout()
        self.result_gridLayout.setObjectName("result_gridLayout")
        self.gridLayout_8.addLayout(self.result_gridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.save_csv = QtWidgets.QPushButton(Dialog)
        self.save_csv.setMinimumSize(QtCore.QSize(150, 30))
        self.save_csv.setStyleSheet("font: 12pt \"굴림\";")
        self.save_csv.setObjectName("save_csv")
        self.horizontalLayout_17.addWidget(self.save_csv)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.minus_pushButton = QtWidgets.QPushButton(Dialog)
        self.minus_pushButton.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.minus_pushButton.setFont(font)
        self.minus_pushButton.setObjectName("minus_pushButton")
        self.horizontalLayout_17.addWidget(self.minus_pushButton)
        self.plus_pushButton = QtWidgets.QPushButton(Dialog)
        self.plus_pushButton.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plus_pushButton.setFont(font)
        self.plus_pushButton.setObjectName("plus_pushButton")
        self.horizontalLayout_17.addWidget(self.plus_pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_17, 1, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_2, 3, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.data_name = QtWidgets.QLabel(Dialog)
        self.data_name.setText("")
        self.data_name.setObjectName("data_name")
        self.gridLayout.addWidget(self.data_name, 2, 1, 1, 1)
        self.Import_Model = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Import_Model.sizePolicy().hasHeightForWidth())
        self.Import_Model.setSizePolicy(sizePolicy)
        self.Import_Model.setMinimumSize(QtCore.QSize(150, 150))
        self.Import_Model.setMaximumSize(QtCore.QSize(150, 150))
        self.Import_Model.setToolTip("")
        self.Import_Model.setText("")
        self.Import_Model.setObjectName("Import_Model")
        self.gridLayout.addWidget(self.Import_Model, 1, 3, 1, 1)
        self.predict_pushbutton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.predict_pushbutton.sizePolicy().hasHeightForWidth())
        self.predict_pushbutton.setSizePolicy(sizePolicy)
        self.predict_pushbutton.setMinimumSize(QtCore.QSize(150, 150))
        self.predict_pushbutton.setMaximumSize(QtCore.QSize(150, 150))
        self.predict_pushbutton.setToolTip("")
        self.predict_pushbutton.setText("")
        self.predict_pushbutton.setObjectName("predict_pushbutton")
        self.gridLayout.addWidget(self.predict_pushbutton, 1, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 6, 1, 1)
        self.Import_Data = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Import_Data.sizePolicy().hasHeightForWidth())
        self.Import_Data.setSizePolicy(sizePolicy)
        self.Import_Data.setMinimumSize(QtCore.QSize(150, 150))
        self.Import_Data.setMaximumSize(QtCore.QSize(150, 150))
        self.Import_Data.setToolTip("")
        self.Import_Data.setText("")
        self.Import_Data.setObjectName("Import_Data")
        self.gridLayout.addWidget(self.Import_Data, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.model_name = QtWidgets.QLabel(Dialog)
        self.model_name.setText("")
        self.model_name.setObjectName("model_name")
        self.gridLayout.addWidget(self.model_name, 2, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 2, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.groupBox_5)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 229, 79))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout.setObjectName("formLayout")
        self.label_x = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_x.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_x.setFont(font)
        self.label_x.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_x.setObjectName("label_x")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_x)
        self.comboBox_x = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.comboBox_x.setMinimumSize(QtCore.QSize(100, 25))
        self.comboBox_x.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_x.setFont(font)
        self.comboBox_x.setObjectName("comboBox_x")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_x)
        self.label_y = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_y.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_y.setFont(font)
        self.label_y.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_y.setObjectName("label_y")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_y)
        self.comboBox_y = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.comboBox_y.setMinimumSize(QtCore.QSize(100, 25))
        self.comboBox_y.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_y.setFont(font)
        self.comboBox_y.setObjectName("comboBox_y")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_y)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_6.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 440, 109))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout_4 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setMinimumSize(QtCore.QSize(100, 25))
        self.label_5.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Date_combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.Date_combobox.setMinimumSize(QtCore.QSize(100, 25))
        self.Date_combobox.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Date_combobox.setFont(font)
        self.Date_combobox.setObjectName("Date_combobox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Date_combobox)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setMinimumSize(QtCore.QSize(100, 25))
        self.label_15.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.Close_combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.Close_combobox.setMinimumSize(QtCore.QSize(100, 25))
        self.Close_combobox.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Close_combobox.setFont(font)
        self.Close_combobox.setObjectName("Close_combobox")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Close_combobox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 418, 143))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setMinimumSize(QtCore.QSize(100, 25))
        self.label_6.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Open_combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.Open_combobox.setMinimumSize(QtCore.QSize(100, 25))
        self.Open_combobox.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Open_combobox.setFont(font)
        self.Open_combobox.setObjectName("Open_combobox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Open_combobox)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setMinimumSize(QtCore.QSize(100, 25))
        self.label_7.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.High_combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.High_combobox.setMinimumSize(QtCore.QSize(100, 25))
        self.High_combobox.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.High_combobox.setFont(font)
        self.High_combobox.setObjectName("High_combobox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.High_combobox)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setMinimumSize(QtCore.QSize(100, 25))
        self.label_8.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Low_combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.Low_combobox.setMinimumSize(QtCore.QSize(100, 25))
        self.Low_combobox.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Low_combobox.setFont(font)
        self.Low_combobox.setObjectName("Low_combobox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Low_combobox)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setMinimumSize(QtCore.QSize(100, 25))
        self.label_16.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.Volume_combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.Volume_combobox.setMinimumSize(QtCore.QSize(100, 25))
        self.Volume_combobox.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Volume_combobox.setFont(font)
        self.Volume_combobox.setObjectName("Volume_combobox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Volume_combobox)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_9.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_8, "")
        self.gridLayout_7.addWidget(self.tabWidget, 2, 0, 1, 2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setMinimumSize(QtCore.QSize(20, 20))
        self.label_17.setMaximumSize(QtCore.QSize(160000, 160000))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.predict_periods = QtWidgets.QLineEdit(Dialog)
        self.predict_periods.setMinimumSize(QtCore.QSize(200, 26))
        self.predict_periods.setMaximumSize(QtCore.QSize(200, 160000))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.predict_periods.setFont(font)
        self.predict_periods.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.predict_periods.setObjectName("predict_periods")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.predict_periods)
        self.gridLayout_7.addLayout(self.formLayout_2, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.Import_Data, self.Import_Model)
        Dialog.setTabOrder(self.Import_Model, self.predict_pushbutton)
        Dialog.setTabOrder(self.predict_pushbutton, self.predict_periods)
        Dialog.setTabOrder(self.predict_periods, self.minus_pushButton)
        Dialog.setTabOrder(self.minus_pushButton, self.plus_pushButton)
        Dialog.setTabOrder(self.plus_pushButton, self.tableWidget)
        Dialog.setTabOrder(self.tableWidget, self.tabWidget)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Dataset"))
        self.groupBox_3.setTitle(_translate("Dialog", "예측 그래프"))
        self.save_csv.setToolTip(_translate("Dialog", "예측된 결과를 CSV 파일로 저장합니다."))
        self.save_csv.setText(_translate("Dialog", "SAVE(CSV)"))
        self.minus_pushButton.setToolTip(_translate("Dialog", "결과 그래프를 축소합니다."))
        self.minus_pushButton.setText(_translate("Dialog", "-"))
        self.plus_pushButton.setToolTip(_translate("Dialog", "결과 그래프를 확대합니다."))
        self.plus_pushButton.setText(_translate("Dialog", "+"))
        self.label_3.setToolTip(_translate("Dialog", "예측을 시작합니다."))
        self.label_3.setText(_translate("Dialog", "실행"))
        self.label_2.setToolTip(_translate("Dialog", "사용하고 싶은 모델을 불러와주세요.<br/>ARIMA = pkl, LSTM = h5"))
        self.label_2.setText(_translate("Dialog", "Model Load"))
        self.label.setToolTip(_translate("Dialog", "사용하고 싶은 CSV 파일을 불러와주세요."))
        self.label.setText(_translate("Dialog", "Data Load"))
        self.groupBox_5.setTitle(_translate("Dialog", "축 설정"))
        self.label_x.setToolTip(_translate("Dialog", "시간에 해당하는 컬럼을 선택해주세요."))
        self.label_x.setText(_translate("Dialog", "x 축"))
        self.comboBox_x.setToolTip(_translate("Dialog", "시간에 해당하는 컬럼을 선택해주세요."))
        self.label_y.setToolTip(_translate("Dialog", "예측하고 싶은 결과에 대한 컬럼을 선택해주세요."))
        self.label_y.setText(_translate("Dialog", "y 축"))
        self.comboBox_y.setToolTip(_translate("Dialog", "예측하고 싶은 결과에 대한 컬럼을 선택해주세요."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Dialog", "ARIMA"))
        self.groupBox_2.setTitle(_translate("Dialog", "축 설정"))
        self.label_5.setToolTip(_translate("Dialog", "시간에 해당하는 컬럼을 선택해주세요."))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>x 축</p></body></html>"))
        self.Date_combobox.setToolTip(_translate("Dialog", "시간에 해당하는 컬럼을 선택해주세요."))
        self.label_15.setToolTip(_translate("Dialog", "예측하고 싶은 결과에 대한 컬럼을 선택해주세요."))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p>y 축</p></body></html>"))
        self.Close_combobox.setToolTip(_translate("Dialog", "예측하고 싶은 결과에 대한 컬럼을 선택해주세요."))
        self.groupBox_4.setTitle(_translate("Dialog", "인자 설정"))
        self.label_6.setToolTip(_translate("Dialog", "시작가에 해당하는 컬럼을 선택해주세요."))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Open</span></p></body></html>"))
        self.Open_combobox.setToolTip(_translate("Dialog", "시작가에 해당하는 컬럼을 선택해주세요."))
        self.label_7.setToolTip(_translate("Dialog", "최고가에 해당하는 컬럼을 선택해주세요."))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">High</span></p></body></html>"))
        self.High_combobox.setToolTip(_translate("Dialog", "최고가에 해당하는 컬럼을 선택해주세요."))
        self.label_8.setToolTip(_translate("Dialog", "최저가에 해당하는 컬럼을 선택해주세요."))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Low</span></p></body></html>"))
        self.Low_combobox.setToolTip(_translate("Dialog", "최저가에 해당하는 컬럼을 선택해주세요."))
        self.label_16.setToolTip(_translate("Dialog", "거래량에 해당하는 컬럼을 선택해주세요."))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Volume</span></p></body></html>"))
        self.Volume_combobox.setToolTip(_translate("Dialog", "거래량에 해당하는 컬럼을 선택해주세요."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Dialog", "LSTM"))
        self.label_17.setToolTip(_translate("Dialog", "예측하고 싶은 기간을 정수로 입력해주세요."))
        self.label_17.setText(_translate("Dialog", "예측 기간 설정"))
        self.predict_periods.setToolTip(_translate("Dialog", "예측하고 싶은 기간을 정수로 입력해주세요."))
        self.predict_periods.setPlaceholderText(_translate("Dialog", "ex ) 10일 = 10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
