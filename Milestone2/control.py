from PyQt4 import QtCore, QtGui,Qt
import sys
import view,model

class Controller(object):
     
   def __init__(self):
     self.model = model.Model()
     self.view = view.Ui_MainWindow(self)
     self.view.start()

   def exit(self):
     self.model.exit()

   def populate_appliances(self):
     appliances=[]
     links=[]
     appliances,links=self.model.populate_appliances()
     return appliances,links

   def install(self,host,user,passwd,app,link,port):
     self.model.install(host,user,passwd,app,link,port)

   def update_list(self):
     self.model.update_list()




if __name__ == "__main__" :
   controller = Controller()
