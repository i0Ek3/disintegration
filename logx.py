#!/usr/bin/env python
# coding=utf-8

import numpy as np
import rich as r

def logx(begin, end, base):
    arr = np.arange(begin, end)
    if base == 2:
        r.print(np.log2(arr))
    elif base == 10:
        r.print(np.log10(arr))
    else:
        r.print(np.log(arr))

