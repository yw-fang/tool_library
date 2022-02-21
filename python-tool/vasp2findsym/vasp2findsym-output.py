#!/usr/bin/python
# -*- coding: utf-8 -*-
#contributor: Yue-Wen Fang
#DATE: 2022 Feb 21 
"""
Revised based on POSCAR2findsym.py first creaetd by Emre S. Tasci <e.tasci@tudelft.nl>                    *
   A simple python code that parses the POSCAR file,
   prepares an input file for Harold Stokes' findsym
   (http://stokes.byu.edu/isotropy.html)
   executable.

   Then, checks the current system to see if findsym is
   accessible: if it is, then feeds the prepared file 
   and directly outputs the result; if findsym is not 
   executable then outputs the generated input file.

   If you are interested only in the results section of 
   the findsymm output, you should append "| grep "\-\-\-\-\-\-" -A1000"
   to the execution of this code.

   Accepts alternative POSCAR filename for argument
   (default = POSCAR)

   If a second argument is proposed then acts as if
   findsym is not accessible (ie, prints out the input
   file instead of feeding it to findsymm)

                                             10/03/09 */
"""

import sys
import re
from numpy import *
from os import popen
import commands

force_output = False

if len(sys.argv)<2:
    filename="POSCAR"
elif len(sys.argv)<3:
    filename=sys.argv[1]
else:
    filename=sys.argv[1]
    force_output = True

f = open(filename,'r')

title = f.readline().strip()
tolerance = 0.00001
latt_vec_type = 1 # We will be specifying in vectors

f.readline() # Read Dummy
lat_vec = array([])
for i in range(0,3):
    lat_vec = append(lat_vec,f.readline().strip())

# Read atom species
species_count = f.readline()
species_count = re.split('[\ ]+', species_count.strip())
species_count = map(int,species_count)
number_of_species = len(species_count)
total_atoms = sum(species_count)

initial_guess = "P" # For the centering

species_designation = array([])
for i in range(1,number_of_species+1):
    for j in range(0,species_count[i-1]):
        species_designation = append(species_designation,i)

species_designation = map(str,map(int,species_designation))
# print species_designation
sep = " "
# print sep.join(species_designation)

# Read Coordinates
f.readline() # Read Dummy
pos_vec = array([])
for i in range(0,total_atoms):
    pos_vec = append(pos_vec,f.readline().strip())

# print pos_vec

findsym_input = array([])
findsym_input = append(findsym_input, title)
findsym_input = append(findsym_input, tolerance)
findsym_input = append(findsym_input, latt_vec_type)
findsym_input = append(findsym_input, lat_vec)
findsym_input = append(findsym_input, 2)
findsym_input = append(findsym_input, initial_guess)
findsym_input = append(findsym_input, total_atoms)
findsym_input = append(findsym_input, species_designation)
findsym_input = append(findsym_input, pos_vec)
# print findsym_input
sep = "\n"
findsym_input_txt = sep.join(findsym_input)
# print findsym_input_txt

# Check if findsym is accessible:
status,output =  commands.getstatusoutput("echo \"\n\n\"|findsym ")
if(output.find("command not found")!=-1 or force_output):
    # if it is not there, then just output the input
    print findsym_input_txt
elif(status==6144):
    # feed it to findsym
    pipe = popen("echo \""+findsym_input_txt+"\" | findsym").readlines()
    for line in pipe:
        print line.strip()
quit()
