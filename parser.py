import os

class Host:
    def __init__(self, info_arr):
        cache = {}
        for item in info_arr:
            cache[item[0]] = item[1]
        self.host = cache["Host"]
        self.pubIp = cache["HostName"]
        self.user = cache["User"]
        self.idFile = cache["IdentityFile"]

    def __str__(self):
        return "\n".join([
            "Host: " + self.host, 
            "HostName: " + self.pubIp,
            "User: " + self.user, 
            "IdentityFile: " + self.idFile,
            ])


SSH_CONFIG_DIR = os.path.expanduser('~') + "/.ssh/config"

def host_parser():
    config = open(SSH_CONFIG_DIR, 'r')

    lines = config.readlines()
    hosts = []
    for i in range(len(lines)):
        if lines[i].strip(" ").split(" ")[0] == "Host":
            j = i + 1
            while (j < len(lines) and lines[j].strip(" ").split(" ")[0] != "Host"):
                j += 1
            res = [lines[k] for k in range(i, j)]
            hosts.append(Host([item.strip().split(" ") for item in res]))
    return hosts

    config.close()


for host in host_parser():
    print host





