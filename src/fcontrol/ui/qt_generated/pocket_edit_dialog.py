# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pocket_edit_dialog.ui'
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
    QDoubleSpinBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_PocketEditDialog(object):
    def setupUi(self, PocketEditDialog):
        if not PocketEditDialog.objectName():
            PocketEditDialog.setObjectName(u"PocketEditDialog")
        PocketEditDialog.resize(400, 300)
        self.saveButton = QPushButton(PocketEditDialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(290, 250, 100, 32))
        self.cancelButton = QPushButton(PocketEditDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(170, 250, 100, 32))
        self.cancelButton.setAutoDefault(False)
        self.label = QLabel(PocketEditDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 101, 16))
        self.label_2 = QLabel(PocketEditDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 41, 16))
        self.label_3 = QLabel(PocketEditDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 110, 51, 16))
        self.label_4 = QLabel(PocketEditDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 140, 61, 16))
        self.label_5 = QLabel(PocketEditDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 20, 101, 16))
        self.label_6 = QLabel(PocketEditDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(230, 120, 16, 16))
        self.nameInput = QLineEdit(PocketEditDialog)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setGeometry(QRect(260, 70, 113, 21))
        self.balanceInput = QDoubleSpinBox(PocketEditDialog)
        self.balanceInput.setObjectName(u"balanceInput")
        self.balanceInput.setGeometry(QRect(270, 110, 62, 22))
        self.balanceInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.currencySelect = QComboBox(PocketEditDialog)
        self.currencySelect.setObjectName(u"currencySelect")
        self.currencySelect.setGeometry(QRect(260, 130, 103, 32))
        self.currentName = QLabel(PocketEditDialog)
        self.currentName.setObjectName(u"currentName")
        self.currentName.setGeometry(QRect(120, 70, 71, 16))
        self.currentBalance = QLabel(PocketEditDialog)
        self.currentBalance.setObjectName(u"currentBalance")
        self.currentBalance.setGeometry(QRect(120, 110, 81, 16))
        self.currentCurrency = QLabel(PocketEditDialog)
        self.currentCurrency.setObjectName(u"currentCurrency")
        self.currentCurrency.setGeometry(QRect(120, 140, 91, 16))
        self.infoLabel = QLabel(PocketEditDialog)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setGeometry(QRect(30, 190, 341, 16))

        self.retranslateUi(PocketEditDialog)

        self.saveButton.setDefault(True)


        QMetaObject.connectSlotsByName(PocketEditDialog)
    # setupUi

    def retranslateUi(self, PocketEditDialog):
        PocketEditDialog.setWindowTitle(QCoreApplication.translate("PocketEditDialog", u"Dialog", None))
        self.saveButton.setText(QCoreApplication.translate("PocketEditDialog", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("PocketEditDialog", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("PocketEditDialog", u"Current values", None))
        self.label_2.setText(QCoreApplication.translate("PocketEditDialog", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("PocketEditDialog", u"Balance", None))
        self.label_4.setText(QCoreApplication.translate("PocketEditDialog", u"Currency", None))
        self.label_5.setText(QCoreApplication.translate("PocketEditDialog", u"New values", None))
        self.label_6.setText(QCoreApplication.translate("PocketEditDialog", u">", None))
        self.currentName.setText(QCoreApplication.translate("PocketEditDialog", u"curr_name", None))
        self.currentBalance.setText(QCoreApplication.translate("PocketEditDialog", u"curr_balance", None))
        self.currentCurrency.setText(QCoreApplication.translate("PocketEditDialog", u"curr_currency", None))
        self.infoLabel.setText(QCoreApplication.translate("PocketEditDialog", u"TextLabel", None))
    # retranslateUi

