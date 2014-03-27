import paramiko
import sys
#import base64
#import getpass
import socket


class SshConnect():
  
    def __init__(self,user,passwd):
        self.port =6670 
        self.username = user
        self.password = passwd
        self.nbytes = 4096

    
    def test(self,hostname):
        x=0
        while x < len(hostname):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                s.connect((hostname[x],self.port))
                print hostname[x] + " is up"
                x+=1
            except socket.error as e:
                print "Error on connect: %s" % e
                print hostname[x] + " is getting removed."
                hostname.remove(hostname[x])
                x+=1
        s.close()
        return hostname

    def connect(self,hostname,command):
        hostname = self.test(hostname)
        x = 0
        while x < len(hostname):
            print "Issuing command to " + hostname[x] + "\n"
            client = paramiko.Transport((hostname[x], self.port))
            client.connect(username=self.username, password=self.password)
            
            stdout_data = []
            stderr_data = []
            session = client.open_channel(kind='session')
            session.exec_command(command)
            
            while True:
                if session.recv_ready():
                    stdout_data.append(session.recv(self.nbytes))
                if session.recv_stderr_ready():
                    stderr_data.append(session.recv_stderr(self.nbytes))
                if session.exit_status_ready():
                    break

            print 'exit status: ', session.recv_exit_status()
            print ''.join(stdout_data)
            print ''.join(stderr_data)

            session.close()
            client.close()
            x+=1

if __name__ == "__main__":
    hosts = ['172.19.48.160']
    user = "beaty"
    passwd = "abc123456"
    A = SshConnect(user,passwd)
    getextpack = "wget http://download.virtualbox.org/virtualbox/4.2.16/Oracle_VM_VirtualBox_Extension_Pack-4.2.16.vbox-extpack"
    installextpack = "echo " + passwd + " | sudo -S VBoxManage extpack install ./Oracle_VM_VirtualBox_Extension_Pack-4.2.16.vbox-extpack"
    mycommand = getextpack + " && " + installextpack
    A.connect(hosts,mycommand)
