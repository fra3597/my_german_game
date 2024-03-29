# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verb_paradigm_mode.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VerbParadigmMode(object):
    def setupUi(self, VerbParadigmMode):
        VerbParadigmMode.setObjectName("VerbParadigmMode")
        VerbParadigmMode.resize(994, 775)
        VerbParadigmMode.setStyleSheet("QWidget {\n"
"    background-color: #83A2FF;\n"
"    color: #FFFFFF;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(VerbParadigmMode)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(50, -1, 50, 50)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(VerbParadigmMode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("border-radius: 50%; /* Makes the label circular */\n"
"border: 2px solid #000000; /* Border color and width */\n"
"padding: 10px; /* Adjust padding as needed */\n"
"background-color: #83A2FF;\n"
"color: #FFD28F;\n"
"border: none;\n"
"")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setWordWrap(True)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.paradigm_table = QtWidgets.QTableWidget(VerbParadigmMode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.paradigm_table.sizePolicy().hasHeightForWidth())
        self.paradigm_table.setSizePolicy(sizePolicy)
        self.paradigm_table.setStyleSheet("QTableWidget {\n"
"    font-size: 24px;  /* Set font size for cells */\n"
"    color: white;     /* Set text color for cells */\n"
"    border: 2px solid #000000; /* Border color and width */\n"
"    padding: 10px; /* Adjust padding as needed */\n"
"    background-color: #FFE3BB;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    font-size: 28px;\n"
"    color: white;     /* Set text color for header */\n"
"    background-color: #FFD28F; /* Set background color for header */\n"
"    border: 1px solid #555; /* Set border for header */\n"
"    height: 36px;     /* Set height for each header */\n"
"    width: 260px;\n"
"    font-weight: bold;\n"
"}")
        self.paradigm_table.setRowCount(1)
        self.paradigm_table.setColumnCount(4)
        self.paradigm_table.setObjectName("paradigm_table")
        item = QtWidgets.QTableWidgetItem()
        self.paradigm_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.paradigm_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.paradigm_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.paradigm_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.paradigm_table.setHorizontalHeaderItem(3, item)
        self.paradigm_table.horizontalHeader().setVisible(True)
        self.paradigm_table.horizontalHeader().setDefaultSectionSize(215)
        self.paradigm_table.horizontalHeader().setMinimumSectionSize(24)
        self.paradigm_table.verticalHeader().setVisible(False)
        self.paradigm_table.verticalHeader().setCascadingSectionResizes(False)
        self.paradigm_table.verticalHeader().setDefaultSectionSize(22)
        self.paradigm_table.verticalHeader().setSortIndicatorShown(False)
        self.paradigm_table.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_11.addWidget(self.paradigm_table)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(100, -1, 100, -1)
        self.horizontalLayout_9.setSpacing(100)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, 30, 20, 30)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.character_combo_box = QtWidgets.QComboBox(VerbParadigmMode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.character_combo_box.sizePolicy().hasHeightForWidth())
        self.character_combo_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.character_combo_box.setFont(font)
        self.character_combo_box.setStyleSheet("text-align: center;\n"
"background-color: #2E2E2E;")
        self.character_combo_box.setMaxVisibleItems(7)
        self.character_combo_box.setObjectName("character_combo_box")
        self.character_combo_box.addItem("")
        self.character_combo_box.addItem("")
        self.character_combo_box.addItem("")
        self.character_combo_box.addItem("")
        self.horizontalLayout_4.addWidget(self.character_combo_box)
        self.add_character_button_3 = QtWidgets.QPushButton(VerbParadigmMode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.add_character_button_3.sizePolicy().hasHeightForWidth())
        self.add_character_button_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_character_button_3.setFont(font)
        self.add_character_button_3.setStyleSheet("QPushButton {\n"
"    border-radius: 20px; /* Adjust the radius as needed */\n"
"    background-color: #FFE3BB;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFD28F;\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: #B4BDFF;\n"
"}")
        self.add_character_button_3.setObjectName("add_character_button_3")
        self.horizontalLayout_4.addWidget(self.add_character_button_3)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.stacked_buttons = QtWidgets.QStackedWidget(VerbParadigmMode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.stacked_buttons.sizePolicy().hasHeightForWidth())
        self.stacked_buttons.setSizePolicy(sizePolicy)
        self.stacked_buttons.setObjectName("stacked_buttons")
        self.summary_page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.summary_page.sizePolicy().hasHeightForWidth())
        self.summary_page.setSizePolicy(sizePolicy)
        self.summary_page.setObjectName("summary_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.summary_page)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(40, 20, 40, 20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.go_to_summary_button = QtWidgets.QPushButton(self.summary_page)
        self.go_to_summary_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.go_to_summary_button.sizePolicy().hasHeightForWidth())
        self.go_to_summary_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.go_to_summary_button.setFont(font)
        self.go_to_summary_button.setStyleSheet("QPushButton {\n"
"    border-radius: 20px; /* Adjust the radius as needed */\n"
"    background-color: #FFE3BB;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFD28F;\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: #B4BDFF;\n"
"}")
        self.go_to_summary_button.setObjectName("go_to_summary_button")
        self.horizontalLayout_5.addWidget(self.go_to_summary_button)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.stacked_buttons.addWidget(self.summary_page)
        self.check_page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.check_page.sizePolicy().hasHeightForWidth())
        self.check_page.setSizePolicy(sizePolicy)
        self.check_page.setObjectName("check_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.check_page)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(40, 20, 40, 20)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open_database_button = QtWidgets.QPushButton(self.check_page)
        self.open_database_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.open_database_button.sizePolicy().hasHeightForWidth())
        self.open_database_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.open_database_button.setFont(font)
        self.open_database_button.setStyleSheet("QPushButton {\n"
"    border-radius: 20px; /* Adjust the radius as needed */\n"
"    background-color: #FFE3BB;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFD28F;\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: #B4BDFF;\n"
"}")
        self.open_database_button.setObjectName("open_database_button")
        self.horizontalLayout.addWidget(self.open_database_button)
        self.check_button = QtWidgets.QPushButton(self.check_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.check_button.sizePolicy().hasHeightForWidth())
        self.check_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.check_button.setFont(font)
        self.check_button.setStyleSheet("QPushButton {\n"
"    border-radius: 20px; /* Adjust the radius as needed */\n"
"    background-color: #FFE3BB;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFD28F;\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: #B4BDFF;\n"
"}")
        self.check_button.setObjectName("check_button")
        self.horizontalLayout.addWidget(self.check_button)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.stacked_buttons.addWidget(self.check_page)
        self.horizontalLayout_9.addWidget(self.stacked_buttons)
        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.comparison_result_label = QtWidgets.QLabel(VerbParadigmMode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comparison_result_label.sizePolicy().hasHeightForWidth())
        self.comparison_result_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comparison_result_label.setFont(font)
        self.comparison_result_label.setStyleSheet("border-radius: 50%; /* Makes the label circular */\n"
"border: 2px solid #000000; /* Border color and width */\n"
"padding: 10px; /* Adjust padding as needed */\n"
"background-color: #83A2FF;\n"
"color: #FFD28F;\n"
"border: none;\n"
"")
        self.comparison_result_label.setText("")
        self.comparison_result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.comparison_result_label.setObjectName("comparison_result_label")
        self.verticalLayout.addWidget(self.comparison_result_label)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(VerbParadigmMode)
        self.stacked_buttons.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(VerbParadigmMode)

    def retranslateUi(self, VerbParadigmMode):
        _translate = QtCore.QCoreApplication.translate
        VerbParadigmMode.setWindowTitle(_translate("VerbParadigmMode", "Verb Paradigm Mode"))
        self.title_label.setText(_translate("VerbParadigmMode", "Complete the Verb Paradigm to win the Game"))
        item = self.paradigm_table.verticalHeaderItem(0)
        item.setText(_translate("VerbParadigmMode", "Word to guess"))
        item = self.paradigm_table.horizontalHeaderItem(0)
        item.setText(_translate("VerbParadigmMode", "Present"))
        item = self.paradigm_table.horizontalHeaderItem(1)
        item.setText(_translate("VerbParadigmMode", "Präteritum"))
        item = self.paradigm_table.horizontalHeaderItem(2)
        item.setText(_translate("VerbParadigmMode", "Perfekt"))
        item = self.paradigm_table.horizontalHeaderItem(3)
        item.setText(_translate("VerbParadigmMode", "Italian"))
        self.character_combo_box.setItemText(0, _translate("VerbParadigmMode", "ä"))
        self.character_combo_box.setItemText(1, _translate("VerbParadigmMode", "ü"))
        self.character_combo_box.setItemText(2, _translate("VerbParadigmMode", "ö"))
        self.character_combo_box.setItemText(3, _translate("VerbParadigmMode", "ß"))
        self.add_character_button_3.setText(_translate("VerbParadigmMode", "Add"))
        self.go_to_summary_button.setText(_translate("VerbParadigmMode", "Go to Summary!"))
        self.open_database_button.setText(_translate("VerbParadigmMode", "Open Database"))
        self.check_button.setText(_translate("VerbParadigmMode", "Check!"))
