# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/baubek/PycharmProjects/LabelingToolWithPy3/LabeltoolDesign.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resource

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(950, 654)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/icons/sosivio_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/icons/sosivio_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/icons/sosivio_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/icons/sosivio_logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        mainWindow.setWindowIcon(icon)
        mainWindow.setWindowOpacity(1.0)
        mainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color: rgb(24, 55, 87);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 20, 781, 82))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hl_Header = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hl_Header.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.hl_Header.setContentsMargins(0, 0, 0, 0)
        self.hl_Header.setSpacing(90)
        self.hl_Header.setObjectName("hl_Header")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.hl_Header.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icon/icons/sosivio_logo.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.hl_Header.addWidget(self.label_4)
        self.hl_Header.setStretch(0, 6)
        self.hl_Header.setStretch(1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(100, 140, 601, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.hl_buttons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hl_buttons.setContentsMargins(0, 0, 0, 0)
        self.hl_buttons.setSpacing(0)
        self.hl_buttons.setObjectName("hl_buttons")
        self.vl_LoadBtn = QtWidgets.QVBoxLayout()
        self.vl_LoadBtn.setContentsMargins(3, 3, 3, 3)
        self.vl_LoadBtn.setSpacing(1)
        self.vl_LoadBtn.setObjectName("vl_LoadBtn")
        self.btnLoad = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLoad.sizePolicy().hasHeightForWidth())
        self.btnLoad.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnLoad.setFont(font)
        self.btnLoad.setStyleSheet("background-color: rgb(67, 168, 217);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.btnLoad.setObjectName("btnLoad")
        self.vl_LoadBtn.addWidget(self.btnLoad)
        self.vl_LoadBtn.setStretch(0, 5)
        self.hl_buttons.addLayout(self.vl_LoadBtn)
        self.line_1 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.hl_buttons.addWidget(self.line_1)
        self.vl_LabelBtn = QtWidgets.QVBoxLayout()
        self.vl_LabelBtn.setContentsMargins(3, 3, 3, 3)
        self.vl_LabelBtn.setSpacing(1)
        self.vl_LabelBtn.setObjectName("vl_LabelBtn")
        self.btnLabel = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLabel.sizePolicy().hasHeightForWidth())
        self.btnLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnLabel.setFont(font)
        self.btnLabel.setStyleSheet("background-color: rgb(33, 85, 217);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.btnLabel.setObjectName("btnLabel")
        self.vl_LabelBtn.addWidget(self.btnLabel)
        self.vl_LabelBtn.setStretch(0, 5)
        self.hl_buttons.addLayout(self.vl_LabelBtn)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.hl_buttons.addWidget(self.line_2)
        self.vl_ReportBtn = QtWidgets.QVBoxLayout()
        self.vl_ReportBtn.setContentsMargins(3, 3, 3, 3)
        self.vl_ReportBtn.setSpacing(1)
        self.vl_ReportBtn.setObjectName("vl_ReportBtn")
        self.btnReport = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReport.sizePolicy().hasHeightForWidth())
        self.btnReport.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnReport.setFont(font)
        self.btnReport.setStyleSheet("background-color: rgb(180, 218, 239);\n"
"border-color: rgb(186, 189, 182);\n"
"color: rgb(6, 70, 127);")
        self.btnReport.setObjectName("btnReport")
        self.vl_ReportBtn.addWidget(self.btnReport)
        self.vl_ReportBtn.setStretch(0, 5)
        self.hl_buttons.addLayout(self.vl_ReportBtn)
        self.hl_buttons.setStretch(0, 2)
        self.hl_buttons.setStretch(1, 2)
        self.hl_buttons.setStretch(2, 2)
        self.hl_buttons.setStretch(3, 2)
        self.hl_buttons.setStretch(4, 2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 290, 561, 72))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.hl_Level_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.hl_Level_1.setContentsMargins(0, 0, 0, 0)
        self.hl_Level_1.setSpacing(50)
        self.hl_Level_1.setObjectName("hl_Level_1")
        self.labelText_TemplateText = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(14)
        self.labelText_TemplateText.setFont(font)
        self.labelText_TemplateText.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelText_TemplateText.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labelText_TemplateText.setObjectName("labelText_TemplateText")
        self.hl_Level_1.addWidget(self.labelText_TemplateText)
        self.vl_Terms = QtWidgets.QVBoxLayout()
        self.vl_Terms.setContentsMargins(1, 1, 1, 1)
        self.vl_Terms.setSpacing(0)
        self.vl_Terms.setObjectName("vl_Terms")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.vl_Terms.addWidget(self.label)
        self.lineEdit_Terms = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Terms.sizePolicy().hasHeightForWidth())
        self.lineEdit_Terms.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(12)
        self.lineEdit_Terms.setFont(font)
        self.lineEdit_Terms.setStyleSheet("background-color: rgb(180, 218, 239);\n"
"color: rgb(148, 159, 166);")
        self.lineEdit_Terms.setObjectName("lineEdit_Terms")
        self.vl_Terms.addWidget(self.lineEdit_Terms)
        self.vl_Terms.setStretch(0, 1)
        self.vl_Terms.setStretch(1, 1)
        self.hl_Level_1.addLayout(self.vl_Terms)
        self.vl_Classes = QtWidgets.QVBoxLayout()
        self.vl_Classes.setContentsMargins(1, 1, 1, 1)
        self.vl_Classes.setSpacing(2)
        self.vl_Classes.setObjectName("vl_Classes")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.btnAddLabel = QtWidgets.QToolButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddLabel.sizePolicy().hasHeightForWidth())
        self.btnAddLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddLabel.setFont(font)
        self.btnAddLabel.setStyleSheet("background-color: rgb(180, 218, 239);\n"
"color: rgb(78, 154, 6);")
        self.btnAddLabel.setObjectName("btnAddLabel")
        self.horizontalLayout.addWidget(self.btnAddLabel)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.vl_Classes.addLayout(self.horizontalLayout)
        self.comboBox_Classes = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox_Classes.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Classes.sizePolicy().hasHeightForWidth())
        self.comboBox_Classes.setSizePolicy(sizePolicy)
        self.comboBox_Classes.setStyleSheet("background-color: rgb(180, 218, 239);\n"
"color: rgb(148, 159, 166);")
        self.comboBox_Classes.setObjectName("comboBox_Classes")
        self.vl_Classes.addWidget(self.comboBox_Classes)
        self.vl_Classes.setStretch(0, 1)
        self.vl_Classes.setStretch(1, 3)
        self.hl_Level_1.addLayout(self.vl_Classes)
        self.hl_Level_1.setStretch(0, 1)
        self.hl_Level_1.setStretch(1, 7)
        self.hl_Level_1.setStretch(2, 1)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(70, 230, 661, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.hl_FileNames = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.hl_FileNames.setContentsMargins(1, 0, 2, 2)
        self.hl_FileNames.setSpacing(30)
        self.hl_FileNames.setObjectName("hl_FileNames")
        self.lt_TempSetFileName = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(13)
        self.lt_TempSetFileName.setFont(font)
        self.lt_TempSetFileName.setStyleSheet("color: rgb(255, 255, 255);")
        self.lt_TempSetFileName.setText("")
        self.lt_TempSetFileName.setObjectName("lt_TempSetFileName")
        self.hl_FileNames.addWidget(self.lt_TempSetFileName)
        self.lt_TrainingSetFileName = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(13)
        self.lt_TrainingSetFileName.setFont(font)
        self.lt_TrainingSetFileName.setStyleSheet("color: rgb(255, 255, 255);")
        self.lt_TrainingSetFileName.setText("")
        self.lt_TrainingSetFileName.setAlignment(QtCore.Qt.AlignCenter)
        self.lt_TrainingSetFileName.setObjectName("lt_TrainingSetFileName")
        self.hl_FileNames.addWidget(self.lt_TrainingSetFileName)
        self.lt_LabeledTermsReportFileName = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(13)
        self.lt_LabeledTermsReportFileName.setFont(font)
        self.lt_LabeledTermsReportFileName.setStyleSheet("color: rgb(255, 255, 255);")
        self.lt_LabeledTermsReportFileName.setText("")
        self.lt_LabeledTermsReportFileName.setObjectName("lt_LabeledTermsReportFileName")
        self.hl_FileNames.addWidget(self.lt_LabeledTermsReportFileName)
        self.hl_FileNames.setStretch(0, 1)
        self.hl_FileNames.setStretch(1, 1)
        self.hl_FileNames.setStretch(2, 1)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(30, 360, 895, 272))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.hl_TemplateJSONtext = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.hl_TemplateJSONtext.setContentsMargins(0, 0, 0, 0)
        self.hl_TemplateJSONtext.setSpacing(10)
        self.hl_TemplateJSONtext.setObjectName("hl_TemplateJSONtext")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_TemplateContext = QtWidgets.QTextEdit(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(12)
        self.textEdit_TemplateContext.setFont(font)
        self.textEdit_TemplateContext.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(135, 135, 135);")
        self.textEdit_TemplateContext.setReadOnly(True)
        self.textEdit_TemplateContext.setObjectName("textEdit_TemplateContext")
        self.verticalLayout.addWidget(self.textEdit_TemplateContext)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnPrev = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btnPrev.setStyleSheet("background-color: rgb(180, 218, 239);\n"
"color: rgb(0, 0, 0);")
        self.btnPrev.setObjectName("btnPrev")
        self.horizontalLayout_2.addWidget(self.btnPrev)
        self.lt_CountDownJSONContext = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.lt_CountDownJSONContext.setStyleSheet("color: rgb(255, 255, 255);")
        self.lt_CountDownJSONContext.setText("")
        self.lt_CountDownJSONContext.setAlignment(QtCore.Qt.AlignCenter)
        self.lt_CountDownJSONContext.setObjectName("lt_CountDownJSONContext")
        self.horizontalLayout_2.addWidget(self.lt_CountDownJSONContext)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.le_temp_num = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.le_temp_num.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 236);")
        self.le_temp_num.setObjectName("le_temp_num")
        self.horizontalLayout_3.addWidget(self.le_temp_num)
        self.btnNext = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btnNext.setStyleSheet("background-color: rgb(180, 218, 239);\n"
"color: rgb(0, 0, 0);")
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout_3.addWidget(self.btnNext)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 13)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.hl_TemplateJSONtext.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tv_LabeledTerms = QtWidgets.QTableView(self.horizontalLayoutWidget_5)
        self.tv_LabeledTerms.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"color: rgb(0, 0, 0);")
        self.tv_LabeledTerms.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tv_LabeledTerms.setLineWidth(4)
        self.tv_LabeledTerms.setMidLineWidth(3)
        self.tv_LabeledTerms.setSortingEnabled(False)
        self.tv_LabeledTerms.setObjectName("tv_LabeledTerms")
        self.verticalLayout_2.addWidget(self.tv_LabeledTerms)
        self.lt_LabledTermFName = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(14)
        self.lt_LabledTermFName.setFont(font)
        self.lt_LabledTermFName.setStyleSheet("color: rgb(255, 255, 255);")
        self.lt_LabledTermFName.setAlignment(QtCore.Qt.AlignCenter)
        self.lt_LabledTermFName.setObjectName("lt_LabledTermFName")
        self.verticalLayout_2.addWidget(self.lt_LabledTermFName)
        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 1)
        self.hl_TemplateJSONtext.addLayout(self.verticalLayout_2)
        self.hl_TemplateJSONtext.setStretch(0, 7)
        self.hl_TemplateJSONtext.setStretch(1, 4)
        self.labelText_TermsLabel = QtWidgets.QLabel(self.centralwidget)
        self.labelText_TermsLabel.setGeometry(QtCore.QRect(640, 330, 251, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelText_TermsLabel.sizePolicy().hasHeightForWidth())
        self.labelText_TermsLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(14)
        self.labelText_TermsLabel.setFont(font)
        self.labelText_TermsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelText_TermsLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.labelText_TermsLabel.setObjectName("labelText_TermsLabel")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 110, 601, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(770, 100, 131, 31))
        self.label_3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        mainWindow.setCentralWidget(self.centralwidget)
        self.actionsave = QtWidgets.QAction(mainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label_2.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">SOSIVIO Labeling Tool for KuBERT</span></p></body></html>"))
        self.btnLoad.setText(_translate("mainWindow", "LOAD"))
        self.btnLabel.setText(_translate("mainWindow", "LABEL"))
        self.btnReport.setText(_translate("mainWindow", "REPORT"))
        self.labelText_TemplateText.setText(_translate("mainWindow", "Template Text"))
        self.label.setText(_translate("mainWindow", "Term to Label"))
        self.lineEdit_Terms.setPlaceholderText(_translate("mainWindow", "Please, enter the term to label"))
        self.label_5.setText(_translate("mainWindow", "LABEL:"))
        self.btnAddLabel.setText(_translate("mainWindow", "+"))
        self.textEdit_TemplateContext.setPlaceholderText(_translate("mainWindow", "Here is going to be the context of the templates json file"))
        self.btnPrev.setText(_translate("mainWindow", "Back"))
        self.le_temp_num.setPlaceholderText(_translate("mainWindow", "page #"))
        self.btnNext.setText(_translate("mainWindow", "Next"))
        self.lt_LabledTermFName.setText(_translate("mainWindow", "Labeled_Terms.json"))
        self.labelText_TermsLabel.setText(_translate("mainWindow", "Labeled Terms"))
        self.label_3.setText(_translate("mainWindow", "Version: 1.03.01"))
        self.actionsave.setText(_translate("mainWindow", "Save"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())