#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:38:54 2020

@author: jose
"""


import random

for tirada in range (5):
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    dado3=random.randint(1,6)
    dado4=random.randint(1,6)
    print('El resultado de tu tirada ha sido '+str(dado1)+str(dado2)+str(dado3)+str(dado4))