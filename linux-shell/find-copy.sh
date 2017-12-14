#!/bin/bash
#author: Y.-W. FANG
#contact: fyuewen@gmail.com
#purpose: find the file you need and copy it to other directory
#grammar: find path_A -name "*AAA*" -print0 | xargs -0 -I {} mv {} path_B
find . -name "*.py" -print0 | xargs -0 -I {} cp {} ./collect-script
find . -name "*.sh" -print0 | xargs -0 -I {} cp {} ./collect-script
