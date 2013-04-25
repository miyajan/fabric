#!/bin/bash

set -x

BASEDIR=$(cd $(dirname $0); pwd)
cd $BASEDIR

pkill java
java -jar  selenium-server-standalone-*.jar -Dwebdriver.chrome.driver=chromedriver.exe -Dwebdriver.ie.driver=IEDriverServer.exe -Xmx2g -role node -nodeConfig nodeconfig.json &
