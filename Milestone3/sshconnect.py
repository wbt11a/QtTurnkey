import paramiko
import sys
import socket


class SshConnect():
  
    def __init__(self,user,passwd,port):
        self.port = port
        self.username = user
        self.password = passwd
        self.nbytes = 4096

    
    def test(self,hostname):

        try:   
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((hostname,self.port))
            print hostname + " is up"
            
        except socket.error as e:
            print "Error on connect: %s" % e
            print hostname + " is getting removed."
            s.close()
            hostname=None
        return hostname
        

    def connect(self,hostname,command):
        output=[]
        hostname = str(hostname)
        hostname = self.test(hostname)
        if hostname != None:
            print "Issuing command to " + hostname + "\n"
            client = paramiko.Transport((hostname, self.port))
            client.connect(username=self.username, password=self.password)
            stdout_data = []
            stderr_data = []
            session = client.open_channel(kind='session')
            session.exec_command(command)
                
            while True:
                if session.recv_ready():
                    stdout_data.append(session.recv(self.nbytes))
                    output.append(session.recv(self.nbytes))
                if session.recv_stderr_ready():
                    stderr_data.append(session.recv_stderr(self.nbytes))
                if session.exit_status_ready():
                    break

            print 'exit status: ', session.recv_exit_status()
            print ''.join(stdout_data)
            print ''.join(stderr_data)
            errors = session.recv_exit_status()
            output.append(stdout_data)
            output.append(stderr_data)

            session.close()
            client.close()
        
        if errors == 0:
            return hostname,errors
        else:
            return errors
       