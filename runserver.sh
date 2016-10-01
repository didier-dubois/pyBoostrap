#!/bin/sh
#
#

PORT=8088
DIR=`dirname $0`
cd $DIR

/usr/bin/python ./server.py $PORT #> /var/log/run.$USER.server.servers.log 2>&1

