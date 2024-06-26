import xrfclk
from xrfclk import *  # expose all public functions
import re
import time


lmk_devices = []
lmx_devices = []

def set_ref_clks_fr(lmk_file, lmx_file, delay=2):
    """Set the LMK and LMX chips according to the provided register files.
    
    Wraps the functions from xrfclk package such that the clock tree settings
    can be passed via the locally available register value files (*.txt files).
    See the documentation for xrfclk for more details.
    
    Parameters
    ----------
    lmk_file: string
        File path to the LMK* register file
    lmx_file: string
        File path to the LMX* register file
    delay: int
        time delay after setting the clock tree.
        delay in seconds.
    """
    global lmk_devices, lmx_devices

    # initialize lmk_devices and lmx_devices list
    # check status of the list in xrfclk to clean up later
    xrfclk_list_empty = None
    if xrfclk.lmk_devices == [] and xrfclk.lmx_devices == []:
        xrfclk_list_empty = True
    else:
        xrfclk_list_empty = False

    # load the xrfclk_fr register if it exists already
    if lmk_devices == [] and lmx_devices == []:
        if xrfclk_list_empty:
            xrfclk._find_devices()  # initialize device list. Writes in xrfclk.*_devices
        lmk_devices = xrfclk.lmk_devices
        lmx_devices = xrfclk.lmx_devices
    else:
        xrfclk.lmk_devices = lmk_devices
        xrfclk.lmx_devices = lmx_devices

    lmk_regs = _read_tics_regfile(lmk_file)
    lmx_regs = _read_tics_regfile(lmx_file)

    for lmk in xrfclk.lmk_devices:
        xrfclk._write_LMK_regs(lmk_regs, lmk)

    for lmx in xrfclk.lmx_devices:
        xrfclk._write_LMX_regs(lmx_regs, lmx)

    # clean up to allow for register files to be copied and xrfclk.set_ref_clks() be called after this function if desired.
    xrfclk.lmk_devices = []
    xrfclk.lmx_devices = []
    
    time.sleep(delay)
    
def _read_tics_regfile(file):
    """Return the register values of the register file as a list.
    
    Reads from register value files and returns its values as a list.

    Parameters
    ----------
    file: string
        File path to the register value file (*.txt file)
        
    Returns
    -------
    registers: list
        List with register values.
    """
    registers = []
    with open(file, 'r') as f:
        lines = [l.rstrip("\n") for l in f]
        
        for i in lines:
            m = re.search('[\t]*(0x[0-9A-F]*)', i)
            registers.append(int(m.group(1), 16),)
            
    return registers