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
        AllocationWidget.resize(600, 500)
        self.mainLayout = QVBoxLayout(AllocationWidget)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(16, 12, 16, 12)
        self.label = QLabel(AllocationWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.label)

        self.incomeLayout = QHBoxLayout()
        self.incomeLayout.setSpacing(6)
        self.incomeLayout.setObjectName(u"incomeLayout")
        self.label_2 = QLabel(AllocationWidget)
        self.label_2.setObjectName(u"label_2")

        self.incomeLayout.addWidget(self.label_2)

        self.incomeInput = QDoubleSpinBox(AllocationWidget)
        self.incomeInput.setObjectName(u"incomeInput")
        self.incomeInput.setMinimumSize(QSize(120, 0))
        self.incomeInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.incomeLayout.addWidget(self.incomeInput)

        self.currencySelect = QComboBox(AllocationWidget)
        self.currencySelect.setObjectName(u"currencySelect")

        self.incomeLayout.addWidget(self.currencySelect)

        self.incomeCategorySelect = QComboBox(AllocationWidget)
        self.incomeCategorySelect.setObjectName(u"incomeCategorySelect")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.incomeCategorySelect.sizePolicy().hasHeightForWidth())
        self.incomeCategorySelect.setSizePolicy(sizePolicy)

        self.incomeLayout.addWidget(self.incomeCategorySelect)

        self.incomeSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.incomeLayout.addItem(self.incomeSpacer)


        self.mainLayout.addLayout(self.incomeLayout)

        self.groupBox = QGroupBox(AllocationWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBoxLayout = QVBoxLayout(self.groupBox)
        self.groupBoxLayout.setSpacing(6)
        self.groupBoxLayout.setObjectName(u"groupBoxLayout")
        self.targetLayout = QHBoxLayout()
        self.targetLayout.setSpacing(6)
        self.targetLayout.setObjectName(u"targetLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.targetLayout.addWidget(self.label_3)

        self.pocketSelect = QComboBox(self.groupBox)
        self.pocketSelect.setObjectName(u"pocketSelect")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pocketSelect.sizePolicy().hasHeightForWidth())
        self.pocketSelect.setSizePolicy(sizePolicy1)

        self.targetLayout.addWidget(self.pocketSelect)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.targetLayout.addWidget(self.label_9)

        self.goalSelect = QComboBox(self.groupBox)
        self.goalSelect.setObjectName(u"goalSelect")
        sizePolicy1.setHeightForWidth(self.goalSelect.sizePolicy().hasHeightForWidth())
        self.goalSelect.setSizePolicy(sizePolicy1)

        self.targetLayout.addWidget(self.goalSelect)


        self.groupBoxLayout.addLayout(self.targetLayout)

        self.ruleTypeLayout = QHBoxLayout()
        self.ruleTypeLayout.setSpacing(6)
        self.ruleTypeLayout.setObjectName(u"ruleTypeLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.ruleTypeLayout.addWidget(self.label_5)

        self.allocationTypeSelect = QComboBox(self.groupBox)
        self.allocationTypeSelect.setObjectName(u"allocationTypeSelect")

        self.ruleTypeLayout.addWidget(self.allocationTypeSelect)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.ruleTypeLayout.addWidget(self.label_8)

        self.ruleValueInput = QDoubleSpinBox(self.groupBox)
        self.ruleValueInput.setObjectName(u"ruleValueInput")
        self.ruleValueInput.setMinimumSize(QSize(100, 0))
        self.ruleValueInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.ruleTypeLayout.addWidget(self.ruleValueInput)

        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")

        self.ruleTypeLayout.addWidget(self.addButton)

        self.ruleTypeSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ruleTypeLayout.addItem(self.ruleTypeSpacer)


        self.groupBoxLayout.addLayout(self.ruleTypeLayout)

        self.infoLabel = QLabel(self.groupBox)
        self.infoLabel.setObjectName(u"infoLabel")

        self.groupBoxLayout.addWidget(self.infoLabel)


        self.mainLayout.addWidget(self.groupBox)

        self.rulesTable = QTableWidget(AllocationWidget)
        self.rulesTable.setObjectName(u"rulesTable")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.rulesTable.sizePolicy().hasHeightForWidth())
        self.rulesTable.setSizePolicy(sizePolicy2)

        self.mainLayout.addWidget(self.rulesTable)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(6)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.deleteButton = QPushButton(AllocationWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.buttonsLayout.addWidget(self.deleteButton)

        self.editButton = QPushButton(AllocationWidget)
        self.editButton.setObjectName(u"editButton")

        self.buttonsLayout.addWidget(self.editButton)

        self.buttonSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.buttonSpacer1)

        self.upButton = QPushButton(AllocationWidget)
        self.upButton.setObjectName(u"upButton")

        self.buttonsLayout.addWidget(self.upButton)

        self.downButton = QPushButton(AllocationWidget)
        self.downButton.setObjectName(u"downButton")

        self.buttonsLayout.addWidget(self.downButton)

        self.buttonSpacer2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.buttonSpacer2)

        self.allocateButton = QPushButton(AllocationWidget)
        self.allocateButton.setObjectName(u"allocateButton")

        self.buttonsLayout.addWidget(self.allocateButton)


        self.mainLayout.addLayout(self.buttonsLayout)


        self.retranslateUi(AllocationWidget)

        QMetaObject.connectSlotsByName(AllocationWidget)
    # setupUi

    def retranslateUi(self, AllocationWidget):
        AllocationWidget.setWindowTitle(QCoreApplication.translate("AllocationWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("AllocationWidget", u"Allocation", None))
        self.label_2.setText(QCoreApplication.translate("AllocationWidget", u"Income", None))
        self.groupBox.setTitle(QCoreApplication.translate("AllocationWidget", u"New Rule", None))
        self.label_3.setText(QCoreApplication.translate("AllocationWidget", u"Allocate to", None))
        self.label_9.setText(QCoreApplication.translate("AllocationWidget", u"/", None))
        self.label_5.setText(QCoreApplication.translate("AllocationWidget", u"Allocate by", None))
        self.label_8.setText(QCoreApplication.translate("AllocationWidget", u"Value:", None))
        self.addButton.setText(QCoreApplication.translate("AllocationWidget", u"Add Rule", None))
        self.infoLabel.setText("")
        self.deleteButton.setText(QCoreApplication.translate("AllocationWidget", u"Delete", None))
        self.editButton.setText(QCoreApplication.translate("AllocationWidget", u"Edit", None))
        self.upButton.setText(QCoreApplication.translate("AllocationWidget", u"Up", None))
        self.downButton.setText(QCoreApplication.translate("AllocationWidget", u"Down", None))
        self.allocateButton.setText(QCoreApplication.translate("AllocationWidget", u"Allocate", None))
    # retranslateUi

