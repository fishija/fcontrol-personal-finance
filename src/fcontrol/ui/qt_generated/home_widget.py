# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_HomeWidget(object):
    def setupUi(self, HomeWidget):
        if not HomeWidget.objectName():
            HomeWidget.setObjectName(u"HomeWidget")
        HomeWidget.resize(400, 300)
        self.label = QLabel(HomeWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 120, 60, 16))

        self.retranslateUi(HomeWidget)

        QMetaObject.connectSlotsByName(HomeWidget)
    # setupUi

    def retranslateUi(self, HomeWidget):
        HomeWidget.setWindowTitle(QCoreApplication.translate("HomeWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("HomeWidget", u"Home", None))
    # retranslateUi

