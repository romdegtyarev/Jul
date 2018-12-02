#!/usr/bin/python3
# -*- coding: utf-8 -*-


#Imports
import sys
from PyQt5.QtWidgets import QMainWindow,  QWidget,        QMessageBox, QComboBox
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QLabel
from PyQt5.QtWidgets import QLineEdit,    QTextEdit,      QGridLayout
from PyQt5.QtWidgets import QPushButton,  QTableWidget,   QApplication
from PyQt5.QtWidgets import QMainWindow,  QGridLayout,    QWidget
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtGui     import QIcon
from PyQt5.QtCore    import QSize, Qt


class MainWindow(QWidget):


    def __init__(self):
        #Возвращает родительский объект MainWindow с классом, и мы вызываем его конструктор
        super().__init__()
        #Create GUI

        #Число нажатий на кнопку "Далее"
        self.buttonPressCount = 0
        #Количество критериев на уровнях
        self.level1EditValue = 0
        self.level2EditValue = 0
        self.level3EditValue = 0
        self.level4EditValue = 0
        self.level5EditValue = 0

        #Матрицы
        self.mas1 = []

        self.mas2_1 = []
        self.mas2_2 = []
        self.mas2_3 = []
        self.mas2_4 = []
        self.mas2_5 = []

        self.mas3_1 = []
        self.mas3_2 = []
        self.mas3_3 = []
        self.mas3_4 = []
        self.mas3_5 = []

        self.mas4_1 = []
        self.mas4_2 = []
        self.mas4_3 = []
        self.mas4_4 = []
        self.mas4_5 = []

        self.mas5_1 = []
        self.mas5_2 = []
        self.mas5_3 = []
        self.mas5_4 = []
        self.mas5_5 = []

        #Среднее геометрическое для каждой матрицы
        self.sg1 = []
        self.sg_sum1 = 0

        self.sg2_1 = []
        self.sg_sum2_1 = 0
        self.sg2_2 = []
        self.sg_sum2_2 = 0
        self.sg2_3 = []
        self.sg_sum2_3 = 0
        self.sg2_4 = []
        self.sg_sum2_4 = 0
        self.sg2_5 = []
        self.sg_sum2_5 = 0

        self.sg3_1 = []
        self.sg3_2 = []
        self.sg3_3 = []
        self.sg3_4 = []
        self.sg3_5 = []

        self.sg4_1 = []
        self.sg4_2 = []
        self.sg4_3 = []
        self.sg4_4 = []
        self.sg4_5 = []

        self.sg5_1 = []
        self.sg5_2 = []
        self.sg5_3 = []
        self.sg5_4 = []
        self.sg5_5 = []

        #Вектор приоритетов
        self.nv1 = []

        self.nv2_1 = []
        self.nv2_2 = []
        self.nv2_3 = []
        self.nv2_4 = []
        self.nv2_5 = []

        self.nv3_1 = []
        self.nv3_2 = []
        self.nv3_3 = []
        self.nv3_4 = []
        self.nv3_5 = []

        self.nv4_1 = []
        self.nv4_2 = []
        self.nv4_3 = []
        self.nv4_4 = []
        self.nv4_5 = []

        self.nv5_1 = []
        self.nv5_2 = []
        self.nv5_3 = []
        self.nv5_4 = []
        self.nv5_5 = []

        #Первая страница количество критереев
        self.ierarhii = QLabel('Количество уровней иерархии')
        self.level1 = QLabel('Количество критериев на первом уровне')
        self.level2 = QLabel('Количество критериев на втором уровне')
        self.level3 = QLabel('Количество критериев на теретьем уровне')
        self.level4 = QLabel('Количество критериев на четветртом уровне')
        self.level5 = QLabel('Количество критериев на пятом уровне')

        self.ierarhiiEdit = QComboBox(self)
        self.level1Edit = QComboBox(self)
        self.level2Edit = QComboBox(self)
        self.level3Edit = QComboBox(self)
        self.level4Edit = QComboBox(self)
        self.level5Edit = QComboBox(self)

        #Инициализируем начальные значения
        self.ierarhiiEdit.addItems(["2", "3", "4", "5"])
        self.ierarhiiEdit.activated[str].connect(self.onActivated)
        self.level1Edit.addItems(["2", "3", "4", "5"])
        self.level2Edit.addItems(["2", "3", "4", "5"])
        self.level3Edit.addItems(["2", "3", "4", "5"])
        self.level4Edit.addItems(["2", "3", "4", "5"])
        self.level5Edit.addItems(["2", "3", "4", "5"])

        #Вторая страница таблица
        self.table = QTableWidget(self)
        self.table2 = QTableWidget(self)
        #Ширина столбцов зависит от содержимого
        self.table.resizeColumnsToContents()
        self.table.itemSelectionChanged.connect(self.on_selection)
        self.table2.resizeColumnsToContents()
        self.table2.itemSelectionChanged.connect(self.on_selection)

        #Кнопка Далее
        self.okButton = QPushButton("Далее", self)
        self.okButton.clicked.connect(self.buttonClicked)

        self.initUI()


    def initUI(self):
        #Создаем сетку
        grid = QGridLayout()
        #Число ячеек в сетке
        grid.setSpacing(14)

        #Делаем таблицу невидимой
        self.table.setVisible(False)

        #Заполняем таблицу Виджетами
        grid.addWidget(self.table, 2, 0)
        grid.addWidget(self.table2, 2, 0)
        self.table2.setVisible(False)

        grid.addWidget(self.ierarhii, 1, 0)
        grid.addWidget(self.ierarhiiEdit, 1, 1)

        grid.addWidget(self.level1, 2, 0)
        grid.addWidget(self.level1Edit, 2, 1)

        grid.addWidget(self.level2, 3, 0)
        grid.addWidget(self.level2Edit, 3, 1)

        grid.addWidget(self.level3, 4, 0)
        grid.addWidget(self.level3Edit, 4, 1)
        self.level3Edit.setVisible(False)
        self.level3.setVisible(False)

        grid.addWidget(self.level4, 5, 0)
        grid.addWidget(self.level4Edit, 5, 1)
        self.level4Edit.setVisible(False)
        self.level4.setVisible(False)

        grid.addWidget(self.level5, 6, 0)
        grid.addWidget(self.level5Edit, 6, 1)
        self.level5Edit.setVisible(False)
        self.level5.setVisible(False)

        grid.addWidget(self.okButton, 7, 0)

        #Запихиваем сетку в экран
        self.setLayout(grid)

        #Начальная позиция и размер окна
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Автоматизация МАИ')
        #self.setWindowIcon(QIcon('1.png'))

        self.show()


    #def closeEvent(self, event):
        #reply = QMessageBox.question(self,
        #                             'Выход',
        #                             "Вы действительно хотите выйти?",
        #                             QMessageBox.Yes | QMessageBox.No,
        #                             QMessageBox.No)

        #if reply == QMessageBox.Yes:
        #    event.accept()
        #else:
        #    event.ignore()


    #Нажитие кнопки
    def buttonClicked(self):
        if self.buttonPressCount == 0:
            #Считываем значения
            self.level1EditValue = int(self.level1Edit.currentText())
            self.level2EditValue = int(self.level2Edit.currentText())
            self.level3EditValue = int(self.level3Edit.currentText())
            self.level4EditValue = int(self.level4Edit.currentText())
            self.level5EditValue = int(self.level5Edit.currentText())
            #Выключаем кнопки
            self.ierarhiiEdit.setVisible(False)
            self.level1Edit.setVisible(False)
            self.level2Edit.setVisible(False)
            self.level3Edit.setVisible(False)
            self.level4Edit.setVisible(False)
            self.level5Edit.setVisible(False)
            self.ierarhii.setText("Матрица парных сравнений для первого уровня иерархии:")
            self.level1.setVisible(False)
            self.level2.setVisible(False)
            self.level3.setVisible(False)
            self.level4.setVisible(False)
            self.level5.setVisible(False)

            #Стороим таблицу
            self.table.setColumnCount(self.level1EditValue)
            self.table.setRowCount(self.level1EditValue)
            for i in range(self.table.rowCount()):
                for j in range(self.table.columnCount()):
                    self.table.setItem(i, j, QTableWidgetItem("1"))
            #Заполняем диагональ
            for i in range(self.table.rowCount()):
                j = i
                self.table.setItem(i, j, QTableWidgetItem("1"))
                self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            #Блокируем объекты
            z = 0
            for i in range(1, self.table.rowCount()):
                z += 1
                for j in range(z):
                    self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            self.table.setVisible(True)

            self.buttonPressCount += 1

        elif self.buttonPressCount == 1:
            #Cчитываем данные в массив
            for i in range(self.table.rowCount()):
                self.mas1.append([])
                for j in range(self.table.rowCount()):
                    self.mas1[i].append(self.table.item(i, j).text())

            self.ierarhii.setText("Матрица парных сравнений для второго уровня иерархии 1:")
            #Стороим таблицу
            self.table.setColumnCount(self.level2EditValue)
            self.table.setRowCount(self.level2EditValue)
            for i in range(self.table.rowCount()):
                for j in range(self.table.columnCount()):
                    self.table.setItem(i, j, QTableWidgetItem("1"))
            #Заполняем диагональ
            for i in range(self.table.rowCount()):
                j = i
                self.table.setItem(i, j, QTableWidgetItem("1"))
                self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            #Блокируем объекты
            z = 0
            for i in range(1, self.table.rowCount()):
                z += 1
                for j in range(z):
                    self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            self.table.setVisible(True)

            self.buttonPressCount += 1

        elif self.buttonPressCount == 2:
            #Cчитываем данные в массив
            for i in range(self.table.rowCount()):
                self.mas2_1.append([])
                for j in range(self.table.rowCount()):
                    self.mas2_1[i].append(self.table.item(i, j).text())

            self.ierarhii.setText("Матрица парных сравнений для второго уровня иерархии 2:")
            #Стороим таблицу
            self.table.setColumnCount(self.level2EditValue)
            self.table.setRowCount(self.level2EditValue)
            for i in range(self.table.rowCount()):
                for j in range(self.table.columnCount()):
                    self.table.setItem(i, j, QTableWidgetItem("1"))
            #Заполняем диагональ
            for i in range(self.table.rowCount()):
                j = i
                self.table.setItem(i, j, QTableWidgetItem("1"))
                self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            #Блокируем объекты
            z = 0
            for i in range(1, self.table.rowCount()):
                z += 1
                for j in range(z):
                    self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            self.table.setVisible(True)

            self.buttonPressCount += 1

        elif self.buttonPressCount == 3:
            #Cчитываем данные в массив
            for i in range(self.table.rowCount()):
                self.mas2_2.append([])
                for j in range(self.table.rowCount()):
                    self.mas2_2[i].append(self.table.item(i, j).text())

            if self.level1EditValue > 2:
                self.ierarhii.setText("Матрица парных сравнений для второго уровня иерархии 3:")
                #Стороим таблицу
                self.table.setColumnCount(self.level2EditValue)
                self.table.setRowCount(self.level2EditValue)
                for i in range(self.table.rowCount()):
                    for j in range(self.table.columnCount()):
                        self.table.setItem(i, j, QTableWidgetItem("1"))
                #Заполняем диагональ
                for i in range(self.table.rowCount()):
                    j = i
                    self.table.setItem(i, j, QTableWidgetItem("1"))
                    self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                #Блокируем объекты
                z = 0
                for i in range(1, self.table.rowCount()):
                    z += 1
                    for j in range(z):
                        self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

                self.table.setVisible(True)
            else:
                self.calc()

            self.buttonPressCount += 1

        elif self.buttonPressCount == 4:
            #Cчитываем данные в массив
            for i in range(self.table.rowCount()):
                self.mas2_3.append([])
                for j in range(self.table.rowCount()):
                    self.mas2_3[i].append(self.table.item(i, j).text())

            if self.level1EditValue > 3:
                self.ierarhii.setText("Матрица парных сравнений для второго уровня иерархии 4:")
                #Стороим таблицу
                self.table.setColumnCount(self.level2EditValue)
                self.table.setRowCount(self.level2EditValue)
                for i in range(self.table.rowCount()):
                    for j in range(self.table.columnCount()):
                        self.table.setItem(i, j, QTableWidgetItem("1"))
                #Заполняем диагональ
                for i in range(self.table.rowCount()):
                    j = i
                    self.table.setItem(i, j, QTableWidgetItem("1"))
                    self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                #Блокируем объекты
                z = 0
                for i in range(1, self.table.rowCount()):
                    z += 1
                    for j in range(z):
                        self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

                self.table.setVisible(True)
            else:
                self.calc()

            self.buttonPressCount += 1

        elif self.buttonPressCount == 5:
            #Cчитываем данные в массив
            for i in range(self.table.rowCount()):
                self.mas2_4.append([])
                for j in range(self.table.rowCount()):
                    self.mas2_4[i].append(self.table.item(i, j).text())

            if self.level1EditValue > 4:
                self.ierarhii.setText("Матрица парных сравнений для второго уровня иерархии 5:")
                #Стороим таблицу
                self.table.setColumnCount(self.level2EditValue)
                self.table.setRowCount(self.level2EditValue)
                for i in range(self.table.rowCount()):
                    for j in range(self.table.columnCount()):
                        self.table.setItem(i, j, QTableWidgetItem("1"))
                #Заполняем диагональ
                for i in range(self.table.rowCount()):
                    j = i
                    self.table.setItem(i, j, QTableWidgetItem("1"))
                    self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                #Блокируем объекты
                z = 0
                for i in range(1, self.table.rowCount()):
                    z += 1
                    for j in range(z):
                        self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            else:
                self.calc()

                self.table.setVisible(True)

            self.buttonPressCount += 1

        elif self.buttonPressCount == 6:
            #Cчитываем данные в массив
            for i in range(self.table.rowCount()):
                self.mas2_5.append([])
                for j in range(self.table.rowCount()):
                    self.mas2_5[i].append(self.table.item(i, j).text())

            self.calc()

            self.buttonPressCount += 1


    #Изменение Комбобокса
    def onActivated(self, text):
        i = int(text)
        if i == 3:
            self.level3Edit.setVisible(True)
            self.level3.setVisible(True)
            self.level4Edit.setVisible(False)
            self.level4.setVisible(False)
            self.level5Edit.setVisible(False)
            self.level5.setVisible(False)
        elif i == 4:
            self.level3Edit.setVisible(True)
            self.level3.setVisible(True)
            self.level4Edit.setVisible(True)
            self.level4.setVisible(True)
            self.level5Edit.setVisible(False)
            self.level5.setVisible(False)
        elif i == 5:
            self.level3Edit.setVisible(True)
            self.level3.setVisible(True)
            self.level4Edit.setVisible(True)
            self.level4.setVisible(True)
            self.level5Edit.setVisible(True)
            self.level5.setVisible(True)
        elif i == 2:
            self.level3Edit.setVisible(False)
            self.level3.setVisible(False)
            self.level4Edit.setVisible(False)
            self.level4.setVisible(False)
            self.level5Edit.setVisible(False)
            self.level5.setVisible(False)


    #Изменение ячейки;
    def on_selection(self):
        #Считаем обратные значения
        z = 0
        for i in range(1, self.table.rowCount()):
            z += 1
            for j in range(z):
                item = str(round(1 / float(self.table.item(j, i).text()), 4))
                self.table.setItem(i, j, QTableWidgetItem(item))
                self.table.item(i, j).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)


    def calc(self):
        self.ierarhii.setText("Результаты:")
        self.okButton.setVisible(False)
        self.table.setVisible(False)
        self.table2.setVisible(True)


        #1
        #Считаем СГ
        for i in range(int(self.level1EditValue)):
            self.sg1.append([])
            self.sg1[i] = 1
            for j in range(int(self.level1EditValue)):
                self.sg1[i] = float(self.sg1[i]) * float(self.mas1[i][j])
            self.sg1[i] = round(pow(float(self.sg1[i]), 1/float(self.level1EditValue)), 4)
            self.sg_sum1 += float(self.sg1[i])

        #Считаем НВ
        for i in range(int(self.level1EditValue)):
            self.nv1.append([])
            self.nv1[i] = float(self.sg1[i]) / float(self.sg_sum1)


        #2_1
        #Считаем СГ
        for i in range(int(self.level2EditValue)):
            self.sg2_1.append([])
            self.sg2_1[i] = 1
            for j in range(int(self.level2EditValue)):
                self.sg2_1[i] = float(self.sg2_1[i]) * float(self.mas2_1[i][j])
            self.sg2_1[i] = round(pow(float(self.sg2_1[i]), 1/float(self.level2EditValue)), 4)
            self.sg_sum2_1 += float(self.sg2_1[i])

        #Считаем НВ
        for i in range(int(self.level2EditValue)):
            self.nv2_1.append([])
            self.nv2_1[i] = float(self.sg2_1[i]) / float(self.sg_sum2_1)


        #2_2
        #Считаем СГ
        for i in range(int(self.level2EditValue)):
            self.sg2_2.append([])
            self.sg2_2[i] = 1
            for j in range(int(self.level2EditValue)):
                self.sg2_2[i] = float(self.sg2_2[i]) * float(self.mas2_2[i][j])
            self.sg2_2[i] = round(pow(float(self.sg2_2[i]), 1/float(self.level2EditValue)), 4)
            self.sg_sum2_2 += float(self.sg2_2[i])

        #Считаем НВ
        for i in range(int(self.level2EditValue)):
            self.nv2_2.append([])
            self.nv2_2[i] = float(self.sg2_2[i]) / float(self.sg_sum2_2)


        if self.level1EditValue > 2:
            #2_3
            #Считаем СГ
            for i in range(int(self.level2EditValue)):
                self.sg2_3.append([])
                self.sg2_3[i] = 1
                for j in range(int(self.level2EditValue)):
                    self.sg2_3[i] = float(self.sg2_3[i]) * float(self.mas2_3[i][j])
                self.sg2_3[i] = round(pow(float(self.sg2_3[i]), 1/float(self.level2EditValue)), 4)
                self.sg_sum2_3 += float(self.sg2_3[i])

            #Считаем НВ
            for i in range(int(self.level2EditValue)):
                self.nv2_3.append([])
                self.nv2_3[i] = float(self.sg2_3[i]) / float(self.sg_sum2_3)


        if self.level1EditValue > 3:
            #2_4
            #Считаем СГ
            for i in range(int(self.level2EditValue)):
                self.sg2_4.append([])
                self.sg2_4[i] = 1
                for j in range(int(self.level2EditValue)):
                    self.sg2_4[i] = float(self.sg2_4[i]) * float(self.mas2_4[i][j])
                self.sg2_4[i] = round(pow(float(self.sg2_4[i]), 1/float(self.level2EditValue)), 4)
                self.sg_sum2_4 += float(self.sg2_4[i])

            #Считаем НВ
            for i in range(int(self.level2EditValue)):
                self.nv2_4.append([])
                self.nv2_4[i] = float(self.sg2_4[i]) / float(self.sg_sum2_4)


        if self.level1EditValue > 4:
            #2_5
            #Считаем СГ
            for i in range(int(self.level2EditValue)):
                self.sg2_5.append([])
                self.sg2_5[i] = 1
                for j in range(int(self.level2EditValue)):
                    self.sg2_5[i] = float(self.sg2_5[i]) * float(self.mas2_5[i][j])
                self.sg2_5[i] = round(pow(float(self.sg2_5[i]), 1/float(self.level2EditValue)), 4)
                self.sg_sum2_5 += float(self.sg2_5[i])

            #Считаем НВ
            for i in range(int(self.level2EditValue)):
                self.nv2_5.append([])
                self.nv2_5[i] = float(self.sg2_5[i]) / float(self.sg_sum2_5)


        #Стороим таблицу
        self.table2.setColumnCount(self.level1EditValue + 1)
        self.table2.setRowCount(self.level1EditValue + 1)
        self.table2.clear()

        for i in range(self.table2.columnCount() - 1):
            item = str(round(float(self.nv1[i]), 4))
            self.table2.setItem(0, i, QTableWidgetItem(item))
            self.table2.item(0, i).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        for i in range(1, self.table2.rowCount()):
            item = str(round(float(self.nv2_1[i - 1]), 4))
            self.table2.setItem(i, 0, QTableWidgetItem(item))
            self.table2.item(i, 0).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        for i in range(1, self.table2.rowCount()):
            item = str(round(float(self.nv2_2[i - 1]), 4))
            self.table2.setItem(i, 1, QTableWidgetItem(item))
            self.table2.item(i, 1).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        if self.level1EditValue > 2:
            for i in range(1, self.table2.rowCount()):
                item = str(round(float(self.nv2_3[i - 1]), 4))
                self.table2.setItem(i, 2, QTableWidgetItem(item))
                self.table2.item(i, 2).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        if self.level1EditValue > 3:
            for i in range(1, self.table2.rowCount()):
                item = str(round(float(self.nv2_4[i - 1]), 4))
                self.table2.setItem(i, 3, QTableWidgetItem(item))
                self.table2.item(i, 3).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        if self.level1EditValue > 4:
        for i in range(1, self.table2.rowCount()):
            item = str(round(float(self.nv2_5[i - 1]), 4))
            self.table2.setItem(i, 4, QTableWidgetItem(item))
            self.table2.item(i, 4).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        temp = 0
        for i in range(0, self.level1EditValue):
            temp += float(self.nv1[i]) * float(self.nv2_1[i])
        item = str(round(float(temp), 4))
        self.table2.setItem(1, 5, QTableWidgetItem(item))
        self.table2.item(1, 5).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        temp = 0
        for i in range(0, self.level1EditValue):
            temp += float(self.nv1[i]) * float(self.nv2_2[i])
        item = str(round(float(temp), 4))
        self.table2.setItem(2, 5, QTableWidgetItem(item))
        self.table2.item(2, 5).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        if self.level1EditValue > 2:
            temp = 0
            for i in range(0, self.level1EditValue):
                temp += float(self.nv1[i]) * float(self.nv2_3[i])
            item = str(round(float(temp), 4))
            self.table2.setItem(3, 5, QTableWidgetItem(item))
            self.table2.item(3, 5).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        if self.level1EditValue > 3:
            temp = 0
            for i in range(0, self.level1EditValue):
                temp += float(self.nv1[i]) * float(self.nv2_4[i])
            item = str(round(float(temp), 4))
            self.table2.setItem(4, 5, QTableWidgetItem(item))
            self.table2.item(4, 5).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        if self.level1EditValue > 4:
            temp = 0
            for i in range(0, self.level1EditValue):
                temp += float(self.nv1[i]) * float(self.nv2_5[i])
            item = str(round(float(temp), 4))
            self.table2.setItem(5, 5, QTableWidgetItem(item))
            self.table2.item(5, 5).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow  = MainWindow()

    sys.exit(app.exec_())
