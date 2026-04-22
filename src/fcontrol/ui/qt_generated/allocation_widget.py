# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allocation_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AllocationWidget(object):
    def setupUi(self, AllocationWidget):
        if not AllocationWidget.objectName():
            AllocationWidget.setObjectName(u"AllocationWidget")
        AllocationWidget.resize(544, 509)
        self.label = QLabel(AllocationWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 71, 16))
        self.allocateButton = QPushButton(AllocationWidget)
        self.allocateButton.setObjectName(u"allocateButton")
        self.allocateButton.setGeometry(QRect(430, 470, 100, 32))
        self.rulesTable = QTableWidget(AllocationWidget)
        self.rulesTable.setObjectName(u"rulesTable")
        self.rulesTable.setGeometry(QRect(20, 220, 511, 251))
        self.deleteButton = QPushButton(AllocationWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(20, 470, 61, 32))
        self.groupBox = QGroupBox(AllocationWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 80, 511, 131))
        self.groupBox.setFlat(False)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.pocketSelect = QComboBox(self.groupBox)
        self.pocketSelect.setObjectName(u"pocketSelect")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pocketSelect.sizePolicy().hasHeightForWidth())
        self.pocketSelect.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pocketSelect)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.allocationTypeSelect = QComboBox(self.groupBox)
        self.allocationTypeSelect.setObjectName(u"allocationTypeSelect")
        sizePolicy.setHeightForWidth(self.allocationTypeSelect.sizePolicy().hasHeightForWidth())
        self.allocationTypeSelect.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.allocationTypeSelect)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.ruleValueInput = QDoubleSpinBox(self.groupBox)
        self.ruleValueInput.setObjectName(u"ruleValueInput")
        sizePolicy.setHeightForWidth(self.ruleValueInput.sizePolicy().hasHeightForWidth())
        self.ruleValueInput.setSizePolicy(sizePolicy)
        self.ruleValueInput.setMinimumSize(QSize(80, 0))
        self.ruleValueInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.horizontalLayout_4.addWidget(self.ruleValueInput)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setAutoDefault(True)

        self.horizontalLayout_5.addWidget(self.addButton)

        self.layoutWidget = QWidget(AllocationWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 40, 281, 32))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.incomeInput = QDoubleSpinBox(self.layoutWidget)
        self.incomeInput.setObjectName(u"incomeInput")
        self.incomeInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.horizontalLayout.addWidget(self.incomeInput)

        self.currencySelect = QComboBox(self.layoutWidget)
        self.currencySelect.setObjectName(u"currencySelect")

        self.horizontalLayout.addWidget(self.currencySelect)

        self.upButton = QPushButton(AllocationWidget)
        self.upButton.setObjectName(u"upButton")
        self.upButton.setGeometry(QRect(230, 470, 31, 32))
        self.downButton = QPushButton(AllocationWidget)
        self.downButton.setObjectName(u"downButton")
        self.downButton.setGeometry(QRect(270, 470, 51, 32))
        self.editButton = QPushButton(AllocationWidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(90, 470, 61, 32))

        self.retranslateUi(AllocationWidget)

        self.addButton.setDefault(False)


        QMetaObject.connectSlotsByName(AllocationWidget)
    # setupUi

    def retranslateUi(self, AllocationWidget):
        AllocationWidget.setWindowTitle(QCoreApplication.translate("AllocationWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("AllocationWidget", u"Allocation", None))
        self.allocateButton.setText(QCoreApplication.translate("AllocationWidget", u"Allocate", None))
        self.deleteButton.setText(QCoreApplication.translate("AllocationWidget", u"Delete", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("AllocationWidget", u"Allocate to", None))
        self.label_4.setText(QCoreApplication.translate("AllocationWidget", u"pocket.", None))
        self.label_5.setText(QCoreApplication.translate("AllocationWidget", u"Allocate by", None))
        self.label_6.setText(QCoreApplication.translate("AllocationWidget", u".", None))
        self.label_8.setText(QCoreApplication.translate("AllocationWidget", u"Value to allocate:", None))
        self.label_7.setText(QCoreApplication.translate("AllocationWidget", u".", None))
        self.addButton.setText(QCoreApplication.translate("AllocationWidget", u"Add Rule", None))
        self.label_2.setText(QCoreApplication.translate("AllocationWidget", u"Income", None))
        self.upButton.setText(QCoreApplication.translate("AllocationWidget", u"Up", None))
        self.downButton.setText(QCoreApplication.translate("AllocationWidget", u"Down", None))
        self.editButton.setText(QCoreApplication.translate("AllocationWidget", u"Edit", None))
    # retranslateUi

