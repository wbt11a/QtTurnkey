import sys,os,subprocess,time, threading
import sshconnect, parser

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
                    names.append(element.split(' : ')[0])
                    temp.append(element.split(' : ')[1])
        for x in temp:
            links.append(x.strip())
        
        return names,links


    def install(self,hostname,username,passwd,appliance,link,port):
        try:
            threading.Thread(target = self.install_thread, args=(hostname,username,passwd,appliance,link,port), name='install_function').start()
        except:
            print "Threading failed."

      
    def install_thread(self,hostname,username,passwd,appliance,link,port):
        appliance = str(appliance).strip()
        newCon = sshconnect.SshConnect(str(username),str(passwd),port)
        filename = link.split('/')[-1]
        directory = filename.replace(' ','')[:-8]
               
        mycmd1 = "echo " + str(passwd) + " | sudo -S VBoxManage extpack uninstall VNC && wget -q -T 9999 " + link + " && unzip " + filename + " && VBoxManage import " + directory + "/*.ovf --vsys 0 --vmname \"" + appliance + "\" && " + "VBoxManage modifyvm " + "\"" + appliance + "\"" + " --ostype Debian_64 &&" +  " nohup bash -c \"VBoxHeadless --startvm \"" + appliance + "\"" + " > output.log &\""
        output1 = newCon.connect(hostname,mycmd1)

        print ("\n\nOutput (0 means successful): " + str(output1))


    def update_list(self):
        A = parser.Parser("http://www.turnkeylinux.org", "appliances.txt")
        retval = A.get_links("http://www.turnkeylinux.org/all")
        return retval

   
        