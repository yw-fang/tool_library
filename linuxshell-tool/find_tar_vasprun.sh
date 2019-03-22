# find vasprun.xml files and tar them, excluding those in gruneisen directories
find . -name vasprun.xml | tar --exclude gruneisen/*/vasprun.xml --exclude gruneisen/*/*/vasprun.xml --exclude gruneisen/*/*/*/vasprun.xml -cf vasprun.tar.gz -T -
