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
    QDateEdit, QDialog, QDoubleSpinBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_GoalEditDialog(object):
    def setupUi(self, GoalEditDialog):
        if not GoalEditDialog.objectName():
            GoalEditDialog.setObjectName(u"GoalEditDialog")
        GoalEditDialog.resize(450, 300)
        self.mainLayout = QVBoxLayout(GoalEditDialog)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(12, 12, 12, 12)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(8)
        self.label = QLabel(GoalEditDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.nameInput = QLineEdit(GoalEditDialog)
        self.nameInput.setObjectName(u"nameInput")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameInput)

        self.label_2 = QLabel(GoalEditDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.pocketSelect = QComboBox(GoalEditDialog)
        self.pocketSelect.setObjectName(u"pocketSelect")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.pocketSelect)

        self.label_3 = QLabel(GoalEditDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.targetAmountInput = QDoubleSpinBox(GoalEditDialog)
        self.targetAmountInput.setObjectName(u"targetAmountInput")
        self.targetAmountInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.targetAmountInput.setMaximum(1000000000.000000000000000)
        self.targetAmountInput.setDecimals(2)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.targetAmountInput)

        self.setTargetDateInput = QCheckBox(GoalEditDialog)
        self.setTargetDateInput.setObjectName(u"setTargetDateInput")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.setTargetDateInput)

        self.dateRow = QHBoxLayout()
        self.dateRow.setSpacing(6)
        self.dateRow.setObjectName(u"dateRow")
        self.targetDateLabel = QLabel(GoalEditDialog)
        self.targetDateLabel.setObjectName(u"targetDateLabel")

        self.dateRow.addWidget(self.targetDateLabel)

        self.targetDateInput = QDateEdit(GoalEditDialog)
        self.targetDateInput.setObjectName(u"targetDateInput")
        self.targetDateInput.setMinimumSize(QSize(120, 0))
        self.targetDateInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.targetDateInput.setCalendarPopup(True)

        self.dateRow.addWidget(self.targetDateInput)

        self.dateSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.dateRow.addItem(self.dateSpacer)


        self.formLayout.setLayout(3, QFormLayout.ItemRole.FieldRole, self.dateRow)

        self.label_4 = QLabel(GoalEditDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.descriptionInput = QTextEdit(GoalEditDialog)
        self.descriptionInput.setObjectName(u"descriptionInput")
        self.descriptionInput.setMaximumSize(QSize(16777215, 70))

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.descriptionInput)


        self.mainLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(6)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.btnSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.btnSpacer)

        self.cancelButton = QPushButton(GoalEditDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setAutoDefault(False)

        self.buttonsLayout.addWidget(self.cancelButton)

        self.saveButton = QPushButton(GoalEditDialog)
        self.saveButton.setObjectName(u"saveButton")

        self.buttonsLayout.addWidget(self.saveButton)


        self.mainLayout.addLayout(self.buttonsLayout)


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

