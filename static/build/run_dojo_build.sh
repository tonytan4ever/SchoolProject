#!/bin/bash
dojo-release-1.9.1-src/util/buildscripts/build.sh --profile project.profile.js
ln -s ./release/dojo ../../js/dojo
ln -s ./release/dojox ../../js/dojox
ln -s ./release/dijit ../../js/dijit

