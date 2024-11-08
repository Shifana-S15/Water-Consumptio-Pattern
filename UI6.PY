
import sys
from PyQt5 import QtCore, QtGui, QtWidgets , QtWebEngineWidgets
import pandas as pd
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
from io import BytesIO
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import datetime
import os
extraction_points = ['Time Office Bore', 'Store Bore', 'North Weigh Bridge', 'South Weigh Bridge', 'Railway Siding Bore', 'Petron Bore', 'Crusher Bore', 'LSR -1 Bore', 'Raw Mill-1 Bore', 'Colony Bore']
usage_points = ['ETP Tank', 'Fountain', 'Lorry Yard', 'Shopping Mall', 'Colony', 'Plant', 'Labour Colony', 'TPP', 'Softner Plant', 'Fire tank', 'Water tank']


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        print("Done UI3")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 1500)
        # MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set translucent background
        MainWindow.setStyleSheet("background-color: rgba(0,0,0, 200);")
       

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(1890, 0, 30, 30))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setStyleSheet("background-color: red; color: white; ")
        self.closeButton.setText("X")
        self.closeButton.clicked.connect(MainWindow.close)
        self.minimizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.minimizeButton.setGeometry(QtCore.QRect(1860, 0, 30, 30))
        self.minimizeButton.setObjectName("minimizeButton")
        self.minimizeButton.setStyleSheet("background-color:white; color: black; ")
        self.minimizeButton.setText("_")
        self.minimizeButton.clicked.connect(MainWindow.showMinimized)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 231, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: rgba(39, 126, 205, 200); color: white; border-radius: 10px;")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 90, 231, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: rgba(39, 126, 205, 200); color: white; border-radius: 10px;")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(390, 40, 1505, 850))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setStyleSheet("""
            background-color: rgba(255, 255, 255, 80);
            border: 4px solid #277ECD;
            border-radius: 10px;
            border-radius: 20px;                          
        """)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 350, 390, 300))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setStyleSheet("""
    QCalendarWidget {
        background-color: white;
        color: black;
        border-radius: 10px;
    }
    QCalendarWidget QAbstractItemView:enabled {
        color: black;
        background-color: white;
        selection-background-color: blue;
        selection-color: white;
    }
    QCalendarWidget QAbstractItemView:disabled {
        color: gray;
    }
    QCalendarWidget QWidget#qt_calendar_navigationbar {
        background-color: blue;
        color: white;
    }
    QCalendarWidget QToolButton {
        color: white;
        font-size: 14px;
        icon-size: 16px, 16px;
    }
    QCalendarWidget QToolButton#qt_calendar_prevmonth, 
    QCalendarWidget QToolButton#qt_calendar_nextmonth {
        border: none;
        background-color: grey;
    }
    QCalendarWidget QToolButton#qt_calendar_prevmonth {
        qproperty-icon: url(left-arrow.png);
        width: 20px;
    }
    QCalendarWidget QToolButton#qt_calendar_nextmonth {
        qproperty-icon: url(right-arrow.png);
        width: 20px;
    }
    QCalendarWidget QToolButton#qt_calendar_yearbutton, 
    QCalendarWidget QToolButton#qt_calendar_monthbutton {
        color: white;
        background-color: blue;
        border: none;
    }
    QCalendarWidget QSpinBox {
        color: white;
        background-color: blue;  /* Background color for the spin box */
        border: none;
    }
    QCalendarWidget QSpinBox::up-button, 
    QCalendarWidget QSpinBox::down-button {
        subcontrol-origin: border;
        width: 16px;
    }
    QCalendarWidget QSpinBox::up-arrow, 
    QCalendarWidget QSpinBox::down-arrow {
        width: 0;
        height: 0;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
    }
    QCalendarWidget QSpinBox::up-arrow {
        border-bottom: 5px solid white;
    }
    QCalendarWidget QSpinBox::down-arrow {
        border-top: 5px solid white;
    }
    QCalendarWidget QTableView {
        border-width: 0px;
    }
    QCalendarWidget QTableView QHeaderView::section {
        color: black;
        background-color: white;
    }
    QCalendarWidget QTableView QHeaderView::section:disabled {
        color: black;
        background-color: white;
    }
    QCalendarWidget QTableView QHeaderView::section:checked {
        color: white;
        background-color: blue;
    }
    QCalendarWidget QTableView QHeaderView::section:hover {
        color: black;
        background-color: #E0E0E0;
    }
""")
        
        
        
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(20, 790, 100, 100))
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setPixmap(QtGui.QPixmap(r"C:\Users\shifa\OneDrive\Desktop\SILIPANA AKKA\logo-white-footer.png"))  # Update the path to your PNG file here
        self.imageLabel.setScaledContents(True)

        self.imageLabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel_1.setGeometry(QtCore.QRect(170, 790, 100, 100))
        self.imageLabel_1.setObjectName("imageLabel")
        self.imageLabel_1.setPixmap(QtGui.QPixmap(r"C:\Users\shifa\OneDrive\Desktop\SILIPANA AKKA\RAMCO-removebg-preview.png"))  # Update the path to your PNG file here
        self.imageLabel_1.setScaledContents(True)



        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 170, 231, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-color: rgba(39, 126, 205, 200); color: white; border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1900, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        print("In UI3")
        MainWindow.setStatusBar(self.statusbar)

        graphics_layout = QVBoxLayout(self.graphicsView)
        self.plot_frame = QtWidgets.QFrame()
        self.plot_frame.setObjectName("plot_frame")
        self.plot_frame.setGeometry(QtCore.QRect(0, 0, 1505, 850))
        self.webEngineView = QWebEngineView(self.plot_frame)
        self.webEngineView.setGeometry(QtCore.QRect(0, 0, 1505, 850))
        graphics_layout.addWidget(self.plot_frame)
        self.create_sankey_diagram()
         # Connect selectionChanged signal to slot function
        self.calendarWidget.selectionChanged.connect(self.handle_selection_change)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def handle_selection_change(self):
        selected_date = self.calendarWidget.selectedDate()
        python_date = datetime.date(selected_date.year(), selected_date.month(), selected_date.day())
        provided_date = pd.Timestamp(python_date)

        mac_data = pd.read_excel('WaterData.xlsx')
        mac_data = mac_data.drop(mac_data.index[:2])
        # Convert 'Date' column to datetime
        mac_data['Date'] = pd.to_datetime(mac_data['Date'], errors='coerce')
        mac_data = mac_data.dropna(subset=['Date'])
        # Handle duplicate dates by grouping and summing the values
        df = mac_data.groupby('Date').sum()
        # df = df.dropna(subset=['Date'])
        # Set date column as index and set frequency

        # Drop rows where 'Date' is NaT
       
        df = df.asfreq('D')
        df = df.abs()  # Apply absolute values to align with Method 1
        # Initialize lists to store data for Sankey diagram
        sources = []
        targets = []
        values = []
        colors = []  # To store colors for the links

        # Define the columns to process
        columns_to_process = df.columns

        # Function to calculate high and low limits
        def calculate_limits(group_data):
            high_limit = group_data.quantile(0.95)
            low_limit = group_data.quantile(0.05)
            return high_limit, low_limit

        # Calculate high and low limits for each column
        limits = {}
        for column in columns_to_process:
            high_limit, low_limit = calculate_limits(df[column])
            limits[column] = {'high_limit': high_limit, 'low_limit': low_limit}
            if(column == 'TPP'):
                print(limits[column])
                print(df[column].count)

        # Load acknowledgments
        acknowledgment_file = 'acknowledgments.xlsx'
        if os.path.exists(acknowledgment_file):
            acknowledgments = pd.read_excel(acknowledgment_file)
        else:
            acknowledgments = pd.DataFrame(columns=['Date','Column', 'Acknowledged'])



