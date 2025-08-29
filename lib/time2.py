#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#

#  Python Libraries
import time as _time

#  Constants
SECS_PER_MIN  = 60
SECS_PER_HOUR = 3600
SECS_PER_DAY  = 86400

CURRENT_TZ_OFFSET_HOURS = 0

def set_timezone_offset( hours ):
    global CURRENT_TZ_OFFSET_HOURS
    CURRENT_TZ_OFFSET_HOURS = hours

class struct_time:

    def __init__(self):
        self.tm_year  = None
        self.tm_mon   = None
        self.tm_mday  = None
        self.tm_hour  = None
        self.tm_min   = None
        self.tm_sec   = None
        self.tm_wday  = None
        self.tm_yday  = None
        self.tm_isdst = None

    def as_array(self):
        return [self.tm_year, self.tm_mon, self.tm_mday, self.tm_hour, self.tm_min, self.tm_sec, self.tm_wday, self.tm_yday, self.tm_isdst]

    def __str__(self):
      output = '( yr: ' + str(self.tm_year) + \
             ', mo: ' + str(self.tm_mon) + \
            ', mday: ' + str(self.tm_mday) + \
            ', hour: ' + str(self.tm_hour) + \
            ', min: ' + str(self.tm_min) + \
            ', sec: ' + str(self.tm_sec) + \
            ', wday: ' + str(self.tm_wday) + \
            ', yday: ' + str(self.tm_yday) + \
            ', isdst: ' + str(self.tm_isdst)
      return output

DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap_year( y ):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def days_in_month(y, m):
    # year, month -> number of days in that month in that year.
    if m == 2 and is_leap_year(y):
        return 29
    return DAYS_IN_MONTH[m]

def gmtime():

    #  Get the unix seconds
    lt = _time.localtime()

    #  Convert this to local time
    tm = struct_time()

    tm.tm_year = lt[0]
    tm.tm_mon  = lt[1]
    tm.tm_mday = lt[2]
    tm.tm_hour = lt[3] + CURRENT_TZ_OFFSET_HOURS
    tm.tm_min  = lt[4]
    tm.tm_sec  = lt[5]
    tm.tm_wday = lt[6]
    tm.tm_yday = lt[7]
    tm.tm_isdst = 0

    return tm

