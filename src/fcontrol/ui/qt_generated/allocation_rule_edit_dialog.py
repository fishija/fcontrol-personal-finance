# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allocation_rule_edit_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QDoubleSpinBox, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AllocationRuleEditDialog(object):
    def setupUi(self, AllocationRuleEditDialog):
        if not AllocationRuleEditDialog.objectName():
            AllocationRuleEditDialog.setObjectName(u"AllocationRuleEditDialog")
        AllocationRuleEditDialog.resize(395, 298)
        self.saveButton = QPushButton(AllocationRuleEditDialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(280, 250, 100, 32))
        self.cancelButton = QPushButton(AllocationRuleEditDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(170, 250, 100, 32))
        self.groupBox = QGroupBox(AllocationRuleEditDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 70, 371, 131))
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


        self.retranslateUi(AllocationRuleEditDialog)

        self.saveButton.setDefault(True)


        QMetaObject.connectSlotsByName(AllocationRuleEditDialog)
    # setupUi

    def retranslateUi(self, AllocationRuleEditDialog):
        AllocationRuleEditDialog.setWindowTitle(QCoreApplication.translate("AllocationRuleEditDialog", u"Dialog", None))
        self.saveButton.setText(QCoreApplication.translate("AllocationRuleEditDialog", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("AllocationRuleEditDialog", u"Cancel", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("AllocationRuleEditDialog", u"Allocate to", None))
        self.label_4.setText(QCoreApplication.translate("AllocationRuleEditDialog", u"pocket.", None))
        self.label_5.setText(QCoreApplication.translate("AllocationRuleEditDialog", u"Allocate by", None))
        self.label_6.setText(QCoreApplication.translate("AllocationRuleEditDialog", u".", None))
        self.label_8.setText(QCoreApplication.translate("AllocationRuleEditDialog", u"Value to allocate:", None))
        self.label_7.setText(QCoreApplication.translate("AllocationRuleEditDialog", u".", None))
    # retranslateUi

