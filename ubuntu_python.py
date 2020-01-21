#!/usr/bin/env python3

import os

stage = os.envirom["STAGE"].upper()

output = "We're running in " + stage

if stage.startwith("PROD"):
    output = "DANGER!!! - " + output

print(output)
