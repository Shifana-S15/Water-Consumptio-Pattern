# main.py
import sys
from PyQt5 import QtWidgets
from UI3 import Ui_MainWindow as UI3_MainWindow
from UI4 import Ui_MainWindow as UI4_MainWindow
from UI1 import Ui_MainWindow as UI1_MainWindow
from UI5 import Ui_MainWindow as UI5_MainWindow
from UI6 import Ui_MainWindow as UI6_MainWindow
import datetime
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from PyQt5.QtWidgets import QMessageBox

# from ui3 import Ui3  # Assuming you have a class for UI3
# from ui4 import Ui4  # Assuming you have a class for UI4

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui3 = None
        self.ui4 = None
        self.ui1 = None
        self.switch_to_ui1()
        self.setWindowTitle("Main Application")
        self.collected_data = []

    def write_to_excel(self):
        existing_file = 'WaterData.xlsx'
        df_existing = pd.read_excel(existing_file)
        self.collected_data[1:] = [int(x) for x in self.collected_data[1:]]
        df_new_row = pd.DataFrame([self.collected_data], columns=df_existing.columns)
        df_updated = pd.concat([df_existing, df_new_row], ignore_index=True)
        df_updated.to_excel(existing_file, index=False)
        print(self.collected_data)

           # Create and show the alert box
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Process Successfully completed")
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        
        print("Process Successfully completed")

    def switch_to_ui1(self):
        self.ui1 = UI1_MainWindow()
        self.ui1.setupUi(self)
        self.ui1.pushButton_2.clicked.connect(self.switch_to_ui3)
        self.ui1.pushButton_3.clicked.connect(self.switch_to_ui5)
        self.ui1.pushButton_4.clicked.connect(self.switch_to_ui6)
        print("switch_to_ui1")

    def switch_to_ui4(self):
        self.ui4 = UI4_MainWindow()
        self.ui4.setupUi(self)
        self.ui4.pushButton_4.clicked.connect(self.collect_data_from_ui4)
        self.ui4.pushButton_6.clicked.connect(self.switch_to_ui3)
        self.ui4.pushButton.clicked.connect(self.switch_to_ui1)
        self.ui4.pushButton_3.clicked.connect(self.switch_to_ui5)
        print("switch_to_ui4")

    def switch_to_ui3(self):
        self.ui3 = UI3_MainWindow()
        self.ui3.setupUi(self)
        self.ui3.pushButton_5.clicked.connect(self.collect_data_from_ui3)
        self.ui3.pushButton_6.clicked.connect(self.switch_to_ui4)
        self.ui3.pushButton.clicked.connect(self.switch_to_ui1)
        self.ui3.pushButton_3.clicked.connect(self.switch_to_ui5)

    def switch_to_ui5(self):
        self.ui5 = UI5_MainWindow()
        self.ui5.setupUi(self)
        self.ui5.pushButton_2.clicked.connect(self.switch_to_ui3)
        self.ui5.pushButton.clicked.connect(self.switch_to_ui1)
        print("switch_to_ui4")

    def switch_to_ui6(self):
        self.ui6 = UI6_MainWindow()
        self.ui6.setupUi(self)
        self.ui6.pushButton.clicked.connect(self.switch_to_ui1)
        self.ui6.pushButton_2.clicked.connect(self.switch_to_ui3)
        self.ui6.pushButton_3.clicked.connect(self.switch_to_ui5)
        print("switch_to_ui6")

    def collect_data_from_ui4(self):
        print("collect_data_from_ui4")
        data = [
            self.ui4.textEdit.toPlainText(),
            self.ui4.textEdit_2.toPlainText(),
            self.ui4.textEdit_3.toPlainText(),
            self.ui4.textEdit_4.toPlainText(),
            self.ui4.textEdit_5.toPlainText(),
            self.ui4.textEdit_6.toPlainText(),
            self.ui4.textEdit_7.toPlainText(),
            self.ui4.textEdit_8.toPlainText(),
            self.ui4.textEdit_9.toPlainText(),
            self.ui4.textEdit_10.toPlainText(),
            self.ui4.textEdit_11.toPlainText()
        ]
        self.collected_data.extend(data)
        if len(self.collected_data) == 22:
            self.write_to_excel()

    def collect_data_from_ui3(self):
        self.selected_date = self.ui3.calendarWidget.selectedDate()
        print(self.selected_date)

        python_date = datetime.date(self.selected_date.year(), self.selected_date.month(), self.selected_date.day())
        # Convert Python date to pandas.Timestamp
        self.provided_date = pd.Timestamp(python_date)
        self.collected_data.insert(0, self.provided_date)
        print("collect_data_from_ui3")
        data = [
            self.ui3.textEdit.toPlainText(),
            self.ui3.textEdit_2.toPlainText(),
            self.ui3.textEdit_3.toPlainText(),
            self.ui3.textEdit_4.toPlainText(),
            self.ui3.textEdit_5.toPlainText(),
            self.ui3.textEdit_6.toPlainText(),
            self.ui3.textEdit_7.toPlainText(),
            self.ui3.textEdit_8.toPlainText(),
            self.ui3.textEdit_9.toPlainText(),
            self.ui3.textEdit_10.toPlainText()
        ]
        self.collected_data.extend(data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())
