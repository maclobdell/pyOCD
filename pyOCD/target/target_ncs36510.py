"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from cortex_m import CortexM
from .memory_map import (FlashRegion, RamRegion, MemoryMap)
import logging

# NRF51 specific registers
RESET = 0x40000544
RESET_ENABLE = (1 << 0)

class NCS36510(CortexM):

    memoryMap = MemoryMap(
        FlashRegion(    start=0x2000,           length=0x50000,      blocksize=0x800, isBootMemory=True),
        RamRegion(      start=0x3FFF4000,  length=0xC000)
        )

    def __init__(self, link):
        super(NCS36510, self).__init__(link, self.memoryMap)

    def resetn(self):
        """
        reset a core. After a call to this function, the core
        is running
        """
        """
        #Regular reset will kick NRF out of DBG mode
        logging.debug("target_nrf51.reset: enable reset pin")
        self.writeMemory(RESET, RESET_ENABLE)
        #reset
        logging.debug("target_nrf51.reset: trigger nRST pin")
        CortexM.reset(self)
        """
