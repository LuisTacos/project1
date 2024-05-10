from gui_voting import *
from PyQt6.QtWidgets import *
class Logic(QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.name1_count = 0
        self.name2_count = 0

        self.voteButton.clicked.connect(self.submit)
        self.clearButton.clicked.connect(self.clear)
    def submit(self):
        if self.name1.isChecked():
            self.name1_count += 1
        elif self.name2.isChecked():
            self.name2_count += 1
        else:
            self.result_label.setText("Please select an option.")

        result_label_text = (
            f'VOTING RESULTS:\n'
            f'{self.name1.text()}: {self.name1_count}\n'
            f'{self.name2.text()}: {self.name2_count}'
        )
        self.result_label.setText(result_label_text)

    def clear(self):
        self.name1_count = 0
        self.name2_count = 0
        result_label_text = (
            f'VOTING RESULTS:\n'
            f'{self.name1.text()}: {self.name1_count}\n'
            f'{self.name2.text()}: {self.name2_count}'
        )
        self.result_label.setText(result_label_text)

