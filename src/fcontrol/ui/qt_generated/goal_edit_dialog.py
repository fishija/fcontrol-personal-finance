# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'goal_edit_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDialog, QDoubleSpinBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_GoalEditDialog(object):
    def setupUi(self, GoalEditDialog):
        if not GoalEditDialog.objectName():
            GoalEditDialog.setObjectName(u"GoalEditDialog")
        GoalEditDialog.resize(420, 300)
        self.label = QLabel(GoalEditDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 14, 100, 16))
        self.nameInput = QLineEdit(GoalEditDialog)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setGeometry(QRect(120, 10, 280, 24))
        self.label_2 = QLabel(GoalEditDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 100, 16))
        self.pocketSelect = QComboBox(GoalEditDialog)
        self.pocketSelect.setObjectName(u"pocketSelect")
        self.pocketSelect.setGeometry(QRect(120, 46, 280, 28))
        self.label_3 = QLabel(GoalEditDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 92, 100, 16))
        self.targetAmountInput = QDoubleSpinBox(GoalEditDialog)
        self.targetAmountInput.setObjectName(u"targetAmountInput")
        self.targetAmountInput.setGeometry(QRect(120, 88, 130, 24))
        self.targetAmountInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.targetAmountInput.setMaximum(1000000000.000000000000000)
        self.targetAmountInput.setDecimals(2)
        self.setTargetDateInput = QCheckBox(GoalEditDialog)
        self.setTargetDateInput.setObjectName(u"setTargetDateInput")
        self.setTargetDateInput.setGeometry(QRect(10, 128, 140, 20))
        self.targetDateLabel = QLabel(GoalEditDialog)
        self.targetDateLabel.setObjectName(u"targetDateLabel")
        self.targetDateLabel.setGeometry(QRect(158, 130, 70, 16))
        self.targetDateInput = QDateEdit(GoalEditDialog)
        self.targetDateInput.setObjectName(u"targetDateInput")
        self.targetDateInput.setGeometry(QRect(236, 126, 120, 24))
        self.targetDateInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.targetDateInput.setCalendarPopup(True)
        self.label_4 = QLabel(GoalEditDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 164, 100, 16))
        self.descriptionInput = QTextEdit(GoalEditDialog)
        self.descriptionInput.setObjectName(u"descriptionInput")
        self.descriptionInput.setGeometry(QRect(10, 184, 390, 60))
        self.cancelButton = QPushButton(GoalEditDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(200, 258, 100, 32))
        self.cancelButton.setAutoDefault(False)
        self.saveButton = QPushButton(GoalEditDialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(310, 258, 100, 32))

        self.retranslateUi(GoalEditDialog)

        self.saveButton.setDefault(True)


        QMetaObject.connectSlotsByName(GoalEditDialog)
    # setupUi

    def retranslateUi(self, GoalEditDialog):
        GoalEditDialog.setWindowTitle(QCoreApplication.translate("GoalEditDialog", u"Edit Goal", None))
        self.label.setText(QCoreApplication.translate("GoalEditDialog", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("GoalEditDialog", u"Pocket:", None))
        self.label_3.setText(QCoreApplication.translate("GoalEditDialog", u"Target Amount:", None))
        self.setTargetDateInput.setText(QCoreApplication.translate("GoalEditDialog", u"Set Target Date", None))
        self.targetDateLabel.setText(QCoreApplication.translate("GoalEditDialog", u"Target date:", None))
        self.label_4.setText(QCoreApplication.translate("GoalEditDialog", u"Description:", None))
        self.cancelButton.setText(QCoreApplication.translate("GoalEditDialog", u"Cancel", None))
        self.saveButton.setText(QCoreApplication.translate("GoalEditDialog", u"Save", None))
    # retranslateUi

