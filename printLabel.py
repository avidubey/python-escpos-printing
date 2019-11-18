#!/usr/bin/python

from escpos.printer import Usb #printer driver

p = Usb(0x0416, 0x5011, 0 , 0x81, 0x01)
p.text(" Hello World\n")
p.cut()
