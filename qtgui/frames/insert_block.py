# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/.virtualenvs/pinguino_env/pinguino/pinguino-ide/qtgui/frames/insert_block.ui'
#
# Created: Thu Feb  6 21:00:55 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_InsertBlock(object):
    def setupUi(self, InsertBlock):
        InsertBlock.setObjectName("InsertBlock")
        InsertBlock.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(InsertBlock)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtGui.QLineEdit(InsertBlock)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.listWidget = QtGui.QListWidget(InsertBlock)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)

        self.retranslateUi(InsertBlock)
        QtCore.QMetaObject.connectSlotsByName(InsertBlock)

    def retranslateUi(self, InsertBlock):
        InsertBlock.setWindowTitle(QtGui.QApplication.translate("InsertBlock", "Insert Block", None, QtGui.QApplication.UnicodeUTF8))

