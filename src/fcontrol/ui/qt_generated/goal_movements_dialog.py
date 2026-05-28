# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'goal_movements_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QDateEdit,
    QDialog, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_GoalMovementsDialog(object):
    def setupUi(self, GoalMovementsDialog):
        if not GoalMovementsDialog.objectName():
            GoalMovementsDialog.setObjectName(u"GoalMovementsDialog")
        GoalMovementsDialog.resize(560, 480)
        self.mainLayout = QVBoxLayout(GoalMovementsDialog)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(12, 12, 12, 12)
        self.infoLabel = QLabel(GoalMovementsDialog)
        self.infoLabel.setObjectName(u"infoLabel")

        self.mainLayout.addWidget(self.infoLabel)

        self.pocketBalanceLabel = QLabel(GoalMovementsDialog)
        self.pocketBalanceLabel.setObjectName(u"pocketBalanceLabel")

        self.mainLayout.addWidget(self.pocketBalanceLabel)

        self.availableBalanceLabel = QLabel(GoalMovementsDialog)
        self.availableBalanceLabel.setObjectName(u"availableBalanceLabel")

        self.mainLayout.addWidget(self.availableBalanceLabel)

        self.movementsList = QListWidget(GoalMovementsDialog)
        self.movementsList.setObjectName(u"movementsList")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.movementsList.sizePolicy().hasHeightForWidth())
        self.movementsList.setSizePolicy(sizePolicy)
        self.movementsList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.mainLayout.addWidget(self.movementsList)

        self.removeLayout = QHBoxLayout()
        self.removeLayout.setObjectName(u"removeLayout")
        self.removeSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.removeLayout.addItem(self.removeSpacer)

        self.removeButton = QPushButton(GoalMovementsDialog)
        self.removeButton.setObjectName(u"removeButton")

        self.removeLayout.addWidget(self.removeButton)


        self.mainLayout.addLayout(self.removeLayout)

        self.addGroupBox = QGroupBox(GoalMovementsDialog)
        self.addGroupBox.setObjectName(u"addGroupBox")
        self.addGroupLayout = QVBoxLayout(self.addGroupBox)
        self.addGroupLayout.setSpacing(6)
        self.addGroupLayout.setObjectName(u"addGroupLayout")
        self.typeRow = QHBoxLayout()
        self.typeRow.setSpacing(6)
        self.typeRow.setObjectName(u"typeRow")
        self.label_type = QLabel(self.addGroupBox)
        self.label_type.setObjectName(u"label_type")

        self.typeRow.addWidget(self.label_type)

        self.contributionRadio = QRadioButton(self.addGroupBox)
        self.contributionRadio.setObjectName(u"contributionRadio")
        self.contributionRadio.setChecked(True)

        self.typeRow.addWidget(self.contributionRadio)

        self.withdrawalRadio = QRadioButton(self.addGroupBox)
        self.withdrawalRadio.setObjectName(u"withdrawalRadio")

        self.typeRow.addWidget(self.withdrawalRadio)

        self.typeRowSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.typeRow.addItem(self.typeRowSpacer)


        self.addGroupLayout.addLayout(self.typeRow)

        self.addRow1 = QHBoxLayout()
        self.addRow1.setSpacing(6)
        self.addRow1.setObjectName(u"addRow1")
        self.label_amount = QLabel(self.addGroupBox)
        self.label_amount.setObjectName(u"label_amount")

        self.addRow1.addWidget(self.label_amount)

        self.amountInput = QDoubleSpinBox(self.addGroupBox)
        self.amountInput.setObjectName(u"amountInput")
        self.amountInput.setMinimumSize(QSize(100, 0))
        self.amountInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.amountInput.setMaximum(1000000000.000000000000000)
        self.amountInput.setDecimals(2)

        self.addRow1.addWidget(self.amountInput)

        self.label_note = QLabel(self.addGroupBox)
        self.label_note.setObjectName(u"label_note")

        self.addRow1.addWidget(self.label_note)

        self.noteInput = QLineEdit(self.addGroupBox)
        self.noteInput.setObjectName(u"noteInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.noteInput.sizePolicy().hasHeightForWidth())
        self.noteInput.setSizePolicy(sizePolicy1)

        self.addRow1.addWidget(self.noteInput)


        self.addGroupLayout.addLayout(self.addRow1)

        self.addRow2 = QHBoxLayout()
        self.addRow2.setSpacing(6)
        self.addRow2.setObjectName(u"addRow2")
        self.label_date = QLabel(self.addGroupBox)
        self.label_date.setObjectName(u"label_date")

        self.addRow2.addWidget(self.label_date)

        self.dateInput = QDateEdit(self.addGroupBox)
        self.dateInput.setObjectName(u"dateInput")
        self.dateInput.setMinimumSize(QSize(110, 0))
        self.dateInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateInput.setCalendarPopup(True)

        self.addRow2.addWidget(self.dateInput)

        self.addRow2Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.addRow2.addItem(self.addRow2Spacer)

        self.addButton = QPushButton(self.addGroupBox)
        self.addButton.setObjectName(u"addButton")

        self.addRow2.addWidget(self.addButton)


        self.addGroupLayout.addLayout(self.addRow2)


        self.mainLayout.addWidget(self.addGroupBox)

        self.closeLayout = QHBoxLayout()
        self.closeLayout.setObjectName(u"closeLayout")
        self.closeSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.closeLayout.addItem(self.closeSpacer)

        self.closeButton = QPushButton(GoalMovementsDialog)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setAutoDefault(False)

        self.closeLayout.addWidget(self.closeButton)


        self.mainLayout.addLayout(self.closeLayout)


        self.retranslateUi(GoalMovementsDialog)

        self.addButton.setDefault(True)


        QMetaObject.connectSlotsByName(GoalMovementsDialog)
    # setupUi

    def retranslateUi(self, GoalMovementsDialog):
        GoalMovementsDialog.setWindowTitle(QCoreApplication.translate("GoalMovementsDialog", u"Goal Movements", None))
        self.infoLabel.setText("")
        self.pocketBalanceLabel.setText("")
        self.availableBalanceLabel.setText("")
        self.removeButton.setText(QCoreApplication.translate("GoalMovementsDialog", u"Remove", None))
        self.addGroupBox.setTitle(QCoreApplication.translate("GoalMovementsDialog", u"Add Movement", None))
        self.label_type.setText(QCoreApplication.translate("GoalMovementsDialog", u"Type:", None))
        self.contributionRadio.setText(QCoreApplication.translate("GoalMovementsDialog", u"Contribution", None))
        self.withdrawalRadio.setText(QCoreApplication.translate("GoalMovementsDialog", u"Withdrawal", None))
        self.label_amount.setText(QCoreApplication.translate("GoalMovementsDialog", u"Amount:", None))
        self.label_note.setText(QCoreApplication.translate("GoalMovementsDialog", u"Note:", None))
        self.label_date.setText(QCoreApplication.translate("GoalMovementsDialog", u"Date:", None))
        self.addButton.setText(QCoreApplication.translate("GoalMovementsDialog", u"Add", None))
        self.closeButton.setText(QCoreApplication.translate("GoalMovementsDialog", u"Close", None))
    # retranslateUi

