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
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_PocketsWidget(object):
    def setupUi(self, PocketsWidget):
        if not PocketsWidget.objectName():
            PocketsWidget.setObjectName(u"PocketsWidget")
        PocketsWidget.resize(550, 480)
        self.mainLayout = QVBoxLayout(PocketsWidget)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(16, 12, 16, 12)
        self.label = QLabel(PocketsWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.label)

        self.groupBox = QGroupBox(PocketsWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBoxLayout = QVBoxLayout(self.groupBox)
        self.groupBoxLayout.setSpacing(6)
        self.groupBoxLayout.setObjectName(u"groupBoxLayout")
        self.nameRow = QHBoxLayout()
        self.nameRow.setSpacing(6)
        self.nameRow.setObjectName(u"nameRow")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.nameRow.addWidget(self.label_2)

        self.nameInput = QLineEdit(self.groupBox)
        self.nameInput.setObjectName(u"nameInput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameInput.sizePolicy().hasHeightForWidth())
        self.nameInput.setSizePolicy(sizePolicy)

        self.nameRow.addWidget(self.nameInput)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.nameRow.addWidget(self.label_3)

        self.balanceInput = QDoubleSpinBox(self.groupBox)
        self.balanceInput.setObjectName(u"balanceInput")
        self.balanceInput.setMinimumSize(QSize(100, 0))
        self.balanceInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.nameRow.addWidget(self.balanceInput)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.nameRow.addWidget(self.label_4)

        self.currencySelect = QComboBox(self.groupBox)
        self.currencySelect.setObjectName(u"currencySelect")

        self.nameRow.addWidget(self.currencySelect)

        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")

        self.nameRow.addWidget(self.addButton)


        self.groupBoxLayout.addLayout(self.nameRow)

        self.infoLabel = QLabel(self.groupBox)
        self.infoLabel.setObjectName(u"infoLabel")

        self.groupBoxLayout.addWidget(self.infoLabel)


        self.mainLayout.addWidget(self.groupBox)

        self.pocketsTable = QTableWidget(PocketsWidget)
        self.pocketsTable.setObjectName(u"pocketsTable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.pocketsTable.sizePolicy().hasHeightForWidth())
        self.pocketsTable.setSizePolicy(sizePolicy1)

        self.mainLayout.addWidget(self.pocketsTable)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(6)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.buttonSpacer)

        self.editButton = QPushButton(PocketsWidget)
        self.editButton.setObjectName(u"editButton")

        self.buttonsLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(PocketsWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.buttonsLayout.addWidget(self.deleteButton)


        self.mainLayout.addLayout(self.buttonsLayout)


        self.retranslateUi(PocketsWidget)

        QMetaObject.connectSlotsByName(PocketsWidget)
    # setupUi

    def retranslateUi(self, PocketsWidget):
        PocketsWidget.setWindowTitle(QCoreApplication.translate("PocketsWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("PocketsWidget", u"Pockets", None))
        self.groupBox.setTitle(QCoreApplication.translate("PocketsWidget", u"New Pocket", None))
        self.label_2.setText(QCoreApplication.translate("PocketsWidget", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("PocketsWidget", u"Balance", None))
        self.label_4.setText(QCoreApplication.translate("PocketsWidget", u"Currency", None))
        self.addButton.setText(QCoreApplication.translate("PocketsWidget", u"Add Pocket", None))
        self.infoLabel.setText("")
        self.editButton.setText(QCoreApplication.translate("PocketsWidget", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("PocketsWidget", u"Delete", None))
    # retranslateUi

