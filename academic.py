#!/usr/bin/python
# -*- coding: utf-8 -*-

def getlist():
    liststr = """
scitation.org
acs.org
aps.org
iop.org
tandfonline.com
elsevier.com
sciencedirect.com
sciencemag.org
nature.com
pnas.org
"""
    return set(liststr.splitlines(False))
