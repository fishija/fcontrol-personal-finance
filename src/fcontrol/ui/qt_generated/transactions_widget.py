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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDoubleSpinBox, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_TransactionsWidget(object):
    def setupUi(self, TransactionsWidget):
        if not TransactionsWidget.objectName():
            TransactionsWidget.setObjectName(u"TransactionsWidget")
        TransactionsWidget.resize(673, 446)
        self.transactionsList = QListWidget(TransactionsWidget)
        self.transactionsList.setObjectName(u"transactionsList")
        self.transactionsList.setGeometry(QRect(250, 220, 411, 191))
        self.groupBox = QGroupBox(TransactionsWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 50, 221, 81))
        self.categoryNameInput = QLineEdit(self.groupBox)
        self.categoryNameInput.setObjectName(u"categoryNameInput")
        self.categoryNameInput.setGeometry(QRect(10, 30, 131, 21))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 58, 16))
        self.addCategoryButton = QPushButton(self.groupBox)
        self.addCategoryButton.setObjectName(u"addCategoryButton")
        self.addCategoryButton.setGeometry(QRect(150, 20, 61, 32))
        self.infoLabel = QLabel(self.groupBox)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setGeometry(QRect(10, 60, 191, 16))
        self.label = QLabel(TransactionsWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 20, 101, 16))
        self.label_2 = QLabel(TransactionsWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 20, 91, 16))
        self.categoriesList = QListWidget(TransactionsWidget)
        self.categoriesList.setObjectName(u"categoriesList")
        self.categoriesList.setGeometry(QRect(20, 140, 221, 271))
        self.deleteCategoryButton = QPushButton(TransactionsWidget)
        self.deleteCategoryButton.setObjectName(u"deleteCategoryButton")
        self.deleteCategoryButton.setGeometry(QRect(160, 410, 81, 32))
        self.groupBox_2 = QGroupBox(TransactionsWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(250, 50, 411, 161))
        self.transactionAmountInput = QDoubleSpinBox(self.groupBox_2)
        self.transactionAmountInput.setObjectName(u"transactionAmountInput")
        self.transactionAmountInput.setGeometry(QRect(10, 30, 62, 22))
        self.transactionAmountInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 58, 16))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 10, 58, 16))
        self.transactionPocketSelect = QComboBox(self.groupBox_2)
        self.transactionPocketSelect.setObjectName(u"transactionPocketSelect")
        self.transactionPocketSelect.setGeometry(QRect(80, 30, 103, 32))
        self.transactionTypeSelect = QComboBox(self.groupBox_2)
        self.transactionTypeSelect.setObjectName(u"transactionTypeSelect")
        self.transactionTypeSelect.setGeometry(QRect(190, 30, 103, 32))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 10, 58, 16))
        self.transactionDateInput = QDateEdit(self.groupBox_2)
        self.transactionDateInput.setObjectName(u"transactionDateInput")
        self.transactionDateInput.setGeometry(QRect(10, 90, 110, 22))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 70, 58, 16))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 10, 58, 16))
        self.transactionCategorySelect = QComboBox(self.groupBox_2)
        self.transactionCategorySelect.setObjectName(u"transactionCategorySelect")
        self.transactionCategorySelect.setGeometry(QRect(290, 30, 121, 32))
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 70, 81, 16))
        self.transactionDescriptionInput = QLineEdit(self.groupBox_2)
        self.transactionDescriptionInput.setObjectName(u"transactionDescriptionInput")
        self.transactionDescriptionInput.setGeometry(QRect(130, 90, 271, 21))
        self.addTransactionButton = QPushButton(self.groupBox_2)
        self.addTransactionButton.setObjectName(u"addTransactionButton")
        self.addTransactionButton.setGeometry(QRect(330, 120, 61, 32))
        self.deleteTransactionButton = QPushButton(TransactionsWidget)
        self.deleteTransactionButton.setObjectName(u"deleteTransactionButton")
        self.deleteTransactionButton.setGeometry(QRect(580, 410, 81, 32))

        self.retranslateUi(TransactionsWidget)

        QMetaObject.connectSlotsByName(TransactionsWidget)
    # setupUi

    def retranslateUi(self, TransactionsWidget):
        TransactionsWidget.setWindowTitle(QCoreApplication.translate("TransactionsWidget", u"Form", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("TransactionsWidget", u"Name", None))
        self.addCategoryButton.setText(QCoreApplication.translate("TransactionsWidget", u"Add", None))
        self.infoLabel.setText(QCoreApplication.translate("TransactionsWidget", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("TransactionsWidget", u"Transactions", None))
        self.label_2.setText(QCoreApplication.translate("TransactionsWidget", u"Categories", None))
        self.deleteCategoryButton.setText(QCoreApplication.translate("TransactionsWidget", u"Delete", None))
        self.groupBox_2.setTitle("")
        self.label_4.setText(QCoreApplication.translate("TransactionsWidget", u"Amount", None))
        self.label_5.setText(QCoreApplication.translate("TransactionsWidget", u"Pocket", None))
        self.label_6.setText(QCoreApplication.translate("TransactionsWidget", u"Type", None))
        self.label_7.setText(QCoreApplication.translate("TransactionsWidget", u"Date", None))
        self.label_8.setText(QCoreApplication.translate("TransactionsWidget", u"Category", None))
        self.label_9.setText(QCoreApplication.translate("TransactionsWidget", u"Description:", None))
        self.addTransactionButton.setText(QCoreApplication.translate("TransactionsWidget", u"Add", None))
        self.deleteTransactionButton.setText(QCoreApplication.translate("TransactionsWidget", u"Delete", None))
    # retranslateUi

