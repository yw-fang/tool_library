#loop DFT jobs in disp-{00001..00111} folders for silicon
#this script can be used with phonopy and phono3py
for i in $(seq -s " " -f %05g 1 111);
do
	rm -rf disp-${i};
	mkdir disp-${i}; 
	cp POSCAR-${i}  disp-${i}/POSCAR;
	cd disp-${i};
	ln -s ../POTCAR .
	ln -s ../aiidasubmit.sh
	ln -s ../KPOINTS .
	ln -s ../INCAR .
	qsub aiidasubmit.sh
	cd ../
done
