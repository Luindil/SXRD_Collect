# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Jul 16 13:01:04 2015
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

class Ui_SXRDCollectWidget(object):
    def setupUi(self, SXRDCollectWidget):
        SXRDCollectWidget.setObjectName(_fromUtf8("SXRDCollectWidget"))
        SXRDCollectWidget.resize(702, 793)
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
        self.filepath_txt = QtGui.QLineEdit(self.widget)
        self.filepath_txt.setObjectName(_fromUtf8("filepath_txt"))
        self.gridLayout.addWidget(self.filepath_txt, 1, 1, 1, 1)
        self.filename_txt = QtGui.QLineEdit(self.widget)
        self.filename_txt.setObjectName(_fromUtf8("filename_txt"))
        self.gridLayout.addWidget(self.filename_txt, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
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
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.get_folder_btn = QtGui.QPushButton(self.widget)
        self.get_folder_btn.setMaximumSize(QtCore.QSize(35, 16777215))
        self.get_folder_btn.setObjectName(_fromUtf8("get_folder_btn"))
        self.gridLayout.addWidget(self.get_folder_btn, 1, 2, 1, 1)
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
        self.reset_sample_position_cb = QtGui.QCheckBox(self.widget)
        self.reset_sample_position_cb.setChecked(True)
        self.reset_sample_position_cb.setObjectName(_fromUtf8("reset_sample_position_cb"))
        self.verticalLayout_2.addWidget(self.reset_sample_position_cb)
        self.reset_detector_position_cb = QtGui.QCheckBox(self.widget)
        self.reset_detector_position_cb.setChecked(True)
        self.reset_detector_position_cb.setObjectName(_fromUtf8("reset_detector_position_cb"))
        self.verticalLayout_2.addWidget(self.reset_detector_position_cb)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_5.addWidget(self.widget)
        self.setup_table = QtGui.QTableWidget(SXRDCollectWidget)
        self.setup_table.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.setup_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.setup_table.setObjectName(_fromUtf8("setup_table"))
        self.setup_table.setColumnCount(8)
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
        item = QtGui.QTableWidgetItem()
        self.setup_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.setup_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.setup_table.setHorizontalHeaderItem(7, item)
        self.setup_table.horizontalHeader().setDefaultSectionSize(60)
        self.setup_table.horizontalHeader().setHighlightSections(True)
        self.setup_table.verticalHeader().setVisible(False)
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
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_8 = QtGui.QLabel(SXRDCollectWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(SXRDCollectWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.x_max_txt = QtGui.QLineEdit(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_max_txt.sizePolicy().hasHeightForWidth())
        self.x_max_txt.setSizePolicy(sizePolicy)
        self.x_max_txt.setMaximumSize(QtCore.QSize(50, 16777215))
        self.x_max_txt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_max_txt.setObjectName(_fromUtf8("x_max_txt"))
        self.gridLayout_2.addWidget(self.x_max_txt, 1, 2, 1, 1)
        self.y_step_txt = QtGui.QLineEdit(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_step_txt.sizePolicy().hasHeightForWidth())
        self.y_step_txt.setSizePolicy(sizePolicy)
        self.y_step_txt.setMaximumSize(QtCore.QSize(50, 16777215))
        self.y_step_txt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_step_txt.setObjectName(_fromUtf8("y_step_txt"))
        self.gridLayout_2.addWidget(self.y_step_txt, 2, 3, 1, 1)
        self.y_min_txt = QtGui.QLineEdit(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_min_txt.sizePolicy().hasHeightForWidth())
        self.y_min_txt.setSizePolicy(sizePolicy)
        self.y_min_txt.setMaximumSize(QtCore.QSize(50, 16777215))
        self.y_min_txt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_min_txt.setObjectName(_fromUtf8("y_min_txt"))
        self.gridLayout_2.addWidget(self.y_min_txt, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 3, 1, 1)
        self.x_step_txt = QtGui.QLineEdit(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_step_txt.sizePolicy().hasHeightForWidth())
        self.x_step_txt.setSizePolicy(sizePolicy)
        self.x_step_txt.setMaximumSize(QtCore.QSize(50, 16777215))
        self.x_step_txt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_step_txt.setObjectName(_fromUtf8("x_step_txt"))
        self.gridLayout_2.addWidget(self.x_step_txt, 1, 3, 1, 1)
        self.x_min_txt = QtGui.QLineEdit(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_min_txt.sizePolicy().hasHeightForWidth())
        self.x_min_txt.setSizePolicy(sizePolicy)
        self.x_min_txt.setMaximumSize(QtCore.QSize(50, 16777215))
        self.x_min_txt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_min_txt.setObjectName(_fromUtf8("x_min_txt"))
        self.gridLayout_2.addWidget(self.x_min_txt, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.y_max_txt = QtGui.QLineEdit(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_max_txt.sizePolicy().hasHeightForWidth())
        self.y_max_txt.setSizePolicy(sizePolicy)
        self.y_max_txt.setMaximumSize(QtCore.QSize(50, 16777215))
        self.y_max_txt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_max_txt.setObjectName(_fromUtf8("y_max_txt"))
        self.gridLayout_2.addWidget(self.y_max_txt, 2, 2, 1, 1)
        self.horizontalLayout_11.addLayout(self.gridLayout_2)
        self.create_map_btn = QtGui.QPushButton(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_map_btn.sizePolicy().hasHeightForWidth())
        self.create_map_btn.setSizePolicy(sizePolicy)
        self.create_map_btn.setObjectName(_fromUtf8("create_map_btn"))
        self.horizontalLayout_11.addWidget(self.create_map_btn)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.collect_bkg_btn = QtGui.QPushButton(SXRDCollectWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collect_bkg_btn.sizePolicy().hasHeightForWidth())
        self.collect_bkg_btn.setSizePolicy(sizePolicy)
        self.collect_bkg_btn.setDefault(False)
        self.collect_bkg_btn.setFlat(False)
        self.collect_bkg_btn.setObjectName(_fromUtf8("collect_bkg_btn"))
        self.verticalLayout_3.addWidget(self.collect_bkg_btn)
        self.auto_bkg_cb = QtGui.QCheckBox(SXRDCollectWidget)
        self.auto_bkg_cb.setChecked(True)
        self.auto_bkg_cb.setObjectName(_fromUtf8("auto_bkg_cb"))
        self.verticalLayout_3.addWidget(self.auto_bkg_cb)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.line_3 = QtGui.QFrame(SXRDCollectWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.status_txt = QtGui.QTextEdit(SXRDCollectWidget)
        self.status_txt.setMinimumSize(QtCore.QSize(0, 75))
        self.status_txt.setObjectName(_fromUtf8("status_txt"))
        self.horizontalLayout_7.addWidget(self.status_txt)
        spacerItem6 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.status_lbl = QtGui.QLabel(SXRDCollectWidget)
        self.status_lbl.setText(_fromUtf8(""))
        self.status_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.status_lbl.setObjectName(_fromUtf8("status_lbl"))
        self.verticalLayout_4.addWidget(self.status_lbl)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.collect_btn = QtGui.QPushButton(SXRDCollectWidget)
        self.collect_btn.setMinimumSize(QtCore.QSize(130, 60))
        self.collect_btn.setObjectName(_fromUtf8("collect_btn"))
        self.verticalLayout_4.addWidget(self.collect_btn)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
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
        self.label_3.setText(_translate("SXRDCollectWidget", "Basename:", None))
        self.label.setText(_translate("SXRDCollectWidget", "Point:", None))
        self.point_txt.setText(_translate("SXRDCollectWidget", "1", None))
        self.label_4.setText(_translate("SXRDCollectWidget", "Folder:", None))
        self.get_folder_btn.setText(_translate("SXRDCollectWidget", "Get", None))
        self.example_filename_lbl.setText(_translate("SXRDCollectWidget", "Examplefilename", None))
        self.rename_files_cb.setText(_translate("SXRDCollectWidget", "Rename Files", None))
        self.rename_after_cb.setText(_translate("SXRDCollectWidget", "Reset name after Measurement", None))
        self.reset_sample_position_cb.setText(_translate("SXRDCollectWidget", "Reset Sample Position", None))
        self.reset_detector_position_cb.setText(_translate("SXRDCollectWidget", "Reset Detector Position", None))
        item = self.setup_table.horizontalHeaderItem(0)
        item.setText(_translate("SXRDCollectWidget", "Name", None))
        item = self.setup_table.horizontalHeaderItem(1)
        item.setText(_translate("SXRDCollectWidget", "Det X", None))
        item = self.setup_table.horizontalHeaderItem(2)
        item.setText(_translate("SXRDCollectWidget", "Det Z", None))
        item = self.setup_table.horizontalHeaderItem(3)
        item.setText(_translate("SXRDCollectWidget", "Ω Start", None))
        item = self.setup_table.horizontalHeaderItem(4)
        item.setText(_translate("SXRDCollectWidget", "Ω End", None))
        item = self.setup_table.horizontalHeaderItem(5)
        item.setText(_translate("SXRDCollectWidget", "Ω Step", None))
        item = self.setup_table.horizontalHeaderItem(6)
        item.setText(_translate("SXRDCollectWidget", "Time/step", None))
        item = self.setup_table.horizontalHeaderItem(7)
        item.setText(_translate("SXRDCollectWidget", "Total time", None))
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
        self.label_8.setText(_translate("SXRDCollectWidget", "y", None))
        self.label_2.setText(_translate("SXRDCollectWidget", "x", None))
        self.x_max_txt.setText(_translate("SXRDCollectWidget", "0.01", None))
        self.y_step_txt.setText(_translate("SXRDCollectWidget", "0.005", None))
        self.y_min_txt.setText(_translate("SXRDCollectWidget", "-0.01", None))
        self.label_5.setText(_translate("SXRDCollectWidget", "step", None))
        self.x_step_txt.setText(_translate("SXRDCollectWidget", "0.005", None))
        self.x_min_txt.setText(_translate("SXRDCollectWidget", "-0.01", None))
        self.label_6.setText(_translate("SXRDCollectWidget", "min", None))
        self.label_7.setText(_translate("SXRDCollectWidget", "max", None))
        self.y_max_txt.setText(_translate("SXRDCollectWidget", "0.01", None))
        self.create_map_btn.setText(_translate("SXRDCollectWidget", "Create Map", None))
        self.collect_bkg_btn.setText(_translate("SXRDCollectWidget", "Collect Background", None))
        self.auto_bkg_cb.setText(_translate("SXRDCollectWidget", "automatic", None))
        self.collect_btn.setText(_translate("SXRDCollectWidget", "Collect", None))

