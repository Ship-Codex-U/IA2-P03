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
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

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
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.layout_graphic = QVBoxLayout()
        self.layout_graphic.setObjectName(u"layout_graphic")

        self.horizontalLayout_5.addLayout(self.layout_graphic)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(10, 134, 169);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_10.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_10)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_7.addWidget(self.label_11)

        self.output_weight_01 = QTextEdit(self.frame_2)
        self.output_weight_01.setObjectName(u"output_weight_01")
        self.output_weight_01.setMaximumSize(QSize(16777215, 25))
        self.output_weight_01.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.output_weight_01.setTabChangesFocus(True)
        self.output_weight_01.setReadOnly(True)
        self.output_weight_01.setCursorWidth(0)

        self.verticalLayout_7.addWidget(self.output_weight_01)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_8.addWidget(self.label_12)

        self.output_weight_02 = QTextEdit(self.frame_2)
        self.output_weight_02.setObjectName(u"output_weight_02")
        self.output_weight_02.setMaximumSize(QSize(16777215, 25))
        self.output_weight_02.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.output_weight_02.setTabChangesFocus(True)
        self.output_weight_02.setReadOnly(True)
        self.output_weight_02.setCursorWidth(0)

        self.verticalLayout_8.addWidget(self.output_weight_02)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.output_bias = QTextEdit(self.frame_2)
        self.output_bias.setObjectName(u"output_bias")
        self.output_bias.setMaximumSize(QSize(16777215, 25))
        self.output_bias.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.output_bias.setTabChangesFocus(True)
        self.output_bias.setReadOnly(True)
        self.output_bias.setCursorWidth(0)

        self.verticalLayout_9.addWidget(self.output_bias)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_12.addWidget(self.label_14)

        self.input_alpha = QTextEdit(self.frame_2)
        self.input_alpha.setObjectName(u"input_alpha")
        self.input_alpha.setMaximumSize(QSize(16777215, 25))
        self.input_alpha.setStyleSheet(u"				background-color: rgb(236, 243, 244);")
        self.input_alpha.setTabChangesFocus(True)

        self.verticalLayout_12.addWidget(self.input_alpha)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_14.addWidget(self.label_15)

        self.input_iterations = QTextEdit(self.frame_2)
        self.input_iterations.setObjectName(u"input_iterations")
        self.input_iterations.setMaximumSize(QSize(16777215, 25))
        self.input_iterations.setStyleSheet(u"				background-color: rgb(236, 243, 244);")
        self.input_iterations.setTabChangesFocus(True)

        self.verticalLayout_14.addWidget(self.input_iterations)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.button_generate_data_new = QPushButton(self.frame_2)
        self.button_generate_data_new.setObjectName(u"button_generate_data_new")
        self.button_generate_data_new.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setPointSize(8)
        self.button_generate_data_new.setFont(font2)
        self.button_generate_data_new.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.verticalLayout_13.addWidget(self.button_generate_data_new)


        self.horizontalLayout.addLayout(self.verticalLayout_13)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_start = QPushButton(self.frame_2)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setMinimumSize(QSize(0, 35))
        self.button_start.setFont(font2)
        self.button_start.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.verticalLayout_5.addWidget(self.button_start)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.button_clean = QPushButton(self.frame_2)
        self.button_clean.setObjectName(u"button_clean")
        self.button_clean.setMinimumSize(QSize(0, 35))
        self.button_clean.setFont(font2)
        self.button_clean.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.verticalLayout_15.addWidget(self.button_clean)


        self.horizontalLayout.addLayout(self.verticalLayout_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 6)
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_3.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setItalic(True)
        self.label_19.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_19)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 100))
        self.widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(3, 68, 13);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.output_true_positives = QLabel(self.frame_3)
        self.output_true_positives.setObjectName(u"output_true_positives")
        font4 = QFont()
        font4.setBold(True)
        self.output_true_positives.setFont(font4)
        self.output_true_positives.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.output_true_positives)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.output_false_positives = QLabel(self.frame_4)
        self.output_false_positives.setObjectName(u"output_false_positives")
        self.output_false_positives.setFont(font4)
        self.output_false_positives.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.output_false_positives.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.output_false_positives)


        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.output_false_negatives = QLabel(self.frame_5)
        self.output_false_negatives.setObjectName(u"output_false_negatives")
        self.output_false_negatives.setFont(font4)
        self.output_false_negatives.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.output_false_negatives.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.output_false_negatives)


        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(3, 68, 13);")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.output_true_negatives = QLabel(self.frame_6)
        self.output_true_negatives.setObjectName(u"output_true_negatives")
        self.output_true_negatives.setFont(font4)
        self.output_true_negatives.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.output_true_negatives)


        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_16.addWidget(self.label_16)

        self.output_precision = QTextEdit(self.frame_2)
        self.output_precision.setObjectName(u"output_precision")
        self.output_precision.setMaximumSize(QSize(16777215, 25))
        self.output_precision.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.output_precision.setTabChangesFocus(True)
        self.output_precision.setReadOnly(False)
        self.output_precision.setCursorWidth(0)

        self.verticalLayout_16.addWidget(self.output_precision)


        self.horizontalLayout_9.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_17.addWidget(self.label_17)

        self.output_f1_score = QTextEdit(self.frame_2)
        self.output_f1_score.setObjectName(u"output_f1_score")
        self.output_f1_score.setMaximumSize(QSize(16777215, 25))
        self.output_f1_score.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.output_f1_score.setTabChangesFocus(True)
        self.output_f1_score.setReadOnly(True)
        self.output_f1_score.setCursorWidth(0)

        self.verticalLayout_17.addWidget(self.output_f1_score)


        self.horizontalLayout_9.addLayout(self.verticalLayout_17)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Perceptr\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Entrenamiento.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Peso 1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Peso 2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Bias", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Taza Aprendizaje", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Numero Iteraciones", None))
        self.button_generate_data_new.setText(QCoreApplication.translate("MainWindow", u"Nuevos\n"
"Parametros", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"Iniciar \n"
" Entrenamiento", None))
        self.button_clean.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Metricas.", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Matriz de confusi\u00f3n.", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Nota: eje x = valores reales (Yes, No), eje y = valores predecidos (Yes, No)", None))
        self.output_true_positives.setText(QCoreApplication.translate("MainWindow", u"TP", None))
        self.output_false_positives.setText(QCoreApplication.translate("MainWindow", u"FP", None))
        self.output_false_negatives.setText(QCoreApplication.translate("MainWindow", u"FN", None))
        self.output_true_negatives.setText(QCoreApplication.translate("MainWindow", u"TN", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Precisi\u00f3n", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"F1 Score", None))
    # retranslateUi

