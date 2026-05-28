# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'goals_widget.ui'
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
    QDateEdit, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_GoalsWidget(object):
    def setupUi(self, GoalsWidget):
        if not GoalsWidget.objectName():
            GoalsWidget.setObjectName(u"GoalsWidget")
        GoalsWidget.resize(550, 450)
        self.mainLayout = QVBoxLayout(GoalsWidget)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(16, 12, 16, 12)
        self.groupBox = QGroupBox(GoalsWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBoxLayout = QVBoxLayout(self.groupBox)
        self.groupBoxLayout.setSpacing(6)
        self.groupBoxLayout.setObjectName(u"groupBoxLayout")
        self.row1 = QHBoxLayout()
        self.row1.setSpacing(6)
        self.row1.setObjectName(u"row1")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.row1.addWidget(self.label)

        self.nameInput = QLineEdit(self.groupBox)
        self.nameInput.setObjectName(u"nameInput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameInput.sizePolicy().hasHeightForWidth())
        self.nameInput.setSizePolicy(sizePolicy)

        self.row1.addWidget(self.nameInput)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.row1.addWidget(self.label_3)

        self.pocketSelect = QComboBox(self.groupBox)
        self.pocketSelect.setObjectName(u"pocketSelect")
        sizePolicy.setHeightForWidth(self.pocketSelect.sizePolicy().hasHeightForWidth())
        self.pocketSelect.setSizePolicy(sizePolicy)

        self.row1.addWidget(self.pocketSelect)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.row1.addWidget(self.label_2)

        self.targetAmountInput = QDoubleSpinBox(self.groupBox)
        self.targetAmountInput.setObjectName(u"targetAmountInput")
        self.targetAmountInput.setMinimumSize(QSize(100, 0))
        self.targetAmountInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        self.row1.addWidget(self.targetAmountInput)


        self.groupBoxLayout.addLayout(self.row1)

        self.row2 = QHBoxLayout()
        self.row2.setSpacing(6)
        self.row2.setObjectName(u"row2")
        self.setTargetDateInput = QCheckBox(self.groupBox)
        self.setTargetDateInput.setObjectName(u"setTargetDateInput")

        self.row2.addWidget(self.setTargetDateInput)

        self.targetDateLabel = QLabel(self.groupBox)
        self.targetDateLabel.setObjectName(u"targetDateLabel")

        self.row2.addWidget(self.targetDateLabel)

        self.targetDateInput = QDateEdit(self.groupBox)
        self.targetDateInput.setObjectName(u"targetDateInput")
        self.targetDateInput.setMinimumSize(QSize(110, 0))
        self.targetDateInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.targetDateInput.setCalendarPopup(True)

        self.row2.addWidget(self.targetDateInput)

        self.row2Spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.row2.addItem(self.row2Spacer)

        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")

        self.row2.addWidget(self.addButton)


        self.groupBoxLayout.addLayout(self.row2)

        self.row3 = QHBoxLayout()
        self.row3.setSpacing(6)
        self.row3.setObjectName(u"row3")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.row3.addWidget(self.label_5)

        self.descriptionInput = QTextEdit(self.groupBox)
        self.descriptionInput.setObjectName(u"descriptionInput")
        self.descriptionInput.setMaximumSize(QSize(16777215, 60))

        self.row3.addWidget(self.descriptionInput)


        self.groupBoxLayout.addLayout(self.row3)


        self.mainLayout.addWidget(self.groupBox)

        self.listWidget = QListWidget(GoalsWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)

        self.mainLayout.addWidget(self.listWidget)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(6)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.contributionsButton = QPushButton(GoalsWidget)
        self.contributionsButton.setObjectName(u"contributionsButton")

        self.buttonsLayout.addWidget(self.contributionsButton)

        self.buttonSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.buttonSpacer)

        self.editButton = QPushButton(GoalsWidget)
        self.editButton.setObjectName(u"editButton")

        self.buttonsLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(GoalsWidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.buttonsLayout.addWidget(self.deleteButton)


        self.mainLayout.addLayout(self.buttonsLayout)


        self.retranslateUi(GoalsWidget)

        QMetaObject.connectSlotsByName(GoalsWidget)
    # setupUi

    def retranslateUi(self, GoalsWidget):
        GoalsWidget.setWindowTitle(QCoreApplication.translate("GoalsWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("GoalsWidget", u"New Goal", None))
        self.label.setText(QCoreApplication.translate("GoalsWidget", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("GoalsWidget", u"Pocket", None))
        self.label_2.setText(QCoreApplication.translate("GoalsWidget", u"Target amount", None))
        self.setTargetDateInput.setText(QCoreApplication.translate("GoalsWidget", u"Set target date", None))
        self.targetDateLabel.setText(QCoreApplication.translate("GoalsWidget", u"Target date", None))
        self.addButton.setText(QCoreApplication.translate("GoalsWidget", u"Add Goal", None))
        self.label_5.setText(QCoreApplication.translate("GoalsWidget", u"Description", None))
        self.contributionsButton.setText(QCoreApplication.translate("GoalsWidget", u"Contributions", None))
        self.editButton.setText(QCoreApplication.translate("GoalsWidget", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("GoalsWidget", u"Delete", None))
    # retranslateUi

