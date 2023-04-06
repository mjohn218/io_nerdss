''''
This is just a workspace to test the speed of functions. Has some NERDSS output files as tests.

NERDSS Output File Explanation:
 - histogram_single_component: (Normally called histogram_complexes_time.dat) is a histogram that shows the number of each type (type = how many monomers are in it) 
 of complex molecule at every time step in single-component NERDSS sim.
 - histogram_multi_component: (Normally called histogram_complexes_time.dat) is a histogram that shows the number of each type (type = how many monomers of each type are in it) 
 of complex molecule at every time step in multi-component NERDSS sim.
 - trajectory: i dont really know. I think shows the trajectories of the molecules in the simulation.
 - transition_matrix_time: idk
 - 1si4.pdb: describes info about hemogoblin??? (wow this list is not super helpful is it)
'''

from TestingFunctions.awful_tmr import badTimer
## CURRENTLY TESTING: hist.py
import numpy as np
import matplotlib.pyplot as plt
import ioNERDSS as ion





op = ion.real_PDB_separate_read(FileName="ioNERDSSPyPi\TestingFunctions\\1si4.pdb")

op = ion.real_PDB_separate_filter(op,["A","B","C"])

op = ion.real_PDB_separate_angle(op)

op = ion.real_PDB_separate_COM(op)
last = badTimer('Start',0)
op = ion.real_PDB_show_3D(op[0:5])
badTimer('Start',lastMeh)