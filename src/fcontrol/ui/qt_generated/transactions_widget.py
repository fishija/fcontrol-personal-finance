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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QSizePolicy,
    QWidget)

class Ui_TransactionsWidget(object):
    def setupUi(self, TransactionsWidget):
        if not TransactionsWidget.objectName():
            TransactionsWidget.setObjectName(u"TransactionsWidget")
        TransactionsWidget.resize(400, 300)
        self.transactionsList = QListWidget(TransactionsWidget)
        self.transactionsList.setObjectName(u"transactionsList")
        self.transactionsList.setGeometry(QRect(20, 10, 361, 281))

        self.retranslateUi(TransactionsWidget)

        QMetaObject.connectSlotsByName(TransactionsWidget)
    # setupUi

    def retranslateUi(self, TransactionsWidget):
        TransactionsWidget.setWindowTitle(QCoreApplication.translate("TransactionsWidget", u"Form", None))
    # retranslateUi

