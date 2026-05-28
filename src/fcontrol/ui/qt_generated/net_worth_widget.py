# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'net_worth_widget.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_NetWorthWidget(object):
    def setupUi(self, NetWorthWidget):
        if not NetWorthWidget.objectName():
            NetWorthWidget.setObjectName(u"NetWorthWidget")
        NetWorthWidget.resize(560, 520)
        self.verticalLayout = QVBoxLayout(NetWorthWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.titleLabel = QLabel(NetWorthWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.headerLayout.addWidget(self.titleLabel)

        self.headerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.headerSpacer)

        self.currencyLabel = QLabel(NetWorthWidget)
        self.currencyLabel.setObjectName(u"currencyLabel")

        self.headerLayout.addWidget(self.currencyLabel)

        self.currencySelect = QComboBox(NetWorthWidget)
        self.currencySelect.setObjectName(u"currencySelect")
        self.currencySelect.setMinimumSize(QSize(80, 0))

        self.headerLayout.addWidget(self.currencySelect)


        self.verticalLayout.addLayout(self.headerLayout)

        self.snapshotGroup = QGroupBox(NetWorthWidget)
        self.snapshotGroup.setObjectName(u"snapshotGroup")
        self.snapshotLayout = QHBoxLayout(self.snapshotGroup)
        self.snapshotLayout.setObjectName(u"snapshotLayout")
        self.noteInput = QLineEdit(self.snapshotGroup)
        self.noteInput.setObjectName(u"noteInput")

        self.snapshotLayout.addWidget(self.noteInput)

        self.takeSnapshotButton = QPushButton(self.snapshotGroup)
        self.takeSnapshotButton.setObjectName(u"takeSnapshotButton")

        self.snapshotLayout.addWidget(self.takeSnapshotButton)


        self.verticalLayout.addWidget(self.snapshotGroup)

        self.chartContainer = QWidget(NetWorthWidget)
        self.chartContainer.setObjectName(u"chartContainer")
        self.chartContainer.setMinimumSize(QSize(0, 200))

        self.verticalLayout.addWidget(self.chartContainer)

        self.snapshotsTable = QTableWidget(NetWorthWidget)
        self.snapshotsTable.setObjectName(u"snapshotsTable")
        self.snapshotsTable.setMinimumSize(QSize(0, 150))

        self.verticalLayout.addWidget(self.snapshotsTable)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.infoLabel = QLabel(NetWorthWidget)
        self.infoLabel.setObjectName(u"infoLabel")

        self.buttonsLayout.addWidget(self.infoLabel)

        self.buttonsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.buttonsSpacer)

        self.editButton = QPushButton(NetWorthWidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setEnabled(False)

        self.buttonsLayout.addWidget(self.editButton)

        self.deleteButton = QPushButton(NetWorthWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)

        self.buttonsLayout.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.buttonsLayout)


        self.retranslateUi(NetWorthWidget)

        QMetaObject.connectSlotsByName(NetWorthWidget)
    # setupUi

    def retranslateUi(self, NetWorthWidget):
        NetWorthWidget.setWindowTitle(QCoreApplication.translate("NetWorthWidget", u"Form", None))
        self.titleLabel.setText(QCoreApplication.translate("NetWorthWidget", u"Net Worth", None))
        self.currencyLabel.setText(QCoreApplication.translate("NetWorthWidget", u"Base Currency:", None))
        self.snapshotGroup.setTitle(QCoreApplication.translate("NetWorthWidget", u"Take Snapshot", None))
        self.noteInput.setPlaceholderText(QCoreApplication.translate("NetWorthWidget", u"Note (optional)", None))
        self.takeSnapshotButton.setText(QCoreApplication.translate("NetWorthWidget", u"Take Snapshot", None))
        self.infoLabel.setText("")
        self.editButton.setText(QCoreApplication.translate("NetWorthWidget", u"Edit", None))
        self.deleteButton.setText(QCoreApplication.translate("NetWorthWidget", u"Delete", None))
    # retranslateUi

