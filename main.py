from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from hospital_database import HospitalDatabase
from point_of_sale import POS
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create the database object
        self.db = HospitalDatabase()
        
        # Create the point of sale widget
        self.pos = POS()
        
        # Add the point of sale widget to the main window
        self.setCentralWidget(self.pos)
        
        # Create the menu bar and menu items
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_file)
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)
        save_as_action = QAction('Save As', self)
        save_as_action.setShortcut('Ctrl+Shift+S')
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        
    def new_file(self):
        # Clear the fields in the point of sale widget and the database
        self.pos.clear_fields()
        self.db.clear_data()
        
    def open_file(self):
        # Open a file dialog to select the database file to open
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Database', '', 'Database Files (*.db)')
        
        if file_path:
            # Load the data from the selected database file into the database object and point of sale widget
            self.db.load_data(file_path)
            self.pos.load_data(self.db.get_data())
            
    def save_file(self):
        # Save the data from the point of sale widget into the database object and save the database object to the current file
        data = self.pos.get_data()
        self.db.set_data(data)
        self.db.save_data()
        
    def save_file_as(self):
        # Save the data from the point of sale widget into the database object and open a file dialog to select the database file to save to
        data = self.pos.get_data()
        self.db.set_data(data)
        
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Database', '', 'Database Files (*.db)')
        
        if file_path:
            self.db.save_data(file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
