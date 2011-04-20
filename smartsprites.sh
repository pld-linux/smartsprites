#!/bin/sh

#
# Add extra JVM options here
#
OPTS="-Xms64m -Xmx256m"

exec java $OPTS org.carrot2.labs.smartsprites.SmartSprites "$@"
