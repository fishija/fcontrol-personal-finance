# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pockets_widget.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_PocketsWidget(object):
    def setupUi(self, PocketsWidget):
        if not PocketsWidget.objectName():
            PocketsWidget.setObjectName(u"PocketsWidget")
        PocketsWidget.resize(488, 483)
        self.label = QLabel(PocketsWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 60, 16))
        self.label_2 = QLabel(PocketsWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 70, 58, 16))
        self.label_3 = QLabel(PocketsWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 100, 58, 16))
        self.label_4 = QLabel(PocketsWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 130, 61, 16))
        self.currencySelect = QComboBox(PocketsWidget)
        self.currencySelect.setObjectName(u"currencySelect")
        self.currencySelect.setGeometry(QRect(180, 120, 81, 32))
        self.nameInput = QLineEdit(PocketsWidget)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setGeometry(QRect(192, 70, 111, 21))
        self.balanceInput = QDoubleSpinBox(PocketsWidget)
        self.balanceInput.setObjectName(u"balanceInput")
        self.balanceInput.setGeometry(QRect(190, 100, 91, 22))
        self.balanceInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.addButton = QPushButton(PocketsWidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(320, 140, 100, 32))
        self.deleteButton = QPushButton(PocketsWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(359, 420, 81, 32))
        self.pocketsTable = QTableWidget(PocketsWidget)
        self.pocketsTable.setObjectName(u"pocketsTable")
        self.pocketsTable.setGeometry(QRect(40, 190, 401, 231))
        self.editButton = QPushButton(PocketsWidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(270, 420, 81, 32))

        self.retranslateUi(PocketsWidget)

        QMetaObject.connectSlotsByName(PocketsWidget)
    # setupUi

    def retranslateUi(self, PocketsWidget):
        PocketsWidget.setWindowTitle(QCoreApplication.translate("PocketsWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("PocketsWidget", u"Pockets", None))
        self.label_2.setText(QCoreApplication.translate("PocketsWidget", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("PocketsWidget", u"Balance", None))
        self.label_4.setText(QCoreApplication.translate("PocketsWidget", u"Currency", None))
        self.addButton.setText(QCoreApplication.translate("PocketsWidget", u"Add Pocket", None))
        self.deleteButton.setText(QCoreApplication.translate("PocketsWidget", u"Delete", None))
        self.editButton.setText(QCoreApplication.translate("PocketsWidget", u"Edit", None))
    # retranslateUi

