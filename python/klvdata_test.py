#!/usr/bin/env python
import sys
import klvdata
for packet in klvdata.StreamParser(sys.stdin.buffer.read()):
    packet.structure()
