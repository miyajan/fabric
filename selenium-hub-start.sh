#!/bin/bash

set -x

BASEDIR=$(cd $(dirname $0); pwd)
cd $BASEDIR

pkill java
java -jar selenium-server-standalone-*.jar -Xmx2g -role hub -hubConfig hubconfig.json &
