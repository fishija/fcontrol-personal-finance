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
    QDoubleSpinBox, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_TransactionsWidget(object):
    def setupUi(self, TransactionsWidget):
        if not TransactionsWidget.objectName():
            TransactionsWidget.setObjectName(u"TransactionsWidget")
        TransactionsWidget.resize(700, 500)
        self.mainLayout = QVBoxLayout(TransactionsWidget)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(16, 12, 16, 12)
        self.label = QLabel(TransactionsWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.label)

        self.contentLayout = QHBoxLayout()
        self.contentLayout.setSpacing(16)
        self.contentLayout.setObjectName(u"contentLayout")
        self.categoriesColumn = QVBoxLayout()
        self.categoriesColumn.setSpacing(8)
        self.categoriesColumn.setObjectName(u"categoriesColumn")
        self.label_2 = QLabel(TransactionsWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.categoriesColumn.addWidget(self.label_2)

        self.groupBox = QGroupBox(TransactionsWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.categoryGroupLayout = QVBoxLayout(self.groupBox)
        self.categoryGroupLayout.setSpacing(6)
        self.categoryGroupLayout.setObjectName(u"categoryGroupLayout")
        self.categoryInputLayout = QHBoxLayout()
        self.categoryInputLayout.setSpacing(6)
        self.categoryInputLayout.setObjectName(u"categoryInputLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.categoryInputLayout.addWidget(self.label_3)

        self.categoryNameInput = QLineEdit(self.groupBox)
        self.categoryNameInput.setObjectName(u"categoryNameInput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryNameInput.sizePolicy().hasHeightForWidth())
        self.categoryNameInput.setSizePolicy(sizePolicy)

        self.categoryInputLayout.addWidget(self.categoryNameInput)

        self.addCategoryButton = QPushButton(self.groupBox)
        self.addCategoryButton.setObjectName(u"addCategoryButton")

        self.categoryInputLayout.addWidget(self.addCategoryButton)


        self.categoryGroupLayout.addLayout(self.categoryInputLayout)

        self.infoLabel = QLabel(self.groupBox)
        self.infoLabel.setObjectName(u"infoLabel")

        self.categoryGroupLayout.addWidget(self.infoLabel)


        self.categoriesColumn.addWidget(self.groupBox)

        self.categoriesList = QListWidget(TransactionsWidget)
        self.categoriesList.setObjectName(u"categoriesList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.categoriesList.sizePolicy().hasHeightForWidth())
        self.categoriesList.setSizePolicy(sizePolicy1)

        self.categoriesColumn.addWidget(self.categoriesList)

        self.categoryButtonsLayout = QHBoxLayout()
        self.categoryButtonsLayout.setObjectName(u"categoryButtonsLayout")
        self.catButtonSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.categoryButtonsLayout.addItem(self.catButtonSpacer)

        self.deleteCategoryButton = QPushButton(TransactionsWidget)
        self.deleteCategoryButton.setObjectName(u"deleteCategoryButton")

        self.categoryButtonsLayout.addWidget(self.deleteCategoryButton)


        self.categoriesColumn.addLayout(self.categoryButtonsLayout)


        self.contentLayout.addLayout(self.categoriesColumn)

        self.transactionsColumn = QVBoxLayout()
        self.transactionsColumn.setSpacing(8)
        self.transactionsColumn.setObjectName(u"transactionsColumn")
        self.label_10 = QLabel(TransactionsWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.transactionsColumn.addWidget(self.label_10)

        self.groupBox_2 = QGroupBox(TransactionsWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.transactionGroupLayout = QVBoxLayout(self.groupBox_2)
        self.transactionGroupLayout.setSpacing(6)
        self.transactionGroupLayout.setObjectName(u"transactionGroupLayout")
        self.transRow1 = QHBoxLayout()
        self.transRow1.setSpacing(6)
        self.transRow1.setObjectName(u"transRow1")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.transRow1.addWidget(self.label_4)

        self.transactionAmountInput = QDoubleSpinBox(self.groupBox_2)
        self.transactionAmountInput.setObjectName(u"transactionAmountInput")
        self.transactionAmountInput.setMinimumSize(QSize(80, 0))
        self.transactionAmountInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.transRow1.addWidget(self.transactionAmountInput)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.transRow1.addWidget(self.label_5)

        self.transactionPocketSelect = QComboBox(self.groupBox_2)
        self.transactionPocketSelect.setObjectName(u"transactionPocketSelect")
        sizePolicy.setHeightForWidth(self.transactionPocketSelect.sizePolicy().hasHeightForWidth())
        self.transactionPocketSelect.setSizePolicy(sizePolicy)

        self.transRow1.addWidget(self.transactionPocketSelect)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.transRow1.addWidget(self.label_6)

        self.transactionTypeSelect = QComboBox(self.groupBox_2)
        self.transactionTypeSelect.setObjectName(u"transactionTypeSelect")

        self.transRow1.addWidget(self.transactionTypeSelect)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.transRow1.addWidget(self.label_8)

        self.transactionCategorySelect = QComboBox(self.groupBox_2)
        self.transactionCategorySelect.setObjectName(u"transactionCategorySelect")
        sizePolicy.setHeightForWidth(self.transactionCategorySelect.sizePolicy().hasHeightForWidth())
        self.transactionCategorySelect.setSizePolicy(sizePolicy)

        self.transRow1.addWidget(self.transactionCategorySelect)


        self.transactionGroupLayout.addLayout(self.transRow1)

        self.transRow2 = QHBoxLayout()
        self.transRow2.setSpacing(6)
        self.transRow2.setObjectName(u"transRow2")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.transRow2.addWidget(self.label_7)

        self.transactionDateInput = QDateEdit(self.groupBox_2)
        self.transactionDateInput.setObjectName(u"transactionDateInput")
        self.transactionDateInput.setMinimumSize(QSize(110, 0))

        self.transRow2.addWidget(self.transactionDateInput)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.transRow2.addWidget(self.label_9)

        self.transactionDescriptionInput = QLineEdit(self.groupBox_2)
        self.transactionDescriptionInput.setObjectName(u"transactionDescriptionInput")
        sizePolicy.setHeightForWidth(self.transactionDescriptionInput.sizePolicy().hasHeightForWidth())
        self.transactionDescriptionInput.setSizePolicy(sizePolicy)

        self.transRow2.addWidget(self.transactionDescriptionInput)

        self.addTransactionButton = QPushButton(self.groupBox_2)
        self.addTransactionButton.setObjectName(u"addTransactionButton")

        self.transRow2.addWidget(self.addTransactionButton)


        self.transactionGroupLayout.addLayout(self.transRow2)


        self.transactionsColumn.addWidget(self.groupBox_2)

        self.transactionsList = QListWidget(TransactionsWidget)
        self.transactionsList.setObjectName(u"transactionsList")
        sizePolicy1.setHeightForWidth(self.transactionsList.sizePolicy().hasHeightForWidth())
        self.transactionsList.setSizePolicy(sizePolicy1)

        self.transactionsColumn.addWidget(self.transactionsList)

        self.transButtonsLayout = QHBoxLayout()
        self.transButtonsLayout.setObjectName(u"transButtonsLayout")
        self.transButtonSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.transButtonsLayout.addItem(self.transButtonSpacer)

        self.deleteTransactionButton = QPushButton(TransactionsWidget)
        self.deleteTransactionButton.setObjectName(u"deleteTransactionButton")

        self.transButtonsLayout.addWidget(self.deleteTransactionButton)


        self.transactionsColumn.addLayout(self.transButtonsLayout)


        self.contentLayout.addLayout(self.transactionsColumn)


        self.mainLayout.addLayout(self.contentLayout)


        self.retranslateUi(TransactionsWidget)

        QMetaObject.connectSlotsByName(TransactionsWidget)
    # setupUi

    def retranslateUi(self, TransactionsWidget):
        TransactionsWidget.setWindowTitle(QCoreApplication.translate("TransactionsWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("TransactionsWidget", u"Transactions", None))
        self.label_2.setText(QCoreApplication.translate("TransactionsWidget", u"Categories", None))
        self.groupBox.setTitle(QCoreApplication.translate("TransactionsWidget", u"New Category", None))
        self.label_3.setText(QCoreApplication.translate("TransactionsWidget", u"Name", None))
        self.addCategoryButton.setText(QCoreApplication.translate("TransactionsWidget", u"Add", None))
        self.infoLabel.setText("")
        self.deleteCategoryButton.setText(QCoreApplication.translate("TransactionsWidget", u"Delete", None))
        self.label_10.setText(QCoreApplication.translate("TransactionsWidget", u"History", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TransactionsWidget", u"New Transaction", None))
        self.label_4.setText(QCoreApplication.translate("TransactionsWidget", u"Amount", None))
        self.label_5.setText(QCoreApplication.translate("TransactionsWidget", u"Pocket", None))
        self.label_6.setText(QCoreApplication.translate("TransactionsWidget", u"Type", None))
        self.label_8.setText(QCoreApplication.translate("TransactionsWidget", u"Category", None))
        self.label_7.setText(QCoreApplication.translate("TransactionsWidget", u"Date", None))
        self.label_9.setText(QCoreApplication.translate("TransactionsWidget", u"Description", None))
        self.addTransactionButton.setText(QCoreApplication.translate("TransactionsWidget", u"Add", None))
        self.deleteTransactionButton.setText(QCoreApplication.translate("TransactionsWidget", u"Delete", None))
    # retranslateUi

