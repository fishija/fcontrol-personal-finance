# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allocation_widget.ui'
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

class Ui_AllocationWidget(object):
    def setupUi(self, AllocationWidget):
        if not AllocationWidget.objectName():
            AllocationWidget.setObjectName(u"AllocationWidget")
        AllocationWidget.resize(494, 431)
        self.label = QLabel(AllocationWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 110, 60, 16))

        self.retranslateUi(AllocationWidget)

        QMetaObject.connectSlotsByName(AllocationWidget)
    # setupUi

    def retranslateUi(self, AllocationWidget):
        AllocationWidget.setWindowTitle(QCoreApplication.translate("AllocationWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("AllocationWidget", u"Allocate", None))
    # retranslateUi

