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
    QDateEdit, QDoubleSpinBox, QGroupBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_GoalsWidget(object):
    def setupUi(self, GoalsWidget):
        if not GoalsWidget.objectName():
            GoalsWidget.setObjectName(u"GoalsWidget")
        GoalsWidget.resize(474, 360)
        self.groupBox = QGroupBox(GoalsWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 10, 421, 151))
        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(310, 100, 100, 32))
        self.pocketSelect = QComboBox(self.groupBox)
        self.pocketSelect.setObjectName(u"pocketSelect")
        self.pocketSelect.setGeometry(QRect(80, 40, 131, 32))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 58, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 101, 16))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 58, 16))
        self.targetDateLabel = QLabel(self.groupBox)
        self.targetDateLabel.setObjectName(u"targetDateLabel")
        self.targetDateLabel.setGeometry(QRect(10, 120, 81, 16))
        self.descriptionInput = QTextEdit(self.groupBox)
        self.descriptionInput.setObjectName(u"descriptionInput")
        self.descriptionInput.setGeometry(QRect(220, 20, 191, 71))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 0, 81, 16))
        self.targetDateInput = QDateEdit(self.groupBox)
        self.targetDateInput.setObjectName(u"targetDateInput")
        self.targetDateInput.setGeometry(QRect(100, 120, 110, 22))
        self.targetDateInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.targetDateInput.setCalendarPopup(True)
        self.targetAmountInput = QDoubleSpinBox(self.groupBox)
        self.targetAmountInput.setObjectName(u"targetAmountInput")
        self.targetAmountInput.setGeometry(QRect(110, 70, 91, 22))
        self.targetAmountInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.nameInput = QLineEdit(self.groupBox)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setGeometry(QRect(70, 10, 131, 21))
        self.setTargetDateInput = QCheckBox(self.groupBox)
        self.setTargetDateInput.setObjectName(u"setTargetDateInput")
        self.setTargetDateInput.setGeometry(QRect(10, 100, 121, 20))
        self.listWidget = QListWidget(GoalsWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 170, 411, 161))
        self.editButton = QPushButton(GoalsWidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(270, 330, 81, 32))
        self.deleteButton = QPushButton(GoalsWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(359, 330, 81, 32))

        self.retranslateUi(GoalsWidget)

        QMetaObject.connectSlotsByName(GoalsWidget)
    # setupUi

    def retranslateUi(self, GoalsWidget):
        GoalsWidget.setWindowTitle(QCoreApplication.translate("GoalsWidget", u"Form", None))
        self.groupBox.setTitle("")
        self.addButton.setText(QCoreApplication.translate("GoalsWidget", u"Add Goal", None))
        self.label.setText(QCoreApplication.translate("GoalsWidget", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("GoalsWidget", u"Target amount", None))
        self.label_3.setText(QCoreApplication.translate("GoalsWidget", u"Pocket", None))
        self.targetDateLabel.setText(QCoreApplication.translate("GoalsWidget", u"Target date", None))
        self.label_5.setText(QCoreApplication.translate("GoalsWidget", u"Description", None))
        self.setTargetDateInput.setText(QCoreApplication.translate("GoalsWidget", u"Set target date", None))
        self.editButton.setText(QCoreApplication.translate("GoalsWidget", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("GoalsWidget", u"Delete", None))
    # retranslateUi

