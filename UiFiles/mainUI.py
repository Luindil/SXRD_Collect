# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Jul  7 22:22:01 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(704, 763)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_9.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(160, 60))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.add_setup_btn = QtGui.QPushButton(Form)
        self.add_setup_btn.setObjectName(_fromUtf8("add_setup_btn"))
        self.horizontalLayout_6.addWidget(self.add_setup_btn)
        self.delete_setup_btn = QtGui.QPushButton(Form)
        self.delete_setup_btn.setObjectName(_fromUtf8("delete_setup_btn"))
        self.horizontalLayout_6.addWidget(self.delete_setup_btn)
        self.clear_setup_btn = QtGui.QPushButton(Form)
        self.clear_setup_btn.setObjectName(_fromUtf8("clear_setup_btn"))
        self.horizontalLayout_6.addWidget(self.clear_setup_btn)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.setup_table = QtGui.QTableWidget(Form)
        self.setup_table.setObjectName(_fromUtf8("setup_table"))
        self.setup_table.setColumnCount(5)
        self.setup_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.setup_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.setup_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.setup_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.setup_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.setup_table.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.setup_table)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.add_sample_btn = QtGui.QPushButton(Form)
        self.add_sample_btn.setObjectName(_fromUtf8("add_sample_btn"))
        self.horizontalLayout.addWidget(self.add_sample_btn)
        self.delete_sample_btn = QtGui.QPushButton(Form)
        self.delete_sample_btn.setObjectName(_fromUtf8("delete_sample_btn"))
        self.horizontalLayout.addWidget(self.delete_sample_btn)
        self.clear_sample_btn = QtGui.QPushButton(Form)
        self.clear_sample_btn.setObjectName(_fromUtf8("clear_sample_btn"))
        self.horizontalLayout.addWidget(self.clear_sample_btn)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.points_table = QtGui.QTableWidget(Form)
        self.points_table.setObjectName(_fromUtf8("points_table"))
        self.points_table.setColumnCount(5)
        self.points_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.points_table.setHorizontalHeaderItem(4, item)
        self.points_table.horizontalHeader().setDefaultSectionSize(80)
        self.verticalLayout.addWidget(self.points_table)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton_12 = QtGui.QPushButton(Form)
        self.pushButton_12.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_12.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.horizontalLayout_4.addWidget(self.pushButton_12)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.add_standard_btn = QtGui.QPushButton(Form)
        self.add_standard_btn.setObjectName(_fromUtf8("add_standard_btn"))
        self.horizontalLayout_2.addWidget(self.add_standard_btn)
        self.delete_standard_btn = QtGui.QPushButton(Form)
        self.delete_standard_btn.setObjectName(_fromUtf8("delete_standard_btn"))
        self.horizontalLayout_2.addWidget(self.delete_standard_btn)
        self.clear_standard_btn = QtGui.QPushButton(Form)
        self.clear_standard_btn.setObjectName(_fromUtf8("clear_standard_btn"))
        self.horizontalLayout_2.addWidget(self.clear_standard_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.standard_table = QtGui.QTableWidget(Form)
        self.standard_table.setObjectName(_fromUtf8("standard_table"))
        self.standard_table.setColumnCount(5)
        self.standard_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.standard_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.standard_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.standard_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.standard_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.standard_table.setHorizontalHeaderItem(4, item)
        self.standard_table.horizontalHeader().setDefaultSectionSize(80)
        self.verticalLayout.addWidget(self.standard_table)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.standard_every_sample_cb = QtGui.QCheckBox(Form)
        self.standard_every_sample_cb.setObjectName(_fromUtf8("standard_every_sample_cb"))
        self.horizontalLayout_5.addWidget(self.standard_every_sample_cb)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.pushButton_11 = QtGui.QPushButton(Form)
        self.pushButton_11.setMinimumSize(QtCore.QSize(130, 60))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalLayout_7.addWidget(self.pushButton_11)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Single Crystal X-ray Diffraction", None))
        self.pushButton.setText(_translate("Form", "EPICS \n"
"Conifguration", None))
        self.label_2.setText(_translate("Form", "Experiment Setup", None))
        self.add_setup_btn.setText(_translate("Form", "Add", None))
        self.delete_setup_btn.setText(_translate("Form", "Delete", None))
        self.clear_setup_btn.setText(_translate("Form", "Clear", None))
        item = self.setup_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Detector", None))
        item = self.setup_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Ω start", None))
        item = self.setup_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Ω end", None))
        item = self.setup_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Step", None))
        item = self.setup_table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Time", None))
        self.label_10.setText(_translate("Form", "Sample Points", None))
        self.add_sample_btn.setText(_translate("Form", "Add", None))
        self.delete_sample_btn.setText(_translate("Form", "Delete", None))
        self.clear_sample_btn.setText(_translate("Form", "Clear", None))
        item = self.points_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Point", None))
        item = self.points_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "x", None))
        item = self.points_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "y", None))
        item = self.points_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "z", None))
        self.pushButton_12.setText(_translate("Form", "-", None))
        self.label_9.setText(_translate("Form", "Standards", None))
        self.add_standard_btn.setText(_translate("Form", "Add", None))
        self.delete_standard_btn.setText(_translate("Form", "Delete", None))
        self.clear_standard_btn.setText(_translate("Form", "Clear", None))
        item = self.standard_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Point", None))
        item = self.standard_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "x", None))
        item = self.standard_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "y", None))
        item = self.standard_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "z", None))
        self.standard_every_sample_cb.setText(_translate("Form", "Every Sample Point", None))
        self.pushButton_11.setText(_translate("Form", "Collect", None))

