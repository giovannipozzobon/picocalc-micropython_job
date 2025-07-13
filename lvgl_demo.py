
#  Micropython Libraries
import logging
import machine
import sys
import time

#  PicoCalc Libraries
import picocalc.core as pc

#  LVGL
import lvgl as lv


#  Setup Logger
logging.basicConfig( level = logging.INFO )

#------------------------------#
#-      Initialize LVGL       -#
#------------------------------#
logging.info( 'Initializing LVGL' )
lv.init()


#  Setup Temporary Working Memory
HRES,VRES=320,320

fb1 = bytearray( HRES * VRES * 3 )


if lv.COLOR.DEPTH!=16 or not lv.COLOR_16.SWAP:
    raise RuntimeError(f'LVGL *must* be compiled with 16bit color depth and swapped bytes (current: lv.COLOR.DEPTH={lv.COLOR.DEPTH}, lv.COLOR_16.SWAP={lv.COLOR_16.SWAP})')

is_fb1=True
def disp_drv_flush_cb( disp_drv, area, color ):

    global display
    global is_fb1
    global fb1

    logging.info( f'disp_drv_flush_cb: {area.x1}, {area.x2}, {area.y1}, {area.y2}' )
    fb = memoryview(fb1)


    pc.display.blit( area.x1, area.y1,
                     w:=(area.x2-area.x1+1),
                     h:=(area.y2-area.y1+1),
                     fb[0:2*w*h],
                     is_blocking = True ) # is_blocking=False)

    if disp_drv.flush_is_last():
        logging.info('FLUSH READY')
        disp_drv.flush_ready()
    logging.info('disp_drv_flush_cb done')


#-------------------------------------#
#-      Display Drawing Function     -#
#-------------------------------------#
disp_draw_buf = lv.disp_draw_buf_t()
disp_draw_buf.init( fb1, None, len(fb1) // lv.color_t.__SIZE__)

#----------------------------------------#
#-      Configure Display Driver        -#
#----------------------------------------#
logging.info( 'driver' )
disp_drv=lv.disp_drv_t()
disp_drv.init()

disp_drv.draw_buf = disp_draw_buf
disp_drv.flush_cb = disp_drv_flush_cb
disp_drv.hor_res  =  HRES
disp_drv.ver_res  =  VRES
disp_drv.register()



def lv_run(timeout_ms=1000,period_ms=10):
    t0=time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(),t0)<timeout_ms:
        print('.')
        tt0=time.ticks_ms()
        lv.task_handler()
        dt=time.ticks_ms()-tt0
        if period_ms>dt:
            time.sleep_ms(period_ms-dt)
            lv.tick_inc(period_ms)
        else: lv.tick_inc(dt)

def cb_btn(event):
    logging.info( "Hello World!" )

# this crashes with MemoryError or freezes... why?
logging.info('lv.obj()')
scr=lv.obj()
logging.info('... okay!')
btn=lv.btn(scr)
lbl=lv.label(btn)
lbl.set_text("Press me!")
btn.center()

btn.add_event_cb(cb_btn,lv.EVENT.CLICKED,None)
lv.scr_load(scr)
lv_run(10_000)

