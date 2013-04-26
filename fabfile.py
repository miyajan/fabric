# -*- coding: utf-8 -*-

from datetime import datetime
from fabric.api import cd, env, put, run, roles, execute
from fabric.utils import puts

def _get_servers(file_name):
    servers = map((lambda x: x.rstrip()), open(file_name, 'r').readlines())
    while(True):
        try:
            servers.remove("")
        except ValueError:
            break
    return servers

# hostが応答しないなどのときにエラーで落ちないようにする
env.skip_bad_hosts = True

env.roledefs = {
    'hub': _get_servers("hub.conf"),
    'node': _get_servers("node.conf")
}

env.user = 'cybozu'
env.password = 'cybozu'

FABRIC_PATH = "/cygdrive/c/Users/cybozu/Desktop/fabric"
SELENIUM_PATH = "/cygdrive/c/Users/cybozu/Desktop/selenium"


@roles('hub')
def updateHub():
    puts("updateHub: " + env.host)
    with cd(SELENIUM_PATH):
        line = run("ps -af | grep java | wc -l")
        puts("line: " + line)
        processExists = int(line) > 0
        puts("processExists: " + str(processExists))
        if processExists:
            run("./selenium-hub-stop.sh")
        run("rm -f selenium-server-standalone-*.jar")
        run("rm -f hubconfig.json")
        run("rm -f inithub.py")
        run("rm -f inithub.bat")
        run("rm -f selenium-hub-*")
    with cd(FABRIC_PATH):
        put("selenium-server-standalone-*.jar", SELENIUM_PATH)
        put("hubconfig.json", SELENIUM_PATH)
        put("inithub.py", SELENIUM_PATH)
        put("inithub.bat", SELENIUM_PATH)
        put("selenium-hub-start.bat", SELENIUM_PATH)
        put("selenium-hub-start.sh", SELENIUM_PATH)
        put("selenium-hub-stop.bat", SELENIUM_PATH)
        put("selenium-hub-stop.sh", SELENIUM_PATH)
    with cd(SELENIUM_PATH):
        if processExists:
            run("./selenium-hub-start.sh")

@roles('node')
def updateNode():
    puts("updateNode: " + env.host)
    with cd(SELENIUM_PATH):
        line = run("ps -af | grep java | wc -l")
        puts("line: " + line)
        processExists = int(line) > 0
        puts("processExists: " + str(processExists))
        if processExists:
            run("./selenium-node-stop.sh")
        run("rm -f selenium-server-standalone-*.jar")
        run("rm -f chromedriver.exe")
        run("rm -f IEDriverServer.exe")
        run("rm -f nodeconfig.json")
        run("rm -f initnode.py")
        run("rm -f initnode.bat")
        run("rm -f selenium-node-*")
    with cd(FABRIC_PATH):
        put("selenium-server-standalone-*.jar", SELENIUM_PATH)
        put("chromedriver.exe", SELENIUM_PATH)
        put("IEDriverServer.exe", SELENIUM_PATH)
        put("nodeconfig.json", SELENIUM_PATH)
        put("initnode.py", SELENIUM_PATH)
        put("initnode.bat", SELENIUM_PATH)
        put("selenium-node-start.bat", SELENIUM_PATH)
        put("selenium-node-start.sh", SELENIUM_PATH)
        put("selenium-node-stop.bat", SELENIUM_PATH)
        put("selenium-node-stop.sh", SELENIUM_PATH)
    with cd(SELENIUM_PATH):
        run("PATH=/cygdrive/c/Python27/Scripts:$PATH fab -f initnode.py initNodeConfig")
        if processExists:
            run("./selenium-node-start.sh")

def updateAll():
    start = datetime.now()
    execute(updateHub)
    execute(updateNode)
    end = datetime.now()
    puts("updateAll execution time: " + str(end - start))
