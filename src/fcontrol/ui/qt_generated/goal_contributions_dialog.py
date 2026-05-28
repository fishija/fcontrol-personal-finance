# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'goal_contributions_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QDialog,
    QDoubleSpinBox, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_GoalContributionsDialog(object):
    def setupUi(self, GoalContributionsDialog):
        if not GoalContributionsDialog.objectName():
            GoalContributionsDialog.setObjectName(u"GoalContributionsDialog")
        GoalContributionsDialog.resize(520, 400)
        self.mainLayout = QVBoxLayout(GoalContributionsDialog)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(12, 12, 12, 12)
        self.infoLabel = QLabel(GoalContributionsDialog)
        self.infoLabel.setObjectName(u"infoLabel")

        self.mainLayout.addWidget(self.infoLabel)

        self.contributionsList = QListWidget(GoalContributionsDialog)
        self.contributionsList.setObjectName(u"contributionsList")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.contributionsList.sizePolicy().hasHeightForWidth())
        self.contributionsList.setSizePolicy(sizePolicy)

        self.mainLayout.addWidget(self.contributionsList)

        self.removeLayout = QHBoxLayout()
        self.removeLayout.setObjectName(u"removeLayout")
        self.removeSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.removeLayout.addItem(self.removeSpacer)

        self.removeButton = QPushButton(GoalContributionsDialog)
        self.removeButton.setObjectName(u"removeButton")

        self.removeLayout.addWidget(self.removeButton)


        self.mainLayout.addLayout(self.removeLayout)

        self.groupBox = QGroupBox(GoalContributionsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.addGroupLayout = QVBoxLayout(self.groupBox)
        self.addGroupLayout.setSpacing(6)
        self.addGroupLayout.setObjectName(u"addGroupLayout")
        self.addRow1 = QHBoxLayout()
        self.addRow1.setSpacing(6)
        self.addRow1.setObjectName(u"addRow1")
        self.label_amount = QLabel(self.groupBox)
        self.label_amount.setObjectName(u"label_amount")

        self.addRow1.addWidget(self.label_amount)

        self.amountInput = QDoubleSpinBox(self.groupBox)
        self.amountInput.setObjectName(u"amountInput")
        self.amountInput.setMinimumSize(QSize(100, 0))
        self.amountInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.amountInput.setMaximum(1000000000.000000000000000)
        self.amountInput.setDecimals(2)

        self.addRow1.addWidget(self.amountInput)

        self.label_note = QLabel(self.groupBox)
        self.label_note.setObjectName(u"label_note")

        self.addRow1.addWidget(self.label_note)

        self.noteInput = QLineEdit(self.groupBox)
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
        self.label_date = QLabel(self.groupBox)
        self.label_date.setObjectName(u"label_date")

        self.addRow2.addWidget(self.label_date)

        self.dateInput = QDateEdit(self.groupBox)
        self.dateInput.setObjectName(u"dateInput")
        self.dateInput.setMinimumSize(QSize(110, 0))
        self.dateInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateInput.setCalendarPopup(True)

        self.addRow2.addWidget(self.dateInput)

        self.addRow2Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.addRow2.addItem(self.addRow2Spacer)

        self.addContributionButton = QPushButton(self.groupBox)
        self.addContributionButton.setObjectName(u"addContributionButton")

        self.addRow2.addWidget(self.addContributionButton)


        self.addGroupLayout.addLayout(self.addRow2)


        self.mainLayout.addWidget(self.groupBox)

        self.closeLayout = QHBoxLayout()
        self.closeLayout.setObjectName(u"closeLayout")
        self.closeSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.closeLayout.addItem(self.closeSpacer)

        self.closeButton = QPushButton(GoalContributionsDialog)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setAutoDefault(False)

        self.closeLayout.addWidget(self.closeButton)


        self.mainLayout.addLayout(self.closeLayout)


        self.retranslateUi(GoalContributionsDialog)

        self.addContributionButton.setDefault(True)


        QMetaObject.connectSlotsByName(GoalContributionsDialog)
    # setupUi

    def retranslateUi(self, GoalContributionsDialog):
        GoalContributionsDialog.setWindowTitle(QCoreApplication.translate("GoalContributionsDialog", u"Goal Contributions", None))
        self.infoLabel.setText("")
        self.removeButton.setText(QCoreApplication.translate("GoalContributionsDialog", u"Remove", None))
        self.groupBox.setTitle(QCoreApplication.translate("GoalContributionsDialog", u"Add Contribution", None))
        self.label_amount.setText(QCoreApplication.translate("GoalContributionsDialog", u"Amount:", None))
        self.label_note.setText(QCoreApplication.translate("GoalContributionsDialog", u"Note:", None))
        self.label_date.setText(QCoreApplication.translate("GoalContributionsDialog", u"Date:", None))
        self.addContributionButton.setText(QCoreApplication.translate("GoalContributionsDialog", u"Add", None))
        self.closeButton.setText(QCoreApplication.translate("GoalContributionsDialog", u"Close", None))
    # retranslateUi

