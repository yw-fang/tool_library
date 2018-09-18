#!/bin/bash
echo 'usage: get_relaxed_structure.sh relax.out'
echo 'Hence, you must have a output of relax calculations by Quantum Espresso pw.x'
# modify NR>=1 or NR>=4 for your own purpose

awk  '/Begin final coordinates/,/End final coordinates/{
        print $0
}' $1 |awk 'NR>=4 && !/End final coordinates/{print $0}' > structure-relaxed.dat

