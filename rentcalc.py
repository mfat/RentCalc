import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QFrame



class RentCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("محاسبه ‌گر رهن و اجاره")
        self.setLayoutDirection(Qt.RightToLeft)  # Set layout direction to right-to-left

        # Total property price
        total_price_label = QLabel("قیمت ملک:")
        total_price_label.setAlignment(Qt.AlignRight)
        self.total_price_input = QLineEdit()

        # Total security deposit
        self.security_deposit_label = QLabel("رهن کامل (برابر با یک هشتم ارزش ملک):")
        self.security_deposit_output = QLabel()

        # Change Deposit label
        change_deposit_label = QLabel("تغییر <b>ودیعه</b>")
        total_price_label.setAlignment(Qt.AlignRight)
        change_deposit_label.setStyleSheet("color: blue; font-weight: bold;")

        # Deposit input
        deposit_label = QLabel("ودیعه:")
        self.deposit_input = QLineEdit()

        # Monthly rent input
        monthly_rent_label = QLabel("اجاره ماهانه:")
        self.monthly_rent_input = QLineEdit()

        # Calculate rent button
        calculate_rent_button = QPushButton("اجاره را محاسبه کن")
        calculate_rent_button.clicked.connect(self.calculate_rent)

        # Rent input
        rent_label = QLabel("اجاره ماهانه:")
        self.rent_input = QLineEdit()

        # Calculate deposit button
        calculate_deposit_button = QPushButton("ودیعه را محاسبه کن")
        calculate_deposit_button.clicked.connect(self.calculate_deposit)

        # Deposit output label
        deposit_output_label = QLabel("ودیعه:")
        self.deposit_output = QLineEdit()
        self.deposit_output.setReadOnly(True)

        # Change Rent label
        change_rent_label = QLabel("تغییر <b>اجاره</b>")
        change_rent_label.setStyleSheet("color: blue; font-weight: bold;")

        # Create grid layout
        grid = QGridLayout()
        grid.setSpacing(10)

        # Add widgets to grid layout
        grid.addWidget(total_price_label, 0, 0)
        grid.addWidget(self.total_price_input, 0, 1)
        grid.addWidget(self.security_deposit_label, 1, 0)
        grid.addWidget(self.security_deposit_output, 1, 1)
        grid.addWidget(change_deposit_label, 2, 0, 1, 2)
        grid.addWidget(deposit_label, 3, 0)
        grid.addWidget(self.deposit_input, 3, 1)
        grid.addWidget(calculate_rent_button, 4, 1)
        grid.addWidget(monthly_rent_label, 5, 0)
        grid.addWidget(self.monthly_rent_input, 5, 1)
        grid.addWidget(change_rent_label, 7, 0, 1, 2)
        grid.addWidget(rent_label, 8, 0)
        grid.addWidget(self.rent_input, 8, 1)
        grid.addWidget(calculate_deposit_button, 9, 1)
        grid.addWidget(deposit_output_label, 10, 0)
        grid.addWidget(self.deposit_output, 10, 1)

        # Set central widget and layout
        central_widget = QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)

        self.setGeometry(100, 100, 400, 300)
        self.show()

        # Set right alignment for labels
        total_price_label.setAlignment(Qt.AlignRight)
        self.security_deposit_label.setAlignment(Qt.AlignRight)
        change_deposit_label.setAlignment(Qt.AlignRight)
        deposit_label.setAlignment(Qt.AlignRight)
        monthly_rent_label.setAlignment(Qt.AlignRight)
        rent_label.setAlignment(Qt.AlignRight)
        deposit_output_label.setAlignment(Qt.AlignRight)
        change_rent_label.setAlignment(Qt.AlignRight)

        # Set right alignment for outputs
        self.security_deposit_output.setAlignment(Qt.AlignRight)
        self.deposit_output.setAlignment(Qt.AlignRight)
        self.monthly_rent_input.setAlignment(Qt.AlignRight)
        self.rent_input.setAlignment(Qt.AlignRight)
        self.deposit_input.setAlignment(Qt.AlignRight)



    def calculate_rent(self):
        try:
            total_price = int(self.total_price_input.text().replace(",", ""))
            self.total_security_deposit = total_price / 8
            self.security_deposit_output.setText("{:,.0f}".format(self.total_security_deposit))
            deposit = int(self.deposit_input.text().replace(",", ""))
            if deposit > self.total_security_deposit:
                deposit = self.total_security_deposit
                self.deposit_input.setText("{:,}".format(deposit))
            monthly_rent = (self.total_security_deposit - deposit) / 30.303030303030303
            self.monthly_rent_input.setText("{:,.0f}".format(monthly_rent))
        except ValueError:
            pass

    def calculate_deposit(self):
        try:
            rent = int(self.rent_input.text().replace(",", ""))
            deposit = self.total_security_deposit - (rent * 30.303030303030303)
            self.deposit_output.setText("{:,.0f}".format(deposit))
        except ValueError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = RentCalculator()
    sys.exit(app.exec_())
