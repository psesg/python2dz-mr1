#!/usr/bin/env python

import sys
import string
import random

reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

i = 1
rnd_num = random.randint(1, 5)
out_str = ""
while True:
    line = sys.stdin.readline()
    if line == '':
        if len(out_str) > 0:
            if out_str[-1] == ",":
                out_str = out_str[:-1]
            print "%s" % out_str
        break
    else:
        line = line.strip("\n")[10:]
        if i < rnd_num:
            out_str = out_str + line + ","
            i += 1
        elif i == rnd_num:
            out_str = out_str + line
            i += 1
        else:
            print "%s" % out_str
            # sys.stdout.write(out_str)
            i = 1
            rnd_num = random.randint(1, 5)
            out_str = ""
