# `xrfclk-fileread` Package

This package extends the `xrfclk` driver package (https://github.com/Xilinx/PYNQ/tree/master/sdbuild/packages/xrfclk/package) to allow clock tree configuration using locally available register files (*.txt files).
The register files are passed by its file name.
No specific file name format required.

## Usage
LMK* and LMX* clocks are set by the function `set_ref_clks_fr`.

```python
import xrfclk_fileread as xrfclk

xrfclk.set_ref_clks_fr(lmk_file='LMK04208_122.88.txt', lmx_file='LMX2594_3932.16.txt')
```