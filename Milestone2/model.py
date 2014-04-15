import sys,os,subprocess
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
                    names.append(element.split(' : ')[0])
                    temp.append(element.split(' : ')[1])
        for x in temp:
            links.append(x.strip())
        
        return names,links


    def install(self,hostname,username,passwd,appliance,link,port):
        successful_hosts=[]
        appliance = str(appliance).strip()
        hostnames=[]
        hostnames.append(str(hostname))
        newCon = sshconnect.SshConnect(str(username),str(passwd),port)
        filename = link.split('/')[-1]
        directory = filename.replace(' ','')[:-8]
        
        
        #mycmd1 = "echo " + str(passwd) + " | sudo -S VBoxManage extpack uninstall VNC && wget -q -T 9999 " + link + " && unzip " + filename  
        mycmd1 = "unzip " + filename
        mycmd2 = "VBoxManage import " + directory + "/*.ovf --vsys 0 --vmname \"" + appliance  + "\""
        #print "sending: " + mycmd
        output1 = newCon.connect(hostnames,mycmd1)
        output2 = newCon.connect(hostnames,mycmd2)
        if output2 == 0:
            #startvm
            #in the future, change this to the list of successful virtual hosts
            startvm = "nohup VBoxHeadless --startvm &" + appliance
            ready2run = sshconnect.SshConnect(str(username),str(passwd),port)
            output2 = read2run.connect(hostnames,startvm)
        else:
            print output1
            print output2
            print "Error in initial setup on."
        #for item in output:
        #    print item
        #    print item[0], ', '.join(map(str,item[1:]))

    def update_list(self):
        p = subprocess.Popen(["python", "parser.py"])
        #sys.stdout.write("Waiting")
        #while(p.poll() is not None):
        #    sys.stdout.write('.')
        
