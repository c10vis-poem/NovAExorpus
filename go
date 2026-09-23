#!/bin/sh
set -e
U=https://raw.githubusercontent.com/c10vis-poem/NovAExorpus/tablet-scripts/Scripts
cd "$HOME"
wget -q -O install-dsh-alpine.sh "$U/install-dsh-alpine.sh"
wget -q -O install-openwiki-alpine.sh "$U/install-openwiki-alpine.sh"
sh install-dsh-alpine.sh
sh install-openwiki-alpine.sh
