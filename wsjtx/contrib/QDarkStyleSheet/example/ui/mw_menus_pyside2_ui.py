# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw_menus.ui'
#
# Created: Thu Dec 13 17:14:05 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.groupBox_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget.addTab(self.tab_12, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 1, 0, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.centralwidget)
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_71")
        self.gridLayout_7.addWidget(self.label_71, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 596, 28))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuMenuSub = QtWidgets.QMenu(self.menuMenu)
        self.menuMenuSub.setObjectName("menuMenuSub")
        self.menuMenuDelayed = QtWidgets.QMenu(self.menubar)
        self.menuMenuDelayed.setObjectName("menuMenuDelayed")
        self.menuMenuSubDelayed = QtWidgets.QMenu(self.menuMenuDelayed)
        self.menuMenuSubDelayed.setObjectName("menuMenuSubDelayed")
        self.menuMenuCheckale = QtWidgets.QMenu(self.menubar)
        self.menuMenuCheckale.setObjectName("menuMenuCheckale")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBarDelayed = QtWidgets.QToolBar(MainWindow)
        self.toolBarDelayed.setObjectName("toolBarDelayed")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarDelayed)
        self.toolBarCheckable = QtWidgets.QToolBar(MainWindow)
        self.toolBarCheckable.setObjectName("toolBarCheckable")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarCheckable)
        MainWindow.insertToolBarBreak(self.toolBarCheckable)
        self.actionActionA = QtWidgets.QAction(MainWindow)
        self.actionActionA.setObjectName("actionActionA")
        self.actionActionSubA = QtWidgets.QAction(MainWindow)
        self.actionActionSubA.setObjectName("actionActionSubA")
        self.actionActionSubB = QtWidgets.QAction(MainWindow)
        self.actionActionSubB.setObjectName("actionActionSubB")
        self.actionActionDelayedA = QtWidgets.QAction(MainWindow)
        self.actionActionDelayedA.setObjectName("actionActionDelayedA")
        self.actionActionDelayedSubA = QtWidgets.QAction(MainWindow)
        self.actionActionDelayedSubA.setObjectName("actionActionDelayedSubA")
        self.actionActionCheckableA = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableA.setCheckable(True)
        self.actionActionCheckableA.setObjectName("actionActionCheckableA")
        self.actionActionCheckableSubAChecked = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableSubAChecked.setCheckable(True)
        self.actionActionCheckableSubAChecked.setChecked(True)
        self.actionActionCheckableSubAChecked.setObjectName("actionActionCheckableSubAChecked")
        self.actionActionCheckableSubAUnchecked = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableSubAUnchecked.setCheckable(True)
        self.actionActionCheckableSubAUnchecked.setObjectName("actionActionCheckableSubAUnchecked")
        self.menuMenuSub.addAction(self.actionActionSubA)
        self.menuMenuSub.addAction(self.actionActionSubB)
        self.menuMenu.addAction(self.actionActionA)
        self.menuMenu.addAction(self.menuMenuSub.menuAction())
        self.menuMenuSubDelayed.addAction(self.actionActionDelayedSubA)
        self.menuMenuDelayed.addAction(self.actionActionDelayedA)
        self.menuMenuDelayed.addAction(self.menuMenuSubDelayed.menuAction())
        self.menuMenuCheckale.addAction(self.actionActionCheckableA)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuMenuDelayed.menuAction())
        self.menubar.addAction(self.menuMenuCheckale.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionActionA)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionActionSubA)
        self.toolBar.addAction(self.actionActionSubB)
        self.toolBarDelayed.addAction(self.actionActionDelayedA)
        self.toolBarDelayed.addSeparator()
        self.toolBarDelayed.addAction(self.actionActionDelayedSubA)
        self.toolBarCheckable.addAction(self.actionActionCheckableA)
        self.toolBarCheckable.addSeparator()
        self.toolBarCheckable.addAction(self.actionActionCheckableSubAChecked)
        self.toolBarCheckable.addAction(self.actionActionCheckableSubAUnchecked)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.lineEdit_2)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Issue #115 - Tabs scroller buttons", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Issue #123 - Missing borders", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "Inside tab, outside frame", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.lineEdit_2.setText(QtWidgets.QApplication.translate("MainWindow", "Inside tab and frame", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Tab 1", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Tab 2", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Issue #112 - Hyperlinks color", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><a href=\"https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues/112\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">Hyperlink Example</span></a></p><p align=\"center\"><span style=\" font-size:10pt; color:#7d7d7d;\">CSS for the documents (RichText) is not the same as the application. We cannot change the internal content CSS, e.g., hyperlinks. We suggest you use the middle tons (0-255, use 125), so this works for both white and dark theme (this color). The original color is the blue link on top.</span></p><p align=\"center\"><br/></p></body></html>", None, -1))
        self.label_71.setText(QtWidgets.QApplication.translate("MainWindow", "Inside Central Widget", None, -1))
        self.menuMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Menu", None, -1))
        self.menuMenuSub.setTitle(QtWidgets.QApplication.translate("MainWindow", "Menu Sub", None, -1))
        self.menuMenuDelayed.setTitle(QtWidgets.QApplication.translate("MainWindow", "Menu Delayed", None, -1))
        self.menuMenuSubDelayed.setTitle(QtWidgets.QApplication.translate("MainWindow", "Menu Sub Delayed", None, -1))
        self.menuMenuCheckale.setTitle(QtWidgets.QApplication.translate("MainWindow", "Menu Checkable", None, -1))
        self.menuAbout.setTitle(QtWidgets.QApplication.translate("MainWindow", "About QDarkStyle", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.toolBar.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Tool bar actions", None, -1))
        self.toolBarDelayed.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Tool bar actions delayed", None, -1))
        self.toolBarCheckable.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Tool bar action checkable", None, -1))
        self.actionActionA.setText(QtWidgets.QApplication.translate("MainWindow", "Action A", None, -1))
        self.actionActionSubA.setText(QtWidgets.QApplication.translate("MainWindow", "Action A Sub", None, -1))
        self.actionActionSubA.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Action A Sub", None, -1))
        self.actionActionSubB.setText(QtWidgets.QApplication.translate("MainWindow", "Action B Sub", None, -1))
        self.actionActionDelayedA.setText(QtWidgets.QApplication.translate("MainWindow", "Action Delayed A", None, -1))
        self.actionActionDelayedA.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Action Delayed A", None, -1))
        self.actionActionDelayedSubA.setText(QtWidgets.QApplication.translate("MainWindow", "Action Delayed Sub A", None, -1))
        self.actionActionDelayedSubA.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Action Delayed Sub A", None, -1))
        self.actionActionCheckableA.setText(QtWidgets.QApplication.translate("MainWindow", "Action Checkable A", None, -1))
        self.actionActionCheckableA.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Action Checkable A", None, -1))
        self.actionActionCheckableSubAChecked.setText(QtWidgets.QApplication.translate("MainWindow", "Action Checkable Sub A Checked", None, -1))
        self.actionActionCheckableSubAChecked.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Action Checkable Sub A Checked", None, -1))
        self.actionActionCheckableSubAUnchecked.setText(QtWidgets.QApplication.translate("MainWindow", "Action Checkable Sub A Unchecked", None, -1))
        self.actionActionCheckableSubAUnchecked.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Action Checkable Sub A Unchecked", None, -1))

