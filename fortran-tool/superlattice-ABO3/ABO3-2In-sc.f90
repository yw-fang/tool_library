!Creating date: 20150525
!Author: Y.-W.FANG, fyuewen@gmail.com
!Affiliation: C.-G.Duan's Group at East China Normal Univ.
!Purpose: This code is used to generate M/N (001) interface, here M & N are both ABO3 peroveskite oxides with cubic of tetragonal sphase.
program main
implicit none

character(len=100)  :: cdump
real*16             :: ratio,pos(5,3),inv(3)
integer*8           :: i,j,natom

!new file
open(unit=1,file='POSCAR')
open(unit=2,file='POSCAR-supercell')

!read and write the lattice constants
do i=1,9
   read(1,'(A66)') cdump
   write(2,'(A66)') cdump
enddo

!read the c/a ratio
write(*,*) 'Input the c/a ratio:'
read(*,*) ratio

!read the position of ions
do i=1,5
   read(1,'(3F20.16)') (pos(i,j),j=1,3)
enddo

!write the postition of Ba
do j=1,3
   write(2,'(3F20.16,A12)') pos(1,1),pos(1,2),pos(1,3)*(2*j-1)/2,'   T   T   T'
enddo

!write the postition of Ti
do j=1,3
   write(2,'(3F20.16,A12)') pos(2,1),pos(2,2),pos(1,3)*j,'   T   T   T'
enddo

!write the postition of O
do j=1,3
   write(2,'(3F20.16,A12)') pos(3,1),pos(3,2),pos(1,3)*(2*j-1)/2,'   T   T   T'
   write(2,'(3F20.16,A12)') pos(4,1),pos(4,2),pos(4,3)*j,'   T   T   T'
   write(2,'(3F20.16,A12)') pos(5,1),pos(5,2),pos(4,3)*j,'   T   T   T'
enddo
          
close(unit=1)
close(unit=2)




end
