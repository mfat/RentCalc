import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton


class RentCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rent Calculator")

        # Total property price
        self.total_price_label = QLabel("Total Property Price:", self)
        self.total_price_label.move(20, 20)
        self.total_price_input = QLineEdit(self)
        self.total_price_input.move(150, 20)

        # Calculate total security deposit
        self.total_security_deposit = 0

        # Change deposit section
        self.change_deposit_label = QLabel("Change Deposit", self)
        self.change_deposit_label.move(20, 60)

        # Deposit input
        self.deposit_label = QLabel("Deposit:", self)
        self.deposit_label.move(20, 90)
        self.deposit_input = QLineEdit(self)
        self.deposit_input.move(150, 90)

        # Monthly rent input
        self.monthly_rent_label = QLabel("Monthly Rent:", self)
        self.monthly_rent_label.move(20, 120)
        self.monthly_rent_input = QLineEdit(self)
        self.monthly_rent_input.move(150, 120)

        # Calculate rent button
        self.calculate_rent_button = QPushButton("Calculate Rent", self)
        self.calculate_rent_button.move(20, 160)
        self.calculate_rent_button.clicked.connect(self.calculate_rent)

        # Rent and deposit section
        self.change_rent_label = QLabel("Change Rent", self)
        self.change_rent_label.move(20, 200)

        # Rent input
        self.rent_label = QLabel("Rent:", self)
        self.rent_label.move(20, 230)
        self.rent_input = QLineEdit(self)
        self.rent_input.move(150, 230)

        # Calculate deposit button
        self.calculate_deposit_button = QPushButton("Calculate Deposit", self)
        self.calculate_deposit_button.move(20, 270)
        self.calculate_deposit_button.clicked.connect(self.calculate_deposit)

        # Deposit output label
        self.deposit_output_label = QLabel("Deposit:", self)
        self.deposit_output_label.move(20, 310)
        self.deposit_output = QLineEdit(self)
        self.deposit_output.move(150, 310)
        self.deposit_output.setReadOnly(True)

        self.setGeometry(100, 100, 400, 400)
        self.show()

    def calculate_rent(self):
        try:
            total_price = int(self.total_price_input.text().replace(",", ""))
            self.total_security_deposit = total_price / 8
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
