from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QComboBox, QLineEdit, QVBoxLayout, QLabel, QWidget
from styles import button
import sys
from converter import convert_currency


class CurrencyConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency Converter")
        self.setMinimumSize(300, 400)

        self.setStyleSheet('''
           QMainWindow {
               background-color: QLinearGradient(x0:0, y0:0, x1:0,y1:1, stop:0 #FFDEE9 , stop:1 #B5FFFC);
           }
           QComboBox {
               padding:10px;
               border:none;
               border-radius:10px;
               background-color: #f87171;
               color:white;
               font-weight: bold;
               font-family: Courier New, Courier, monospace;
           }
           QComboBox:hover {
               border:2px solid black;
           }
           QComboBox::drop-down {
               background-color: transparent;
           }
           QLineEdit {
               padding:10px;
               border:none;
               border-radius:10px;
               background-color: #fecaca;
               font-family: Courier New, Courier, monospace;
               font-weight: bold;
               color:black;
           }
           #convert_button {
               background-color: blue;
               border-radius:10px; 
               background-color:#059669;
               color: white;
               font-family: Courier New, Courier, monospace;
               font-weight: bold;
           }
           #show_converted_amount {
                color:#1e40af;
                font-weight: bold;
                font-size: 25px;
           } 
        ''')

        #widgets
        self.select_currency = QComboBox()
        currency_types = ["USD", "EUR", "JPY", "CNY", "XAF"]
        self.select_currency.addItems(currency_types)

        self.target_currency = QComboBox()
        currency_kinds = ["USD", "EUR", "JPY", "CNY", "XAF"]
        self.target_currency.addItems(currency_kinds)
        self.target_currency.setCurrentIndex(2)

        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Currency amount")

        convert_button = button.AnimatedButton(text="Convert")
        convert_button.setObjectName("convert_button")
        convert_button.clicked.connect(self.convert_currency)

        self.show_converted_amount = QLabel()
        self.show_converted_amount.setObjectName("show_converted_amount")

        parent_layout = QVBoxLayout()

        parent_layout.addWidget(self.select_currency)
        parent_layout.addWidget(self.target_currency)
        parent_layout.addWidget(self.amount)
        parent_layout.addWidget(convert_button)
        parent_layout.addWidget(self.show_converted_amount, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(parent_layout)

        self.setCentralWidget(central_widget)

    def convert_currency(self):
        select_cur = self.select_currency.itemText(self.select_currency.currentIndex())
        target_cur = self.target_currency.itemText(self.target_currency.currentIndex())
        user_amount = self.amount.text()
        convert_amount = convert_currency(select=select_cur, target=target_cur, amount=user_amount)
        self.show_converted_amount.setText(f"{convert_amount["target"]}: {convert_amount["amount"]}")


app = QApplication(sys.argv)
currency_converter = CurrencyConverter()
currency_converter.show()
sys.exit(app.exec())
