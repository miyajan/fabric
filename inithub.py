import socket

from fabric.api import cd, env, execute
from fabric.contrib.files import append
from fabric.utils import puts

env.hosts = ['172.29.1.67']

env.user = 'cybozu'
env.password = 'cybozu'

FABRIC_PATH = "/cygdrive/c/Users/cybozu/Desktop/fabric"

def appendAddress():
    puts("appendAddress: " + env.host)
    address = socket.gethostbyname(socket.gethostname())
    puts("address: " + address)
    with cd(FABRIC_PATH):
        append("hub.conf", address)

def inithub():
    execute(appendAddress)
