# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 642)
        MainWindow.setStyleSheet(u"QTextEdit {\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #45a049;\n"
"border-radius: 7px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, -1, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 200))
        self.frame.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(31, 31, 31);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(10, 134, 169);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label.setMargin(5)

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 15, -1)
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_2.addWidget(self.label_14)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.button_open_signal = QPushButton(self.frame_2)
        self.button_open_signal.setObjectName(u"button_open_signal")
        self.button_open_signal.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setPointSize(8)
        self.button_open_signal.setFont(font1)
        self.button_open_signal.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.gridLayout.addWidget(self.button_open_signal, 0, 1, 1, 1)

        self.button_show_signal = QPushButton(self.frame_2)
        self.button_show_signal.setObjectName(u"button_show_signal")
        self.button_show_signal.setMinimumSize(QSize(0, 35))
        self.button_show_signal.setMaximumSize(QSize(60, 16777215))
        self.button_show_signal.setFont(font1)
        self.button_show_signal.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.gridLayout.addWidget(self.button_show_signal, 0, 2, 1, 1)

        self.button_hide_signal = QPushButton(self.frame_2)
        self.button_hide_signal.setObjectName(u"button_hide_signal")
        self.button_hide_signal.setMinimumSize(QSize(0, 35))
        self.button_hide_signal.setMaximumSize(QSize(60, 16777215))
        self.button_hide_signal.setFont(font1)
        self.button_hide_signal.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.gridLayout.addWidget(self.button_hide_signal, 0, 3, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)

        self.button_open_signal_noisy = QPushButton(self.frame_2)
        self.button_open_signal_noisy.setObjectName(u"button_open_signal_noisy")
        self.button_open_signal_noisy.setMinimumSize(QSize(0, 35))
        self.button_open_signal_noisy.setFont(font1)
        self.button_open_signal_noisy.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.gridLayout.addWidget(self.button_open_signal_noisy, 1, 1, 1, 1)

        self.button_show_signa_noisy = QPushButton(self.frame_2)
        self.button_show_signa_noisy.setObjectName(u"button_show_signa_noisy")
        self.button_show_signa_noisy.setMinimumSize(QSize(0, 35))
        self.button_show_signa_noisy.setMaximumSize(QSize(60, 16777215))
        self.button_show_signa_noisy.setFont(font1)
        self.button_show_signa_noisy.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.gridLayout.addWidget(self.button_show_signa_noisy, 1, 2, 1, 1)

        self.button_hide_signal_noisy = QPushButton(self.frame_2)
        self.button_hide_signal_noisy.setObjectName(u"button_hide_signal_noisy")
        self.button_hide_signal_noisy.setMinimumSize(QSize(0, 35))
        self.button_hide_signal_noisy.setMaximumSize(QSize(60, 16777215))
        self.button_hide_signal_noisy.setFont(font1)
        self.button_hide_signal_noisy.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.gridLayout.addWidget(self.button_hide_signal_noisy, 1, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_3.addWidget(self.label_15)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_start_clean = QPushButton(self.frame_2)
        self.button_start_clean.setObjectName(u"button_start_clean")
        self.button_start_clean.setMinimumSize(QSize(0, 0))
        self.button_start_clean.setFont(font1)
        self.button_start_clean.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.gridLayout_2.addWidget(self.button_start_clean, 1, 0, 1, 1)

        self.button_erase_signal_clean = QPushButton(self.frame_2)
        self.button_erase_signal_clean.setObjectName(u"button_erase_signal_clean")
        self.button_erase_signal_clean.setMinimumSize(QSize(0, 0))
        self.button_erase_signal_clean.setFont(font1)
        self.button_erase_signal_clean.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.gridLayout_2.addWidget(self.button_erase_signal_clean, 1, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_7.addWidget(self.label_11)

        self.input_number_points = QTextEdit(self.frame_2)
        self.input_number_points.setObjectName(u"input_number_points")
        self.input_number_points.setEnabled(True)
        self.input_number_points.setMaximumSize(QSize(16777215, 25))
        self.input_number_points.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.input_number_points.setTabChangesFocus(True)
        self.input_number_points.setReadOnly(False)
        self.input_number_points.setCursorWidth(1)

        self.verticalLayout_7.addWidget(self.input_number_points)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_8.addWidget(self.label_16)

        self.input_alpha = QTextEdit(self.frame_2)
        self.input_alpha.setObjectName(u"input_alpha")
        self.input_alpha.setEnabled(True)
        self.input_alpha.setMaximumSize(QSize(16777215, 25))
        self.input_alpha.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.input_alpha.setTabChangesFocus(True)
        self.input_alpha.setReadOnly(False)
        self.input_alpha.setCursorWidth(1)

        self.verticalLayout_8.addWidget(self.input_alpha)


        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.layout_graphic = QVBoxLayout()
        self.layout_graphic.setObjectName(u"layout_graphic")

        self.verticalLayout_5.addLayout(self.layout_graphic)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 3)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Adaline", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Carga de Se\u00f1ales:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al.", None))
        self.button_open_signal.setText(QCoreApplication.translate("MainWindow", u"Cargar Grafica", None))
        self.button_show_signal.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.button_hide_signal.setText(QCoreApplication.translate("MainWindow", u"Ocultar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al con Ruido.", None))
        self.button_open_signal_noisy.setText(QCoreApplication.translate("MainWindow", u"Cargar Grafica", None))
        self.button_show_signa_noisy.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.button_hide_signal_noisy.setText(QCoreApplication.translate("MainWindow", u"Ocultar", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n de la Limpieza:", None))
        self.button_start_clean.setText(QCoreApplication.translate("MainWindow", u"Iniciar \n"
" Limpieza", None))
        self.button_erase_signal_clean.setText(QCoreApplication.translate("MainWindow", u"Eliminar \n"
" Se\u00f1al Limpiado", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Numero de Puntos a Tomar:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Taza de Aprendizaje", None))
    # retranslateUi

