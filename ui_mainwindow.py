# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(734, 521)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionOrdenar_por_ID = QAction(MainWindow)
        self.actionOrdenar_por_ID.setObjectName(u"actionOrdenar_por_ID")
        self.actionOrdenar_por_velocidad = QAction(MainWindow)
        self.actionOrdenar_por_velocidad.setObjectName(u"actionOrdenar_por_velocidad")
        self.actionOrdenar_por_distancia = QAction(MainWindow)
        self.actionOrdenar_por_distancia.setObjectName(u"actionOrdenar_por_distancia")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 210, 22, 16))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 23, 16, 16))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 141, 45, 16))
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 270, 20, 16))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 180, 52, 16))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 117, 60, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 47, 56, 16))
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 240, 28, 16))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 70, 56, 16))
        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")
        self.agregar_inicio_pushButton.setGeometry(QRect(10, 310, 307, 21))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 94, 60, 16))
        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")
        self.agregar_final_pushButton.setGeometry(QRect(10, 339, 307, 21))
        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")
        self.mostrar_pushButton.setGeometry(QRect(10, 363, 307, 21))
        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setGeometry(QRect(76, 23, 241, 18))
        self.id_spinBox.setProperty("showGroupSeparator", False)
        self.id_spinBox.setMaximum(500)
        self.origen_x_spinBox = QSpinBox(self.groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setGeometry(QRect(76, 47, 241, 17))
        self.origen_x_spinBox.setMaximum(500)
        self.origen_y_spinBox = QSpinBox(self.groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setGeometry(QRect(76, 70, 241, 18))
        self.origen_y_spinBox.setMaximum(500)
        self.destino_x_spinBox = QSpinBox(self.groupBox)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setGeometry(QRect(76, 94, 241, 17))
        self.destino_x_spinBox.setMaximum(500)
        self.destino_y_spinBox = QSpinBox(self.groupBox)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setGeometry(QRect(76, 117, 241, 18))
        self.destino_y_spinBox.setMaximum(500)
        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setGeometry(QRect(76, 141, 241, 17))
        self.velocidad_spinBox.setMaximum(500)
        self.rojo_spinBox = QSpinBox(self.groupBox)
        self.rojo_spinBox.setObjectName(u"rojo_spinBox")
        self.rojo_spinBox.setGeometry(QRect(70, 210, 241, 18))
        self.rojo_spinBox.setMaximum(225)
        self.verde_spinBox = QSpinBox(self.groupBox)
        self.verde_spinBox.setObjectName(u"verde_spinBox")
        self.verde_spinBox.setGeometry(QRect(70, 240, 241, 17))
        self.verde_spinBox.setMaximum(225)
        self.azul_spinBox = QSpinBox(self.groupBox)
        self.azul_spinBox.setObjectName(u"azul_spinBox")
        self.azul_spinBox.setGeometry(QRect(70, 270, 241, 18))
        self.azul_spinBox.setMaximum(225)
        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(340, 20, 311, 361))

        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buscar_spinBox = QSpinBox(self.tab_2)
        self.buscar_spinBox.setObjectName(u"buscar_spinBox")
        self.buscar_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.buscar_spinBox, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setMidLineWidth(0)

        self.gridLayout.addWidget(self.tabla, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_2.addWidget(self.dibujar, 1, 0, 1, 1)

        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_2.addWidget(self.limpiar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 734, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuOrdenar = QMenu(self.menubar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        self.menuCrear = QMenu(self.menubar)
        self.menuCrear.setObjectName(u"menuCrear")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOrdenar.menuAction())
        self.menubar.addAction(self.menuCrear.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuOrdenar.addAction(self.actionOrdenar_por_ID)
        self.menuOrdenar.addAction(self.actionOrdenar_por_velocidad)
        self.menuOrdenar.addAction(self.actionOrdenar_por_distancia)
        self.menuCrear.addAction(self.actionGrafo)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionOrdenar_por_ID.setText(QCoreApplication.translate("MainWindow", u"Ordenar por ID", None))
#if QT_CONFIG(shortcut)
        self.actionOrdenar_por_ID.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionOrdenar_por_velocidad.setText(QCoreApplication.translate("MainWindow", u"Ordenar por velocidad", None))
#if QT_CONFIG(shortcut)
        self.actionOrdenar_por_velocidad.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionOrdenar_por_distancia.setText(QCoreApplication.translate("MainWindow", u"Ordenar por distancia", None))
#if QT_CONFIG(shortcut)
        self.actionOrdenar_por_distancia.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
#if QT_CONFIG(shortcut)
        self.actionGrafo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rojo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Azul", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color (rgb)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Destino en y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Verde", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Origen en y", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destino en x", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
#if QT_CONFIG(statustip)
        self.buscar_spinBox.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.buscar_spinBox.setSpecialValueText(QCoreApplication.translate("MainWindow", u"ID de la particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Graficar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.menuCrear.setTitle(QCoreApplication.translate("MainWindow", u"Crear", None))
    # retranslateUi
