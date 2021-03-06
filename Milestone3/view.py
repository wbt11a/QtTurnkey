from PyQt4 import QtCore, QtGui
import sys, About


app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    
    def __init__(self,control):
    	QtGui.QMainWindow.__init__(self)
        self.controller = control
        self.setupUi()
        self.appliances=[]
        self.links=[]
        self.fname=None
         
    def setupUi(self):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1038, 285)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton = QtGui.QCommandLinkButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.gridLayout.addWidget(self.commandLinkButton, 6, 5, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 4, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.frame)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.frame)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout.addWidget(self.lineEdit_7, 4, 1, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.frame)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout.addWidget(self.lineEdit_8, 2, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.frame)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.gridLayout.addWidget(self.comboBox_4, 2, 3, 1, 1)
        self.comboBox_7 = QtGui.QComboBox(self.frame)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.gridLayout.addWidget(self.comboBox_7, 3, 3, 1, 1)
        self.comboBox_10 = QtGui.QComboBox(self.frame)
        self.comboBox_10.setObjectName(_fromUtf8("comboBox_10"))
        self.gridLayout.addWidget(self.comboBox_10, 4, 3, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.frame)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_2, 1, 4, 1, 1)
        self.comboBox_5 = QtGui.QComboBox(self.frame)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_5, 2, 4, 1, 1)
        self.comboBox_8 = QtGui.QComboBox(self.frame)
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_8, 3, 4, 1, 1)
        self.comboBox_11 = QtGui.QComboBox(self.frame)
        self.comboBox_11.setObjectName(_fromUtf8("comboBox_11"))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.comboBox_11.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_11, 4, 4, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.frame)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_3, 1, 5, 1, 1)
        self.comboBox_6 = QtGui.QComboBox(self.frame)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_6, 2, 5, 1, 1)
        self.comboBox_9 = QtGui.QComboBox(self.frame)
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_9, 3, 5, 1, 1)
        self.comboBox_12 = QtGui.QComboBox(self.frame)
        self.comboBox_12.setObjectName(_fromUtf8("comboBox_12"))
        self.comboBox_12.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_12, 4, 5, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.frame)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_9.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout.addWidget(self.lineEdit_9, 1, 2, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.frame)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_10.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.gridLayout.addWidget(self.lineEdit_10, 2, 2, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.frame)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_11.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.gridLayout.addWidget(self.lineEdit_11, 3, 2, 1, 1)
        self.lineEdit_12 = QtGui.QLineEdit(self.frame)
        self.lineEdit_12.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.gridLayout.addWidget(self.lineEdit_12, 4, 2, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1038, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionUpdate_Apps = QtGui.QAction(MainWindow)
        self.actionUpdate_Apps.setObjectName(_fromUtf8("actionUpdate_Apps"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUpdate_Apps)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(_fromUtf8("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(myIcon)
        self.retranslateUi(MainWindow)
		
		####### Slot Actions########################
        QtCore.QObject.connect(self.actionUpdate_Apps, QtCore.SIGNAL(_fromUtf8("activated()")),self.update_list)
        QtCore.QObject.connect(self.commandLinkButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.install)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("activated()")), self.exit)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("activated()")), self.about)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked()")),self.boxClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "QtTurnKey Install Assistant", None))
        self.label.setText(_translate("MainWindow", "Turnkey Application", None))
        self.label_2.setText(_translate("MainWindow", "Virtualization Type", None))
        self.commandLinkButton.setText(_translate("MainWindow", "Install", None))
        self.checkBox.setText(_translate("MainWindow", "Load From File", None))
        self.lineEdit.setText(_translate("MainWindow", "Target Master IP", None))
        self.label_3.setText(_translate("MainWindow", "Connection Method", None))
        self.lineEdit_5.setText(_translate("MainWindow", "Login", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "VirtualBox", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "VMWare", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Xen", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "VirtualBox", None))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "VMWare", None))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Xen", None))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "VirtualBox", None))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "VMWare", None))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "Xen", None))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "VirtualBox", None))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "VMWare", None))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "Xen", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "SSH", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "SSH", None))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "SSH", None))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "SSH", None))
        self.lineEdit_9.setText(_translate("MainWindow", "Password", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionUpdate_Apps.setText(_translate("MainWindow", "Update Apps", None))
        self.populate_combos()

    def error_frame(self, display_message):
    	quit_msg = str(display_message)
        QtGui.QMessageBox.warning(self, 'Message', quit_msg)

         
    def populate_combos(self):
        self.appliances,self.links=self.controller.populate_appliances()
        self.myDict = dict(zip(self.appliances,self.links))
        self.comboBox.clear()
        self.comboBox.addItems(self.appliances)
        self.comboBox_4.clear()
        self.comboBox_4.addItems(self.appliances)
        self.comboBox_7.clear()
        self.comboBox_7.addItems(self.appliances)
        self.comboBox_10.clear()
        self.comboBox_10.addItems(self.appliances)

    def update(self):
        print "stub"

    def update_list(self):
    	self.error_frame("Updating.  This may take some time and UI will be unresponsive.")
        retval = self.controller.update_list()
        if int(retval) == 5:
        	self.error_frame("Update Complete.")
        else:
        	self.error_frame("There was an error in updating.")

    def exit(self):
        self.controller.exit()

    def about(self):
    	AboutWindow = QtGui.QDialog()
        myAbout = About.Ui_Dialog(self)
        myAbout.setupUi(AboutWindow)
        AboutWindow.exec_()

    def install(self):
        port = 22

       
        if(self.lineEdit.text() != "Target Master IP"):
        	if(self.lineEdit_5.text() != "Login"):
        		if(self.lineEdit_9.text()!="Password"):
        			self.controller.install(self.lineEdit.text(),self.lineEdit_5.text(),self.lineEdit_9.text(),self.comboBox.currentText(),self.myDict.get((str(self.comboBox.currentText())), 'Key not found'), port)
        		else:
        			self.error_frame("Error:  Please enter a password.")
        	else:
        		self.error_frame("Error:  Please enter a login.")
        else:
        	self.error_frame("Error:  Please enter a host.")
        
        if(self.lineEdit_2.text() !=""):
        	self.controller.install(self.lineEdit_2.text(),self.lineEdit_8.text(),self.lineEdit_10.text(),self.comboBox_4.currentText(),self.myDict.get((str(self.comboBox_4.currentText())), 'Key not found'), port)
        	print "sent " + self.lineEdit_2.text()
        if(self.lineEdit_3.text() !=""):
        	self.controller.install(self.lineEdit_3.text(),self.lineEdit_6.text(),self.lineEdit_11.text(),self.comboBox_7.currentText(),self.myDict.get((str(self.comboBox_7.currentText())), 'Key not found'), port)
        if(self.lineEdit_4.text() !=""):
        	self.controller.install(self.lineEdit_4.text(),self.lineEdit_7.text(),self.lineEdit_12.text(),self.comboBox_10.currentText(),self.myDict.get((str(self.comboBox_10.currentText())), 'Key not found'), port)
   
    	if(self.fname!=None):
    		myFile = open(str(self.fname),'r')
    		for line in myFile:
    			app = line.split(":")[3]
    			app = app + " "
    			self.controller.install(line.split(":")[0], line.split(":")[1], line.split(":")[2], line.split(":")[3], self.myDict.get((app),'Key not found'), port)
    			#[0]==host
    			#[1]==login
    			#[2]==password
    			#[3]==application
    			#fourth argument is the dictionary lookup of the url

    def boxClicked(self):
    	if self.checkBox.isChecked():
    		self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.')
    		

    def start(object):
        MainWindow.show()
        sys.exit(app.exec_())


