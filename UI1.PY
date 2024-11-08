
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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

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
        self.graphicsView.setGeometry(QtCore.QRect(1090,520,750,450))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setStyleSheet("""
            background-color: rgba(255, 255, 255, 80);
            border: 4px solid #277ECD;
            border-radius: 10px;
            border-radius: 20px;                          
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

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 250, 231, 71))
        self.pushButton_4.setObjectName("pushButton_3")
        self.pushButton_4.setStyleSheet("background-color: rgba(39, 126, 205, 200); color: white; border-radius: 10px;")
        
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(320,40,750,450))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_3.setStyleSheet("""
            background-color: rgba(255, 255, 255, 80);
            border: 4px solid #277ECD;
            border-radius: 10px;
            border-radius: 20px;                          
        """)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(1090, 40,750,450))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_4.setStyleSheet("""
            background-color: rgba(255, 255, 255, 80);
            border: 4px solid #277ECD;
            border-radius: 10px;
            border-radius: 20px;                          
        """)
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_5.setGeometry(QtCore.QRect(320,520,750,450))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.graphicsView_5.setStyleSheet("""
            background-color: rgba(255, 255, 255, 80);
            border: 4px solid #277ECD;
            border-radius: 10px;
            border-radius: 20px;                          
        """)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1900, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        print("In UI3")
        MainWindow.setStatusBar(self.statusbar)

        #Radar Map
        graphics_layout0 = QVBoxLayout(self.graphicsView_3)
        self.plot_frame0 = QtWidgets.QFrame()
        self.plot_frame0.setObjectName("plot_frame")
        self.plot_frame0.setGeometry(QtCore.QRect(0, 0, 800, 400))
        self.webEngineView0 = QWebEngineView(self.plot_frame0)
        self.webEngineView0.setGeometry(QtCore.QRect(0, 0, 800, 400))
        graphics_layout0.addWidget(self.plot_frame0)
        self.create_radar_diagram_0()

        #Radar Map 2
        graphics_layout1 = QVBoxLayout(self.graphicsView_4)
        self.plot_frame1 = QtWidgets.QFrame()
        self.plot_frame1.setObjectName("plot_frame")
        self.plot_frame1.setGeometry(QtCore.QRect(0, 0, 800, 400))
        self.webEngineView1 = QWebEngineView(self.plot_frame1)
        self.webEngineView1.setGeometry(QtCore.QRect(0, 0, 800, 400))
        graphics_layout1.addWidget(self.plot_frame1)
        self.create_radar_diagram_1()
        #Middle Draw
        graphics_layout2 = QVBoxLayout(self.graphicsView_5)
        self.plot_frame2 = QtWidgets.QFrame()
        self.plot_frame2.setObjectName("plot_frame")
        self.plot_frame2.setGeometry(QtCore.QRect(0, 0, 800, 400))
        self.webEngineView2 = QWebEngineView(self.plot_frame2)
        self.webEngineView2.setGeometry(QtCore.QRect(0, 0, 800, 400))
        graphics_layout2.addWidget(self.plot_frame2)
        self.create_sankey_diagram1()

                #Middle Draw
        graphics_layout3 = QVBoxLayout(self.graphicsView)
        self.plot_frame3 = QtWidgets.QFrame()
        self.plot_frame3.setObjectName("plot_frame")
        self.plot_frame3.setGeometry(QtCore.QRect(0, 0, 800, 400))
        self.webEngineView3 = QWebEngineView(self.plot_frame3)
        self.webEngineView3.setGeometry(QtCore.QRect(0, 0, 800, 400))
        graphics_layout3.addWidget(self.plot_frame3)
        self.create_sankey_diagram0()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "DASHBOARD"))
        self.pushButton_2.setText(_translate("MainWindow", "ADD DATA"))
        self.pushButton_3.setText(_translate("MainWindow", "ALERT"))
        self.pushButton_4.setText(_translate("MainWindow", "Sankey"))

    def create_radar_diagram_0(self):
        mac_data = pd.read_excel('WaterData.xlsx')
        df = pd.DataFrame(mac_data)

        # Preprocess the date column
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
        df['Month'] = df['Date'].dt.to_period('M')
        df_monthly = df.groupby('Month').sum(numeric_only=True).reset_index()
        df_monthly['Month'] = df_monthly['Month'].astype(str)

        title = 'Monthly Comparison of Extraction Points'# Replace with your actual column names
        df = df_monthly
        # Melt the DataFrame
        points = extraction_points
        df_melted = df.melt(id_vars=['Month'], value_vars=points, var_name='Point', value_name='Value')

        # Create the bar plot using Plotly
        # title = "Monthly Values by Point"
        fig = px.bar(df_melted, x='Month', y='Value', color='Point', title=title)

# Customize the layout
        fig.update_layout(
    xaxis_title='Month',
    yaxis_title='Value',
    legend_title='Point',
    xaxis_tickangle=-45
        )

        html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        # Set the width and height of the plot in the HTML content
    

        # Load the HTML content into the QWebEngineView
        self.webEngineView0.setHtml(html)

    def create_radar_diagram_1(self):
        mac_data = pd.read_excel('WaterData.xlsx')
        df = pd.DataFrame(mac_data)

        # Preprocess the date column
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
        df['Month'] = df['Date'].dt.to_period('M')
        df_monthly = df.groupby('Month').sum(numeric_only=True).reset_index()
        df_monthly['Month'] = df_monthly['Month'].astype(str)

        title = 'Monthly Comparison of Usage Points'# Replace with your actual column names
        df = df_monthly
        # Melt the DataFrame
        points = usage_points
        df_melted = df.melt(id_vars=['Month'], value_vars=points, var_name='Point', value_name='Value')

        # Create the bar plot using Plotly
        # title = "Monthly Values by Point"
        fig = px.bar(df_melted, x='Month', y='Value', color='Point', title=title)

# Customize the layout
        fig.update_layout(
    xaxis_title='Month',
    yaxis_title='Value',
    legend_title='Point',
    xaxis_tickangle=-45
        )

        html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        # Set the width and height of the plot in the HTML content
    

        # Load the HTML content into the QWebEngineView
        self.webEngineView1.setHtml(html)

    def create_sankey_diagram0(self):
        mac_data = pd.read_excel('WaterData.xlsx')
        df = pd.DataFrame(mac_data)
        points = extraction_points
        sums = df[points].sum()

        # Create the pie chart using Plotly
        title = "Distribution of Extraction Points"
        fig = px.pie(values=sums, names=points, title=title, hole=0.0)

        # Customize the layout
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(showlegend=True)

        # Convert Plotly figure to HTML
        html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        # Set the width and height of the plot in the HTML content
    

        # Load the HTML content into the QWebEngineView
        self.webEngineView3.setHtml(html)

    def create_sankey_diagram1(self):
        mac_data = pd.read_excel('WaterData.xlsx')
        df = pd.DataFrame(mac_data)
        points = usage_points
        sums = df[points].sum()

        # Create the pie chart using Plotly
        title = "Distribution of Usage Points"
        fig = px.pie(values=sums, names=points, title=title, hole=0.0)

        # Customize the layout
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(showlegend=True)

        # Convert Plotly figure to HTML
        html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        # Set the width and height of the plot in the HTML content
    

        # Load the HTML content into the QWebEngineView
        self.webEngineView2.setHtml(html)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
