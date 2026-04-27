# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transactions_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_TransactionsWidget(object):
    def setupUi(self, TransactionsWidget):
        if not TransactionsWidget.objectName():
            TransactionsWidget.setObjectName(u"TransactionsWidget")
        TransactionsWidget.resize(626, 455)
        self.transactionsList = QListWidget(TransactionsWidget)
        self.transactionsList.setObjectName(u"transactionsList")
        self.transactionsList.setGeometry(QRect(250, 50, 361, 391))
        self.groupBox = QGroupBox(TransactionsWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 50, 221, 71))
        self.nameInput = QLineEdit(self.groupBox)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setGeometry(QRect(10, 30, 131, 21))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 58, 16))
        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(150, 20, 61, 32))
        self.infoLabel = QLabel(self.groupBox)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setGeometry(QRect(10, 50, 191, 16))
        self.label = QLabel(TransactionsWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 20, 131, 16))
        self.label_2 = QLabel(TransactionsWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 20, 91, 16))
        self.categoriesList = QListWidget(TransactionsWidget)
        self.categoriesList.setObjectName(u"categoriesList")
        self.categoriesList.setGeometry(QRect(20, 130, 221, 281))
        self.deleteButton = QPushButton(TransactionsWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(160, 410, 81, 32))

        self.retranslateUi(TransactionsWidget)

        QMetaObject.connectSlotsByName(TransactionsWidget)
    # setupUi

    def retranslateUi(self, TransactionsWidget):
        TransactionsWidget.setWindowTitle(QCoreApplication.translate("TransactionsWidget", u"Form", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("TransactionsWidget", u"Name", None))
        self.addButton.setText(QCoreApplication.translate("TransactionsWidget", u"Add", None))
        self.infoLabel.setText(QCoreApplication.translate("TransactionsWidget", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("TransactionsWidget", u"Transaciton list", None))
        self.label_2.setText(QCoreApplication.translate("TransactionsWidget", u"Categories", None))
        self.deleteButton.setText(QCoreApplication.translate("TransactionsWidget", u"Delete", None))
    # retranslateUi

