# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Jul 16 17:58:51 2014
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_SXRDCollectWidget(object):
    def setupUi(self, SXRDCollectWidget):
        SXRDCollectWidget.setObjectName(_fromUtf8("SXRDCollectWidget"))
        SXRDCollectWidget.resize(704, 763)
        SXRDCollectWidget.setStyleSheet(_fromUtf8("#experiment_lbl, #sample_lbl, #standards_lbl {\n"
"    font: italic 20px;\n"
"}\n"
"\n"
"#title_lbl {\n"
"    font: bold 25px;\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(SXRDCollectWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.title_lbl = QtGui.QLabel(SXRDCollectWidget)
        self.title_lbl.setObjectName(_fromUtf8("title_lbl"))
        self.horizontalLayout_9.addWidget(self.title_lbl)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(SXRDCollectWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(160, 60))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.line_8 = QtGui.QFrame(SXRDCollectWidget)
        self.line_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_8.setLineWidth(1)
        self.line_8.setMidLineWidth(0)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout.addWidget(self.line_8)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.experiment_lbl = QtGui.QLabel(SXRDCollectWidget)
        self.experiment_lbl.setObjectName(_fromUtf8("experiment_lbl"))
        self.horizontalLayout_8.addWidget(self.experiment_lbl)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.add_setup_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.add_setup_btn.setObjectName(_fromUtf8("add_setup_btn"))
        self.horizontalLayout_6.addWidget(self.add_setup_btn)
        self.delete_setup_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.delete_setup_btn.setObjectName(_fromUtf8("delete_setup_btn"))
        self.horizontalLayout_6.addWidget(self.delete_setup_btn)
        self.clear_setup_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.clear_setup_btn.setObjectName(_fromUtf8("clear_setup_btn"))
        self.horizontalLayout_6.addWidget(self.clear_setup_btn)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.line_7 = QtGui.QFrame(SXRDCollectWidget)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout.addWidget(self.line_7)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.widget = QtGui.QWidget(SXRDCollectWidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.filename_txt = QtGui.QLineEdit(self.widget)
        self.filename_txt.setObjectName(_fromUtf8("filename_txt"))
        self.gridLayout.addWidget(self.filename_txt, 0, 1, 1, 1)
        self.filepath_txt = QtGui.QLineEdit(self.widget)
        self.filepath_txt.setObjectName(_fromUtf8("filepath_txt"))
        self.gridLayout.addWidget(self.filepath_txt, 1, 1, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.point_txt = QtGui.QLineEdit(self.widget)
        self.point_txt.setMaximumSize(QtCore.QSize(50, 16777215))
        self.point_txt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.point_txt.setObjectName(_fromUtf8("point_txt"))
        self.horizontalLayout_10.addWidget(self.point_txt)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.example_filename_lbl = QtGui.QLabel(self.widget)
        self.example_filename_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.example_filename_lbl.setObjectName(_fromUtf8("example_filename_lbl"))
        self.verticalLayout_2.addWidget(self.example_filename_lbl)
        self.line_4 = QtGui.QFrame(self.widget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.rename_files_cb = QtGui.QCheckBox(self.widget)
        self.rename_files_cb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rename_files_cb.setChecked(True)
        self.rename_files_cb.setObjectName(_fromUtf8("rename_files_cb"))
        self.verticalLayout_2.addWidget(self.rename_files_cb)
        self.rename_after_cb = QtGui.QCheckBox(self.widget)
        self.rename_after_cb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rename_after_cb.setChecked(True)
        self.rename_after_cb.setObjectName(_fromUtf8("rename_after_cb"))
        self.verticalLayout_2.addWidget(self.rename_after_cb)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_5.addWidget(self.widget)
        self.setup_table = QtGui.QTableWidget(SXRDCollectWidget)
        self.setup_table.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.setup_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
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
        self.setup_table.horizontalHeader().setDefaultSectionSize(60)
        self.setup_table.horizontalHeader().setHighlightSections(True)
        self.horizontalLayout_5.addWidget(self.setup_table)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line = QtGui.QFrame(SXRDCollectWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.sample_lbl = QtGui.QLabel(SXRDCollectWidget)
        self.sample_lbl.setObjectName(_fromUtf8("sample_lbl"))
        self.horizontalLayout_3.addWidget(self.sample_lbl)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.add_sample_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.add_sample_btn.setObjectName(_fromUtf8("add_sample_btn"))
        self.horizontalLayout.addWidget(self.add_sample_btn)
        self.delete_sample_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.delete_sample_btn.setObjectName(_fromUtf8("delete_sample_btn"))
        self.horizontalLayout.addWidget(self.delete_sample_btn)
        self.clear_sample_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.clear_sample_btn.setObjectName(_fromUtf8("clear_sample_btn"))
        self.horizontalLayout.addWidget(self.clear_sample_btn)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_5 = QtGui.QFrame(SXRDCollectWidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.sample_points_table = QtGui.QTableWidget(SXRDCollectWidget)
        self.sample_points_table.setStyleSheet(_fromUtf8("QPushButton {\n"
"    height: 18px;\n"
"    border: 1px solid #000;\n"
"    border-radius:2px;\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    margin-left: 7px;\n"
"    margin-top: 7px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: #EEE\n"
"}"))
        self.sample_points_table.setLineWidth(0)
        self.sample_points_table.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.sample_points_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.sample_points_table.setColumnCount(6)
        self.sample_points_table.setObjectName(_fromUtf8("sample_points_table"))
        self.sample_points_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.sample_points_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.sample_points_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.sample_points_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.sample_points_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.sample_points_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.sample_points_table.setHorizontalHeaderItem(5, item)
        self.sample_points_table.horizontalHeader().setDefaultSectionSize(80)
        self.sample_points_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.sample_points_table)
        self.line_2 = QtGui.QFrame(SXRDCollectWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.standard_show_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.standard_show_btn.setMinimumSize(QtCore.QSize(30, 0))
        self.standard_show_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.standard_show_btn.setObjectName(_fromUtf8("standard_show_btn"))
        self.horizontalLayout_4.addWidget(self.standard_show_btn)
        self.standards_lbl = QtGui.QLabel(SXRDCollectWidget)
        self.standards_lbl.setObjectName(_fromUtf8("standards_lbl"))
        self.horizontalLayout_4.addWidget(self.standards_lbl)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.add_standard_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.add_standard_btn.setObjectName(_fromUtf8("add_standard_btn"))
        self.horizontalLayout_2.addWidget(self.add_standard_btn)
        self.delete_standard_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.delete_standard_btn.setObjectName(_fromUtf8("delete_standard_btn"))
        self.horizontalLayout_2.addWidget(self.delete_standard_btn)
        self.clear_standard_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.clear_standard_btn.setObjectName(_fromUtf8("clear_standard_btn"))
        self.horizontalLayout_2.addWidget(self.clear_standard_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_6 = QtGui.QFrame(SXRDCollectWidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout.addWidget(self.line_6)
        self.standard_table = QtGui.QTableWidget(SXRDCollectWidget)
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
        self.standard_footer_2 = QtGui.QWidget(SXRDCollectWidget)
        self.standard_footer_2.setObjectName(_fromUtf8("standard_footer_2"))
        self.standard_footer = QtGui.QHBoxLayout(self.standard_footer_2)
        self.standard_footer.setMargin(0)
        self.standard_footer.setObjectName(_fromUtf8("standard_footer"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.standard_footer.addItem(spacerItem6)
        self.standard_every_sample_cb = QtGui.QCheckBox(self.standard_footer_2)
        self.standard_every_sample_cb.setObjectName(_fromUtf8("standard_every_sample_cb"))
        self.standard_footer.addWidget(self.standard_every_sample_cb)
        self.verticalLayout.addWidget(self.standard_footer_2)
        self.line_3 = QtGui.QFrame(SXRDCollectWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.collect_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.collect_btn.setMinimumSize(QtCore.QSize(130, 60))
        self.collect_btn.setObjectName(_fromUtf8("collect_btn"))
        self.horizontalLayout_7.addWidget(self.collect_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(SXRDCollectWidget)
        QtCore.QMetaObject.connectSlotsByName(SXRDCollectWidget)

    def retranslateUi(self, SXRDCollectWidget):
        SXRDCollectWidget.setWindowTitle(_translate("SXRDCollectWidget", "Form", None))
        self.title_lbl.setText(_translate("SXRDCollectWidget", "Single Crystal X-ray Diffraction", None))
        self.pushButton.setText(_translate("SXRDCollectWidget", "EPICS \n"
"Conifguration", None))
        self.experiment_lbl.setText(_translate("SXRDCollectWidget", "Experiment Setup", None))
        self.add_setup_btn.setText(_translate("SXRDCollectWidget", "Add", None))
        self.delete_setup_btn.setText(_translate("SXRDCollectWidget", "Delete", None))
        self.clear_setup_btn.setText(_translate("SXRDCollectWidget", "Clear", None))
        self.label_4.setText(_translate("SXRDCollectWidget", "Folder:", None))
        self.label_3.setText(_translate("SXRDCollectWidget", "Basename:", None))
        self.point_txt.setText(_translate("SXRDCollectWidget", "1", None))
        self.label.setText(_translate("SXRDCollectWidget", "Point:", None))
        self.example_filename_lbl.setText(_translate("SXRDCollectWidget", "Examplefilename", None))
        self.rename_files_cb.setText(_translate("SXRDCollectWidget", "Rename Files", None))
        self.rename_after_cb.setText(_translate("SXRDCollectWidget", "Reset name after Measurement", None))
        item = self.setup_table.horizontalHeaderItem(0)
        item.setText(_translate("SXRDCollectWidget", "Detector", None))
        item = self.setup_table.horizontalHeaderItem(1)
        item.setText(_translate("SXRDCollectWidget", "Ω Start", None))
        item = self.setup_table.horizontalHeaderItem(2)
        item.setText(_translate("SXRDCollectWidget", "Ω End", None))
        item = self.setup_table.horizontalHeaderItem(3)
        item.setText(_translate("SXRDCollectWidget", "Ω Step", None))
        item = self.setup_table.horizontalHeaderItem(4)
        item.setText(_translate("SXRDCollectWidget", "Time", None))
        self.sample_lbl.setText(_translate("SXRDCollectWidget", "Sample Points", None))
        self.add_sample_btn.setText(_translate("SXRDCollectWidget", "Add", None))
        self.delete_sample_btn.setText(_translate("SXRDCollectWidget", "Delete", None))
        self.clear_sample_btn.setText(_translate("SXRDCollectWidget", "Clear", None))
        item = self.sample_points_table.horizontalHeaderItem(0)
        item.setText(_translate("SXRDCollectWidget", "Point", None))
        item = self.sample_points_table.horizontalHeaderItem(1)
        item.setText(_translate("SXRDCollectWidget", "x", None))
        item = self.sample_points_table.horizontalHeaderItem(2)
        item.setText(_translate("SXRDCollectWidget", "y", None))
        item = self.sample_points_table.horizontalHeaderItem(3)
        item.setText(_translate("SXRDCollectWidget", "z", None))
        self.standard_show_btn.setText(_translate("SXRDCollectWidget", "-", None))
        self.standards_lbl.setText(_translate("SXRDCollectWidget", "Standards", None))
        self.add_standard_btn.setText(_translate("SXRDCollectWidget", "Add", None))
        self.delete_standard_btn.setText(_translate("SXRDCollectWidget", "Delete", None))
        self.clear_standard_btn.setText(_translate("SXRDCollectWidget", "Clear", None))
        item = self.standard_table.horizontalHeaderItem(0)
        item.setText(_translate("SXRDCollectWidget", "Point", None))
        item = self.standard_table.horizontalHeaderItem(1)
        item.setText(_translate("SXRDCollectWidget", "x", None))
        item = self.standard_table.horizontalHeaderItem(2)
        item.setText(_translate("SXRDCollectWidget", "y", None))
        item = self.standard_table.horizontalHeaderItem(3)
        item.setText(_translate("SXRDCollectWidget", "z", None))
        self.standard_every_sample_cb.setText(_translate("SXRDCollectWidget", "Every Sample Point", None))
        self.collect_btn.setText(_translate("SXRDCollectWidget", "Collect", None))

