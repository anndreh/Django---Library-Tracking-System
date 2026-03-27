#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:11:21 2026

@author: andre
"""

import random

start = 1
end = 20
list_size = 10

random_int = [random.randint(start, end) for _ in range(list_size)]

print(random_int)