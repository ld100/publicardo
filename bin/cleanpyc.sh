#!/bin/bash
var="$1"
if [ -z "$var" ]
then
 var="$PWD"
fi
echo "cleaning up directory: $var..."

FILES=`find $var -name "*.pyc" -or -name "*.orig" -or -name "~*" -or -name "*~"`

for filename in $FILES
do
 rm -rfv $filename
done
