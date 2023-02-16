from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox

class POS(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create the labels and input fields
        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()
        self.age_label = QLabel('Age:')
        self.age_input = QLineEdit()
        self.gender_label = QLabel('Gender:')
        self.gender_input = QLineEdit()
        self.address_label = QLabel('Address:')
        self.address_input = QLineEdit()
        self.phone_label = QLabel('Phone:')
        self.phone_input = QLineEdit()
        self.doctor_fee_label = QLabel('Doctor fee:')
        self.doctor_fee_input = QLineEdit()
        self.ward_fee_label = QLabel('Ward fee:')
        self.ward_fee_input = QLineEdit()
        self.medicine_fee_label = QLabel('Medicine fee:')
        self.medicine_fee_input = QLineEdit()
        self.total_label = QLabel('Total:')
        self.total_input = QLineEdit()
        self.total_input.setReadOnly(True)
        
        # Create the buttons
        self.calculate_button = QPushButton('Calculate')
        self.save_button = QPushButton('Save')
        self.clear_button = QPushButton('Clear')
        
        # Create the grid layout for the labels and input fields
        layout = QGridLayout()
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.name_input, 0, 1)
        layout.addWidget(self.age_label, 1, 0)
        layout.addWidget(self.age_input, 1, 1)
        layout.addWidget(self.gender_label, 2, 0)
        layout.addWidget(self.gender_input, 2, 1)
        layout.addWidget(self.address_label, 3, 0)
        layout.addWidget(self.address_input, 3, 1)
        layout.addWidget(self.phone_label, 4, 0)
        layout.addWidget(self.phone_input, 4, 1)
        layout.addWidget(self.doctor_fee_label, 5, 0)
        layout.addWidget(self.doctor_fee_input, 5, 1)
        layout.addWidget(self.ward_fee_label, 6, 0)
        layout.addWidget(self.ward_fee_input, 6, 1)
        layout.addWidget(self.medicine_fee_label, 7, 0)
        layout.addWidget(self.medicine_fee_input, 7, 1)
        layout.addWidget(self.total_label, 8, 0)
        layout.addWidget(self.total_input, 8, 1)
        
        # Create the horizontal layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.calculate_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)
        
        # Create the vertical layout for the labels, input fields, and buttons
        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(button_layout)
        
        # Set the main layout for the widget
        self.setLayout(main_layout)
        
        # Connect the signals and slots for the buttons
        self.calculate_button.clicked.connect(self.calculate_total)
        self.save_button.clicked.connect(self.save_data)
        self.clear_button.clicked.connect(self.clear_fields)
        
    def calculate_total(self):
        # Calculate the total based on the fees entered
        doctor_fee = float(self.doctor_fee_input.text())
        ward_fee = float(self.ward_fee_input.text())
        medicine_fee = float(self.medicine_fee_input.text())
        total = doctor_fee + ward_fee + medicine_fee
        self.total_input.setText(str(total))
        
    def save_data
