from paramiko import SSHClient, AutoAddPolicy


class SSHUtil(object):
    def __init__(self, host, port=22, username=None, password=None, no_auth=False):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.no_auth = no_auth

    def client(self, command):
        s = SSHClient()
        if self.no_auth is True:
            s.set_missing_host_key_policy(AutoAddPolicy())
        else:
            s.load_system_host_keys()

        s.connect(self.host, self.port)
        stdin, stdout, stderr = s.exec_command(command)
        return stdout.read()
        s.close()


# hosts = ["node-%.2d.local" % i for i in range(1, 11)]
# for h in hosts:
#     c = SSHUtil(host=h, no_auth=True)
#     s = c.client(command="cat /var/log/inblogs/inblog")
#     result = s.decode("utf-8")
#     with open("sample_log", "a+") as lout:
#         lout.write(result)
