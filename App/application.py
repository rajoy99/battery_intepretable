import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from joblib import dump, load
rfr = load('RFRegressor.joblib')
import numpy as np
import sklearn

class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Battery Voltage Prediction App')
		self.resize(500, 420)

		layout = QGridLayout()

		label_cgrav = QLabel('<font size="6"> Capacity Grav </font>')
		self.lineEdit_cgrav = QLineEdit()
		self.lineEdit_cgrav.setPlaceholderText('Please enter your usercgrav')
		layout.addWidget(label_cgrav, 0, 0)
		layout.addWidget(self.lineEdit_cgrav, 0, 1)

		
		label_cvol = QLabel('<font size="6"> Capacity Vol </font>')
		self.lineEdit_cvol = QLineEdit()
		self.lineEdit_cvol.setPlaceholderText('Please enter your cvol')
		layout.addWidget(label_cvol, 1, 0)
		layout.addWidget(self.lineEdit_cvol, 1, 1)
  
		label_maxfrac = QLabel('<font size="6"> Max Frac </font>')
		self.lineEdit_maxfrac = QLineEdit()
		self.lineEdit_maxfrac.setPlaceholderText('Please enter your maxfrac')
		layout.addWidget(label_maxfrac, 2, 0)
		layout.addWidget(self.lineEdit_maxfrac, 2, 1)
  
		label_numsites = QLabel('<font size="6"> Numsites </font>')
		self.lineEdit_numsites = QLineEdit()
		self.lineEdit_numsites.setPlaceholderText('Please enter your numsites')
		layout.addWidget(label_numsites, 3, 0)
		layout.addWidget(self.lineEdit_numsites, 3, 1)

  





		self.label_res = QLabel('<font size="7"> Result</font>')
		layout.addWidget(self.label_res, 7, 1)
		

		button_login = QPushButton('Predict Average Voltage')
		button_login.clicked.connect(self.check_cvol)
		
		button_login.setStyleSheet("background-color: yellow")
		layout.addWidget(button_login, 5, 0, 1, 2)
		layout.setRowMinimumHeight(7, 75)

		self.setLayout(layout)

	def check_cvol(self):
		
		input_array=np.array([self.lineEdit_cgrav.text(),self.lineEdit_cvol.text(),self.lineEdit_maxfrac.text(),self.lineEdit_numsites.text()])
		input_array=input_array.astype(np.float32)
		
		ans=rfr.predict(input_array.reshape(1,4))
		ans=str(ans[0])
		self.label_res.setFont(QFont('Times', 18))
		self.label_res.setText("The predicted average voltage is : "+ans+" Volts")


if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = LoginForm()
	form.show()

	sys.exit(app.exec_())
