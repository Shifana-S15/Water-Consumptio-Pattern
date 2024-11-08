from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os

class StyledItemDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        painter.save()

        if index.row() % 2 == 0:  # Alternate row coloring
            painter.fillRect(option.rect, QtGui.QColor(240, 240, 240))

        text = index.data()
        font = painter.font()
        font.setPointSize(12)
        painter.setFont(font)
        
        # Draw borders
        border_rect = option.rect.adjusted(0, 0, -1, -1)
        painter.setPen(QtGui.QColor("black"))
        painter.drawRect(border_rect)
        
      # Add padding for better spacing
        text_rect = option.rect.adjusted(15, 5, -15, -5)  # Adjust padding as needed
        painter.drawText(text_rect, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter, text)

        painter.restore()
    def sizeHint(self, option, index):
        # Set a fixed height for each row
        return QtCore.QSize(option.rect.width(), 40)  # Adjust the height as needed

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 1500)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.setStyleSheet("background-color: rgba(0,0,0, 200);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Close button  
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(1890, 0, 30, 30))
        self.closeButton.setStyleSheet("background-color: red; color: white; ")
        self.closeButton.setText("X")
        self.closeButton.clicked.connect(MainWindow.close)

        self.minimizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.minimizeButton.setGeometry(QtCore.QRect(1860, 0, 30, 30))
        self.minimizeButton.setStyleSheet("background-color:white; color: black; ")
        self.minimizeButton.setText("_")
        self.minimizeButton.clicked.connect(MainWindow.showMinimized)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 221, 61))
        self.pushButton.setStyleSheet("background-color: rgba(39, 126, 205, 200); color: white; border-radius: 10px;")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 90, 221, 61))
        self.pushButton_2.setStyleSheet("background-color: rgba(39, 126, 205, 200); color: white; border-radius: 10px;")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 170, 221, 61))
        self.pushButton_3.setStyleSheet("background-color: rgba(39, 126, 205, 200); color: white; border-radius: 10px;")

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(270, 260, 1600, 891))
        self.listView.setStyleSheet("background-color: rgba(255, 255, 255, 80);")



        # Acknowledge button
        self.ack_button = QtWidgets.QPushButton("Acknowledge")
        self.ack_button.setFixedSize(250, 100)  # Set the button size
        self.ack_button.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                padding: 20px;
            }
        """)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(990, 150, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #277ECD; background-color: rgba(0, 0, 0, 0);")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)
        delegate = StyledItemDelegate()
        self.listView.setItemDelegate(delegate)
        self.processData()
        MainWindow.showFullScreen()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alert"))
        self.pushButton.setText(_translate("MainWindow", "DashBoard"))
        self.pushButton_2.setText(_translate("MainWindow", "Add Data"))
        self.pushButton_3.setText(_translate("MainWindow", "Alert"))
        self.label.setText(_translate("MainWindow", "ALERTS"))

    def processData(self):
        # self.data = pd.read_excel('WaterData.xlsx')
        # self.data = self.data.drop(self.data.index[:2])
        # self.data['Date'] = pd.to_datetime(self.data['Date'])
        # self.data.set_index('Date', inplace=True)

        # Load and preprocess data (Method 1's approach)
        self.data = pd.read_excel('WaterData.xlsx')

        # Drop the first two rows if needed
        self.data = self.data.drop(self.data.index[:2])

        # Convert 'Date' column to datetime
        self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')  # Convert invalid dates to NaT

        # Check if 'Date' column exists
        if 'Date' not in self.data.columns:
            raise KeyError("Column 'Date' does not exist in the DataFrame.")

        # Drop rows where 'Date' is NaT (previously NaN)
        self.data = self.data.dropna(subset=['Date'])

        # Set 'Date' column as index
        self.data.set_index('Date', inplace=True)

        # Apply frequency
        self.data = self.data.asfreq('D')

        # Apply absolute values
        self.data = self.data.abs()
        last_date = self.data.index[-1]  # This retrieves the last date in the index

        print(f"The last date in the data is: {last_date}")

        def calculate_limits(group_data):
            high_limit = group_data.quantile(0.95)
            low_limit = group_data.quantile(0.05)
            return high_limit, low_limit

        columns_to_process = self.data.columns
        self.limits = {}
        for column in columns_to_process:
            high_limit, low_limit = calculate_limits(self.data[column])
            self.limits[column] = {'high_limit': high_limit, 'low_limit': low_limit}
            if(column == 'TPP'):
                print(self.limits[column])
                print(self.data[column].count)

        self.last_values = self.data.iloc[-1]

        # Load acknowledgments
        acknowledgment_file = 'acknowledgments.xlsx'
        if os.path.exists(acknowledgment_file):
            self.acknowledgments = pd.read_excel(acknowledgment_file)
        else:
            self.acknowledgments = pd.DataFrame(columns=['Date', 'Column', 'Acknowledged'])

        self.model.clear()  # Clear the model before adding new data

        for column in columns_to_process:
            last_value = self.last_values[column]
            high_limit = self.limits[column]['high_limit']
            low_limit = self.limits[column]['low_limit']
            
            # Check if already acknowledged
            if not self.acknowledgments[(self.acknowledgments['Column'] == column) &  (self.acknowledgments['Date'] == last_date)].empty:
                continue

            if last_value > high_limit:
                result = f"'{column}' exceeds the Normal Range."
                show_acknowledgment_button = True
            elif last_value < low_limit:
                result = f"'{column}' is below the Normal Range."
                show_acknowledgment_button = True
            else:
                result = f"'{column}' is within the Normal range."
                show_acknowledgment_button = False

            item = QtGui.QStandardItem(result)
            self.model.appendRow(item)

            if show_acknowledgment_button:
                ack_button = QtWidgets.QPushButton("Acknowledge")
                ack_button.clicked.connect(lambda _, col=column: self.acknowledgeAlert(col))
                
                # Create a container widget to hold the button
                container = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout(container)
                layout.addStretch()
                layout.addWidget(ack_button)
                layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
                
                self.listView.setIndexWidget(item.index(), container)

    def acknowledgeAlert(self, column):
        try:
            # Retrieve the date from the WaterData.xlsx file
            acknowledgment_date = self.data.index[-1]  # Last date in the data

            # Read the acknowledgment file
            if os.path.exists('acknowledgments.xlsx'):
                self.acknowledgments = pd.read_excel('acknowledgments.xlsx')
            else:
                self.acknowledgments = pd.DataFrame(columns=['Date', 'Column', 'Acknowledged'])

            # Add a new acknowledgment for the column
            new_acknowledgment = pd.DataFrame({
                'Date': [acknowledgment_date],
                'Column': [column],
                'Acknowledged': [True]
            })

            # Concatenate the new acknowledgment with the existing ones
            self.acknowledgments = pd.concat([self.acknowledgments, new_acknowledgment], ignore_index=True)

            # Save back to the file
            self.acknowledgments.to_excel('acknowledgments.xlsx', index=False)
            self.refreshUI()

            # Optionally, update the UI or give feedback to the user
            print(f"Acknowledgment for {column} on {acknowledgment_date} has been recorded.")

        except FileNotFoundError:
            # If the file doesn't exist, create it
            acknowledgment_date = self.data.index[-1]  # Last date in the data
            new_acknowledgment = pd.DataFrame({
                'Date': [acknowledgment_date],
                'Column': [column],
                'Acknowledged': [True]
            })
            new_acknowledgment.to_excel('acknowledgments.xlsx', index=False)
            self.refreshUI()

    def refreshUI(self):
        self.model.clear()  # Clear the model before adding new data
        self.processData()  # Re-process and update the UI
