from paramiko import SS


class SSHUtil(object):
    def __init__(self, host, port=22, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def client(self, command):
        s = SSHClient()
        s.load_system_host_keys()
        s.connect(self.host, self.port)
        stdin, stdout, stderr = s.exec_command(command)
        return {"in": stdin, "out": stdout, "err": stderr}
        s.close()
