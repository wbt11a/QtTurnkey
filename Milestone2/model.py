import sys,os
import sshconnect

class Model(object):

    def exit(self):
        currentdir = os.path.dirname(os.path.realpath(__file__))
        files = os.listdir(currentdir)
        for file in files:
            if file.endswith(".pyc"):
                os.remove(os.path.join(currentdir,file))
            if file.endswith("~"):
                os.remove(os.path.join(currentdir,file))
            if file.endswith(".swp"):
                os.remove(os.path.join(currentdir,file))
        sys.exit()

    def populate_appliances(self):
        names=[]
        temp=[]
        links=[]
        with open('appliances.txt','r') as f:
            contents = f.readlines() 
            for element in contents:
                if element != '\n':
                    names.append(element.split('|')[0])
                    temp.append(element.split('|')[1])
        
        for x in temp:
            links.append(x.strip())
        
        return names,links
