# python
Python ports of my Max patches - using Olivier Bélanger's awesome pyo module for DSP.

LP_Analyzer.py - Run this python script in interactive mode with the command: python -i LP_Analyzer.py
The pyo module from Olivier Belanger is required - download at http://ajaxsoundstudio.com/software/pyo/
WHAT DOES THIS THING DO?
The MIDI Notes output by a Novation Launchpad do not increment sequentially when you cross rows. For some reason they put in big gaps of several MIDI numbers, so it does not ascend chromatically when you change from one row to the next. This code fixes that and just gives you ascending note numbers from 0 to 63. ADDITIONALLY, it converts the MIDI numbers into a coordinate compatible with MONOME GRID applications. Super cool I know. The coordinate is extremely useful for mapping the launchpad quickly, or assigning sequencers to rows or all kinds of fun stuff.


