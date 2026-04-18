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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_PocketsWidget(object):
    def setupUi(self, PocketsWidget):
        if not PocketsWidget.objectName():
            PocketsWidget.setObjectName(u"PocketsWidget")
        PocketsWidget.resize(499, 444)
        self.label = QLabel(PocketsWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 170, 60, 16))

        self.retranslateUi(PocketsWidget)

        QMetaObject.connectSlotsByName(PocketsWidget)
    # setupUi

    def retranslateUi(self, PocketsWidget):
        PocketsWidget.setWindowTitle(QCoreApplication.translate("PocketsWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("PocketsWidget", u"Pockets", None))
    # retranslateUi

