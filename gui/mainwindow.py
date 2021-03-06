# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui/qt\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# Added by buildgui.py script to support pyinstaller
from src.pyinstaller_helper import PyInstallerHelper

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setObjectName("statusLabel")
        self.horizontalLayout_3.addWidget(self.statusLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.connectionComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.connectionComboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.connectionComboBox.setObjectName("connectionComboBox")
        self.horizontalLayout_3.addWidget(self.connectionComboBox)
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(PyInstallerHelper.resource_path("icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_3.addWidget(self.refreshButton)
        self.connectionStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectionStackedWidget.sizePolicy().hasHeightForWidth())
        self.connectionStackedWidget.setSizePolicy(sizePolicy)
        self.connectionStackedWidget.setObjectName("connectionStackedWidget")
        self.uartPage = QtWidgets.QWidget()
        self.uartPage.setObjectName("uartPage")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.uartPage)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.uartPage)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.baudComboBox = QtWidgets.QComboBox(self.uartPage)
        self.baudComboBox.setObjectName("baudComboBox")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.baudComboBox)
        self.serialResetCheckBox = QtWidgets.QCheckBox(self.uartPage)
        self.serialResetCheckBox.setChecked(False)
        self.serialResetCheckBox.setObjectName("serialResetCheckBox")
        self.horizontalLayout_5.addWidget(self.serialResetCheckBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.connectionStackedWidget.addWidget(self.uartPage)
        self.wifiPage = QtWidgets.QWidget()
        self.wifiPage.setObjectName("wifiPage")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.wifiPage)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.wifiPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.ipLineEdit = QtWidgets.QLineEdit(self.wifiPage)
        self.ipLineEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.horizontalLayout_6.addWidget(self.ipLineEdit)
        self.label_6 = QtWidgets.QLabel(self.wifiPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.portSpinBox = QtWidgets.QSpinBox(self.wifiPage)
        self.portSpinBox.setMaximum(65536)
        self.portSpinBox.setProperty("value", 8266)
        self.portSpinBox.setObjectName("portSpinBox")
        self.horizontalLayout_6.addWidget(self.portSpinBox)
        self.presetButton = QtWidgets.QPushButton(self.wifiPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presetButton.sizePolicy().hasHeightForWidth())
        self.presetButton.setSizePolicy(sizePolicy)
        self.presetButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.presetButton.setObjectName("presetButton")
        self.horizontalLayout_6.addWidget(self.presetButton)
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.connectionStackedWidget.addWidget(self.wifiPage)
        self.horizontalLayout_3.addWidget(self.connectionStackedWidget)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_3.addWidget(self.connectButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.localFilesTreeView = QtWidgets.QTreeView(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localFilesTreeView.sizePolicy().hasHeightForWidth())
        self.localFilesTreeView.setSizePolicy(sizePolicy)
        self.localFilesTreeView.setMinimumSize(QtCore.QSize(250, 0))
        self.localFilesTreeView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.localFilesTreeView.setBaseSize(QtCore.QSize(0, 0))
        self.localFilesTreeView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.localFilesTreeView.setSortingEnabled(True)
        self.localFilesTreeView.setObjectName("localFilesTreeView")
        self.verticalLayout_2.addWidget(self.localFilesTreeView)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.compileButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.compileButton.setObjectName("compileButton")
        self.horizontalLayout_7.addWidget(self.compileButton)
        self.autoTransferCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.autoTransferCheckBox.setMaximumSize(QtCore.QSize(90, 16777215))
        self.autoTransferCheckBox.setObjectName("autoTransferCheckBox")
        self.horizontalLayout_7.addWidget(self.autoTransferCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.remoteNameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.remoteNameEdit.setObjectName("remoteNameEdit")
        self.horizontalLayout_4.addWidget(self.remoteNameEdit)
        self.transferToMcuButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.transferToMcuButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.transferToMcuButton.setObjectName("transferToMcuButton")
        self.horizontalLayout_4.addWidget(self.transferToMcuButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.mcuFilesListView = QtWidgets.QListView(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mcuFilesListView.sizePolicy().hasHeightForWidth())
        self.mcuFilesListView.setSizePolicy(sizePolicy)
        self.mcuFilesListView.setMinimumSize(QtCore.QSize(150, 0))
        self.mcuFilesListView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mcuFilesListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.mcuFilesListView.setObjectName("mcuFilesListView")
        self.verticalLayout.addWidget(self.mcuFilesListView)
        self.listButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listButton.sizePolicy().hasHeightForWidth())
        self.listButton.setSizePolicy(sizePolicy)
        self.listButton.setObjectName("listButton")
        self.verticalLayout.addWidget(self.listButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.executeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.executeButton.setObjectName("executeButton")
        self.horizontalLayout.addWidget(self.executeButton)
        self.removeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout.addWidget(self.removeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.localPathEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.localPathEdit.setObjectName("localPathEdit")
        self.horizontalLayout_2.addWidget(self.localPathEdit)
        self.transferToPcButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.transferToPcButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.transferToPcButton.setObjectName("transferToPcButton")
        self.horizontalLayout_2.addWidget(self.transferToPcButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNavigate = QtWidgets.QAction(MainWindow)
        self.actionNavigate.setObjectName("actionNavigate")
        self.actionTerminal = QtWidgets.QAction(MainWindow)
        self.actionTerminal.setObjectName("actionTerminal")
        self.actionUpload = QtWidgets.QAction(MainWindow)
        self.actionUpload.setObjectName("actionUpload")
        self.actionCode_Editor = QtWidgets.QAction(MainWindow)
        self.actionCode_Editor.setObjectName("actionCode_Editor")
        self.actionFlash = QtWidgets.QAction(MainWindow)
        self.actionFlash.setObjectName("actionFlash")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionNavigate)
        self.menuFile.addAction(self.actionUpload)
        self.menuFile.addAction(self.actionFlash)
        self.menuView.addAction(self.actionTerminal)
        self.menuView.addAction(self.actionCode_Editor)
        self.menuOptions.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.connectionStackedWidget.setCurrentIndex(0)
        self.baudComboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "uPyLoader"))
        self.label_3.setText(_translate("MainWindow", "Status:"))
        self.statusLabel.setText(_translate("MainWindow", "Disconnected"))
        self.label_2.setText(_translate("MainWindow", "Connection"))
        self.label.setText(_translate("MainWindow", "Baud rate:"))
        self.baudComboBox.setItemText(0, _translate("MainWindow", "9600"))
        self.baudComboBox.setItemText(1, _translate("MainWindow", "115200"))
        self.serialResetCheckBox.setText(_translate("MainWindow", "Issue reset"))
        self.label_5.setText(_translate("MainWindow", "IP"))
        self.ipLineEdit.setText(_translate("MainWindow", "192.168.4.1"))
        self.label_6.setText(_translate("MainWindow", "Port"))
        self.presetButton.setText(_translate("MainWindow", "preset"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.label_7.setText(_translate("MainWindow", "Local"))
        self.compileButton.setText(_translate("MainWindow", "Compile"))
        self.autoTransferCheckBox.setText(_translate("MainWindow", "Auto-transfer"))
        self.label_9.setText(_translate("MainWindow", "MCU name:"))
        self.transferToMcuButton.setText(_translate("MainWindow", "Transfer"))
        self.label_4.setText(_translate("MainWindow", "Remote (MCU)"))
        self.listButton.setText(_translate("MainWindow", "List files"))
        self.executeButton.setText(_translate("MainWindow", "Execute"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.label_8.setText(_translate("MainWindow", "PC path:"))
        self.transferToPcButton.setText(_translate("MainWindow", "Transfer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionNavigate.setText(_translate("MainWindow", "Navigate"))
        self.actionTerminal.setText(_translate("MainWindow", "Terminal"))
        self.actionUpload.setText(_translate("MainWindow", "Init transfer files"))
        self.actionCode_Editor.setText(_translate("MainWindow", "Code Editor"))
        self.actionFlash.setText(_translate("MainWindow", "Flash firmware"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

