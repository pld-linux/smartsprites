#!/bin/sh
set -e

# set JAVA_HOME from jpackage-utils if available
if [ ! -f /usr/share/java-utils/java-functions ]; then
	echo >&2 "jpackage-utils not found."
	exit 1
fi
. /usr/share/java-utils/java-functions

jars='smartsprites args4j commons-io commons-lang commons-math google-collections smartsprites'
for jar in $jars; do
	jar=$(find-jar $jar)
	CLASSPATH=$CLASSPATH:$jar
done

MAIN_CLASS=org.carrot2.labs.smartsprites.SmartSprites

# extra JVM options
OPTIONS="-Xms64m -Xmx256m"

exec run "$@"
