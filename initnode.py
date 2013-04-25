import socket

from fabric.api import cd, env, execute, local
from fabric.contrib.files import append
from fabric.utils import puts

env.hosts = ['172.29.1.67']

env.user = 'cybozu'
env.password = 'cybozu'

FABRIC_PATH = "/cygdrive/c/Users/cybozu/Desktop/fabric"
SELENIUM_PATH = "/cygdrive/c/Users/cybozu/Desktop/selenium"

def _getHubHost():
    return open("hubaddress.conf", 'r').readlines()[0].rstrip()

def appendAddress():
    puts("appendAddress: " + env.host)
    address = socket.gethostbyname(socket.gethostname())
    puts("address: " + address)
    with cd(FABRIC_PATH):
        append("node.conf", address)

def updateHubHost():
    hubAddress = _getHubHost()
    puts("hubAddress: " + hubAddress)
    with cd(SELENIUM_PATH):
        local('sed -i -r -e "s#%HUB_ADDRESS%#' + hubAddress + '#g" nodeconfig.json')

def initnode():
    execute(appendAddress)
    execute(updateHubHost)
