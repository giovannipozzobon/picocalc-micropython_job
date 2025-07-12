#!/usr/bin/env bash

#  Exit on the first error
set -e

#  Enter your "workspace" path here!
BASE_PATH='/Users/marvin/Desktop/Projects/workspace'

#  Eigen-Math path
#   - You should not need to adjust this, should you follow my README
MATH_PATH="${BASE_PATH}/eigenmath_micropython/micropython.cmake"

#  Micropython-ULAB Path
ULAB_PATH="${BASE_PATH}/micropython-ulab/code/micropython.cmake"

#  Display Driver Path
#   - You should not need to adjust this, should you follow my README
DISP_PATH="${BASE_PATH}/PicoCalc-micropython-driver/picocalcdisplay/micropython.cmake"

#  Terminal Path
#  - You should not need to adjust this, should you follow my README
TERM_PATH="${BASE_PATH}/PicoCalc-micropython-driver/vtterminal/micropython.cmake"

#  Run CMake on and generate makefiles
#  - Tested on macos, with `gcc-arm-embedded` per 6/14/2025
cmake .. -DUSER_C_MODULES="${MATH_PATH};${DISP_PATH};${TERM_PATH};${ULAB_PATH}" -DMICROPY_BOARD=RPI_PICO2_W

#  Run make
make -j
