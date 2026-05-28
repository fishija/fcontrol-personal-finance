# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(500, 400)
        self.verticalLayout = QVBoxLayout(SettingsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(SettingsWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.verticalLayout.addWidget(self.titleLabel)

        self.currencyGroup = QGroupBox(SettingsWidget)
        self.currencyGroup.setObjectName(u"currencyGroup")
        self.currencyGroupLayout = QVBoxLayout(self.currencyGroup)
        self.currencyGroupLayout.setObjectName(u"currencyGroupLayout")
        self.currencyLayout = QHBoxLayout()
        self.currencyLayout.setObjectName(u"currencyLayout")
        self.currencyLabel = QLabel(self.currencyGroup)
        self.currencyLabel.setObjectName(u"currencyLabel")

        self.currencyLayout.addWidget(self.currencyLabel)

        self.currencySelect = QComboBox(self.currencyGroup)
        self.currencySelect.setObjectName(u"currencySelect")
        self.currencySelect.setMinimumSize(QSize(100, 0))

        self.currencyLayout.addWidget(self.currencySelect)

        self.currencySpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.currencyLayout.addItem(self.currencySpacer)


        self.currencyGroupLayout.addLayout(self.currencyLayout)

        self.warningLabel = QLabel(self.currencyGroup)
        self.warningLabel.setObjectName(u"warningLabel")
        self.warningLabel.setWordWrap(True)
        self.warningLabel.setVisible(False)

        self.currencyGroupLayout.addWidget(self.warningLabel)

        self.saveButton = QPushButton(self.currencyGroup)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)

        self.currencyGroupLayout.addWidget(self.saveButton)


        self.verticalLayout.addWidget(self.currencyGroup)

        self.infoLabel = QLabel(SettingsWidget)
        self.infoLabel.setObjectName(u"infoLabel")

        self.verticalLayout.addWidget(self.infoLabel)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Form", None))
        self.titleLabel.setText(QCoreApplication.translate("SettingsWidget", u"Settings", None))
        self.currencyGroup.setTitle(QCoreApplication.translate("SettingsWidget", u"Default Currency", None))
        self.currencyLabel.setText(QCoreApplication.translate("SettingsWidget", u"Currency:", None))
        self.warningLabel.setText(QCoreApplication.translate("SettingsWidget", u"Changing currency will convert all Net Worth snapshots using historical exchange rates. This may introduce small rounding differences.", None))
        self.warningLabel.setStyleSheet(QCoreApplication.translate("SettingsWidget", u"color: orange;", None))
        self.saveButton.setText(QCoreApplication.translate("SettingsWidget", u"Save", None))
        self.infoLabel.setText("")
    # retranslateUi

