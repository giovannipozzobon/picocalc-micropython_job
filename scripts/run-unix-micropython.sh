#!/usr/bin/env bash

#  Where the micropython path is
MPY_PATH="${HOME}/Desktop/Projects/workspace/micropython/ports/unix/build-standard"

#  Copy Library Folder Over
rsync -avP  ./lib/ ~/.micropython/lib/


#  Launch Micropython
${MPY_PATH}/micropython
