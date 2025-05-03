# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.editName = QLineEdit(self.centralwidget)
        self.editName.setObjectName(u"editName")
        self.editName.setGeometry(QRect(80, 40, 113, 21))
        self.btnName = QPushButton(self.centralwidget)
        self.btnName.setObjectName(u"btnName")
        self.btnName.setGeometry(QRect(250, 40, 75, 24))
        self.lblName = QLabel(self.centralwidget)
        self.lblName.setObjectName(u"lblName")
        self.lblName.setGeometry(QRect(10, 40, 49, 16))
        self.editCreet = QTextEdit(self.centralwidget)
        self.editCreet.setObjectName(u"editCreet")
        self.editCreet.setGeometry(QRect(370, 50, 104, 64))
        self.editCreet.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnName.setText(QCoreApplication.translate("MainWindow", u"\u0422\u044b\u043a!", None))
        self.lblName.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
    # retranslateUi

