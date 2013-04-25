import ConfigParser
import socket

from fabric.api import cd, env, execute, local
from fabric.contrib.files import append
from fabric.utils import puts

env.hosts = ['172.29.1.67']

env.user = 'cybozu'
env.password = 'cybozu'

FABRIC_PATH = "/cygdrive/c/Users/cybozu/Desktop/fabric"
SELENIUM_PATH = "/cygdrive/c/Users/cybozu/Desktop/selenium"


def appendAddress():
    puts("appendAddress: " + env.host)
    address = socket.gethostbyname(socket.gethostname())
    puts("address: " + address)
    with cd(FABRIC_PATH):
        append("node.conf", address)

def initNodeConfig():
    with cd(SELENIUM_PATH):
        conf = ConfigParser.SafeConfigParser()
        conf.read("node.ini")
        hubAddress = conf.get("node", "hubaddress")
        ieVersion = conf.get("node", "ieversion")
        puts("hubAddress: " + hubAddress)
        puts("ieVersion: " + ieVersion)
        local('sed -i -r -e "s#%HUB_ADDRESS%#' + hubAddress + '#g" nodeconfig.json')
        local('sed -i -r -e "s#%IE_VERSION%#' + ieVersion + '#g" nodeconfig.json')

def initnode():
    execute(appendAddress)
    execute(initNodeConfig)
