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
    QDoubleSpinBox, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_GoalContributionsDialog(object):
    def setupUi(self, GoalContributionsDialog):
        if not GoalContributionsDialog.objectName():
            GoalContributionsDialog.setObjectName(u"GoalContributionsDialog")
        GoalContributionsDialog.resize(500, 370)
        self.infoLabel = QLabel(GoalContributionsDialog)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setGeometry(QRect(10, 10, 480, 16))
        self.contributionsList = QListWidget(GoalContributionsDialog)
        self.contributionsList.setObjectName(u"contributionsList")
        self.contributionsList.setGeometry(QRect(10, 34, 480, 160))
        self.removeButton = QPushButton(GoalContributionsDialog)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setGeometry(QRect(380, 202, 110, 30))
        self.groupBox = QGroupBox(GoalContributionsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 242, 480, 88))
        self.label_amount = QLabel(self.groupBox)
        self.label_amount.setObjectName(u"label_amount")
        self.label_amount.setGeometry(QRect(10, 26, 60, 16))
        self.amountInput = QDoubleSpinBox(self.groupBox)
        self.amountInput.setObjectName(u"amountInput")
        self.amountInput.setGeometry(QRect(75, 22, 110, 24))
        self.amountInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.amountInput.setMaximum(1000000000.000000000000000)
        self.amountInput.setDecimals(2)
        self.label_note = QLabel(self.groupBox)
        self.label_note.setObjectName(u"label_note")
        self.label_note.setGeometry(QRect(200, 26, 40, 16))
        self.noteInput = QLineEdit(self.groupBox)
        self.noteInput.setObjectName(u"noteInput")
        self.noteInput.setGeometry(QRect(244, 22, 226, 24))
        self.label_date = QLabel(self.groupBox)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(10, 60, 40, 16))
        self.dateInput = QDateEdit(self.groupBox)
        self.dateInput.setObjectName(u"dateInput")
        self.dateInput.setGeometry(QRect(55, 56, 120, 24))
        self.dateInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateInput.setCalendarPopup(True)
        self.addContributionButton = QPushButton(self.groupBox)
        self.addContributionButton.setObjectName(u"addContributionButton")
        self.addContributionButton.setGeometry(QRect(380, 56, 90, 28))
        self.closeButton = QPushButton(GoalContributionsDialog)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(380, 338, 110, 32))
        self.closeButton.setAutoDefault(False)

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