# Iterate through each row in df
        for index, row in df.iterrows():
            # Check if the index matches the provided date
            if index == provided_date:
                # Add flows from extraction points to the tank
                for extraction_point in extraction_points:
                    last_value = row[extraction_point]
                    high_limit = limits[extraction_point]['high_limit']
                    low_limit = limits[extraction_point]['low_limit']

                    # Ensure that the 'Date' column in acknowledgments is a datetime object
                    acknowledgments['Date'] = pd.to_datetime(acknowledgments['Date'], errors='coerce')
                    # Determine the color based on limits and acknowledgment
                    acknowledgment_entry = acknowledgments[
                        (acknowledgments['Column'] == extraction_point) &
                        (acknowledgments['Date'] == provided_date)
                    ]
                    print(acknowledgment_entry)
                    
                    # print(acknowledgment_entry['Acknowledged'].values[0])
                    if not acknowledgment_entry.empty:
                        acknowledgment_status = acknowledgment_entry['Acknowledged'].values[0]
                        
                    else:
                        acknowledgment_status = False

                    if last_value > high_limit or last_value < low_limit:
                        color = 'red' if not acknowledgment_status else '#FF5733'
                    else:
                        color = '#00FF00'  # Default color for within limits

                    sources.append(extraction_point)
                    targets.append('Tank')
                    values.append(last_value)
                    colors.append(color)

                # Add flows from the tank to usage points
                for usage_point in usage_points:
                    last_value = row[usage_point]
                    high_limit = limits[usage_point]['high_limit']
                    low_limit = limits[usage_point]['low_limit']
                    acknowledgments['Date'] = pd.to_datetime(acknowledgments['Date'], errors='coerce')
                    # Determine the color based on limits and acknowledgment
                    acknowledgment_entry = acknowledgments[
                        (acknowledgments['Column'] == usage_point) &
                        (acknowledgments['Date'] == provided_date)
                    ]
                    
                    # print("------======-------",usage_point)
                    if not acknowledgment_entry.empty:
                        acknowledgment_status = acknowledgment_entry['Acknowledged'].values[0]
                        
                    else:
                        acknowledgment_status = False
                    
                    if last_value > high_limit or last_value < low_limit:
                        color = 'red' if not acknowledgment_status else '#f7f705'
                    else:
                        color = '#00FF00'  # Default color for within limits

                    sources.append('Tank')
                    targets.append(usage_point)
                    values.append(last_value)
                    colors.append(color)

        # Create node labels and colors
        node_labels = extraction_points + ['Tank'] + usage_points
        node_colors = ['#A0CBE2' if label != 'Tank' else '#FFD700' for label in node_labels]  # Custom color for the tank

        # Create the Plotly Sankey diagram
        fig = make_subplots(rows=1, cols=1)
        sankey = go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=node_labels,
                color=node_colors,
            ),
            link=dict(
                source=[node_labels.index(src) for src in sources],
                target=[node_labels.index(trg) for trg in targets],
                value=values,
                color=colors,  # Use the color list for the links
            ),
        )
        fig.add_trace(sankey)
        html = fig.to_html(full_html=False, include_plotlyjs='cdn')

        # Load the HTML content into the QWebEngineView
        self.webEngineView.setHtml(html)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "DASHBOARD"))
        self.pushButton_2.setText(_translate("MainWindow", "ADD DATA"))
        self.pushButton_3.setText(_translate("MainWindow", "ALERT"))

    def create_sankey_diagram(self):
        mac_data = pd.read_excel('WaterData.xlsx')
        df = pd.DataFrame(mac_data)
        df['Date'] = pd.to_datetime(df['Date'])

        # Handle duplicate dates by grouping and summing the values
        df = df.groupby('Date').sum()

        # Set date column as index and set frequency
        df = df.asfreq('D')
        df = df.abs()
        sources = []
        targets = []
        values = []

        for index, row in df.iterrows():
            for extraction_point in extraction_points:
                sources.append(extraction_point)
                targets.append('Tank')
                values.append(row[extraction_point])

            for usage_point in usage_points:
                sources.append('Tank')
                targets.append(usage_point)
                values.append(row[usage_point])

        node_labels = extraction_points + ['Tank'] + usage_points
        node_colors = ['#FF5733'] * len(extraction_points) + ['#A0CBE2'] + ['#00FF00'] * len(usage_points)

        # Create the Plotly figure
        fig = make_subplots(rows=1, cols=1)
        sankey = go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=node_labels,
                color=node_colors,
            ),
            link=dict(
                source=[node_labels.index(source) for source in sources],
                target=[node_labels.index(target) for target in targets],
                value=values,
            ),
        )
        fig.add_trace(sankey)
    # Update layout for transparent background
        # fig.update_layout(
        #     plot_bgcolor='rgba(0,0,0,0)',
        #     paper_bgcolor='rgba(0,0,0,0)'
        # )
        # Convert Plotly figure to HTML
        html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        # Set the width and height of the plot in the HTML content

        # Load the HTML content into the QWebEngineView
        self.webEngineView.setHtml(html)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
