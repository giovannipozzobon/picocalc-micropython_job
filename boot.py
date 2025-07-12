#

#  Micropython Libraries
import builtins
import gc
import os
import sd_chk
import sys
import time

#  Secondary Libraries
from enhanced_sd import initsd, killsd, check_real_sd, show_sd_info
from checksd import checksd
from mkdir import mkdir
from flush import flush
from pye import pye_edit
import vt

#  PicoCalc
import picocalc
from picocalc.core import PicoDisplay, PicoKeyboard
from picocalc.system import run, files
from picocalc.system import memory, disk
import vt


#  Update System Path
paths_to_add = ["/sd/py_scripts"]
for path in paths_to_add:
    if path not in sys.path:
        sys.path.insert(0, path)


try:
    # Initialize basic hardware first
    pc_display = PicoDisplay(320, 320)
    pc_keyboard = PicoKeyboard()

    # Setup debugging
    _usb = sys.stdout
    def usb_debug(msg):
        if isinstance(msg, str):
            _usb.write(msg)
        else:
            _usb.write(str(msg))
        _usb.write('\r\n')
    picocalc.core.usb_debug = usb_debug

    # Run garbage collection before SD card init
    gc.collect()
    usb_debug("Starting SD card initialization...")

    # Mount SD card to /sd with extra delay for stability
    time.sleep_ms(900)  # Add delay before SD init
    sd = initsd(debug=True)  # Enable debug output

    # Check if SD was initialized properly
    if sd:
        usb_debug("SD card initialized successfully")
        # Verify it's the real SD card with full capacity
        if check_real_sd():
            usb_debug("Full capacity SD card detected")
        else:
            usb_debug("WARNING: SD card capacity seems wrong")
    else:
        usb_debug("SD card initialization failed!")

    # Give a moment for SD card to stabilize
    time.sleep_ms(900)

    # Continue with terminal and rest of setup
    pc_terminal = vt.vt(pc_display, pc_keyboard, sd=sd)

    picocalc.core.display  = pc_display
    picocalc.core.keyboard = pc_keyboard
    picocalc.core.terminal = pc_terminal
    picocalc.core.sd       = sd

    def edit(*args, tab_size=2, undo=50):
        # Dry the key buffer before editing
        pc_terminal.dryBuffer()
        return pye_edit(args, tab_size=tab_size, undo=undo, io_device=pc_terminal)
    picocalc.core.edit = edit

    os.dupterm(pc_terminal)

    # Run the standard SD check function
    sd_status, sd_msg = checksd()
    usb_debug(f"SD check: {sd_msg}")

    # Start main menu
    from py_run import main_menu
    main_menu()

    usb_debug( 'Finished Main Menu' )

except Exception as e:
    import sys
    sys.print_exception(e)
    try:
        os.dupterm(None).write(b"[boot.py error]\n")
    except:
        pass
