!Creating date: 20150525
!Author: Y.-W.FANG, fyuewen@gmail.com
!Affiliation: C.-G.Duan's Group at East China Normal Univ.
!Purpose: This code is used to generate supperlattice for ABO3 peroveskite oxides with cubic of tetragonal sphase.

!definition list
! 1. mat--> material name
! 2. latcons-->lattice constant of ABO3
! 3. latvect--> lattice vectors of ABO3
! 4. nelem--> number of types of elements
! 5. natom--> ammounts of atoms
! 6. coord--> coordinates
! 7. element--> the name of element

program main
implicit none

    
character(len=100)  :: checkread,ignore
! donnot use too large len for mat 
!or it will cause extra blank in the new POSCAR
character(len=30)   :: mat   
real*8              :: latcons,total_len_1,latvect_33
real*8              :: latvect(3,3)
real*8              :: coord(3,3)
!real*8             ::  !ratio,pos(5,3),inv(3)
integer*8           :: i,j,natom
integer*8           :: natom_element(3),natom_element_new(3)
integer*8           :: zrepeat,N
integer*8           :: nelem
character(len=3)    :: element1,element2,element3
character(len=10)   :: selective, dynamics, coord_system
character(len=2)   :: tag


!read ling 9 to check whether POSCAR was read successfully
write(*,*) "Please use POSCAR containing the name of elements"
open(unit=2,file='POSCAR-new.vasp')
open(unit=1,file='POSCAR')
    do i=1,9
read(1,'(A6)') checkread
    end do
    if(checkread=='Direct') then
write(*,*) "POSCAR was read successfully!"
    else 
write(*,*) "Read error for POSCAR!"
end if
rewind(1)

!read materials and lattice constant from POSCAR
read(1,'(A14)') mat
    write(*,*) mat
    write(2,*) mat
read(1,'(F20.16)') latcons
    write(*,'(F20.16)') latcons
    write(2,'(F20.16)') latcons

       write(*,*) "Repeat unit cell along Z: "
       read(*,*) zrepeat 
!read lattice vector from POSCAR
  do i=1,3
      read(1,*) latvect(i,:)
  end do
!copy initial latvect(3,3) to a variable
  latvect_33 = latvect(3,3)
  write(*,*) "The initial latvect(3,3) is ", latvect_33

!get new latvect after updating the zrepeat
       latvect(3,3)=latvect(3,3)*zrepeat
       total_len_1=latvect(3,3)*latcons
       write(*,*) total_len_1
!write new lattice vector to file
  do i=1,3
      write(*,100) latvect(i,:2),latvect(i,3)
      write(2,100) latvect(i,:2),latvect(i,3)
  100 FORMAT (1X,2(F20.15,2X),(F20.15))
  end do
!read the name of elements from POSCAR
read(1,*)   element1,element2,element3
write(*,*)  element1,element2,element3
write(2,*)  element1,element2,element3

!read the amounts of atoms for each element from initial POSCAR
!and write the corresponding amounts for new PSOCAR
read(1,*)    natom_element(:)
write(*,200) natom_element(:)
natom_element_new=natom_element(:)*zrepeat
write(*,200) natom_element_new(:)
write(2,200) natom_element_new(:)

200 FORMAT (2X,3(I3))

!compute total atoms
natom=0
do i=1,3
natom=natom+natom_element(i)
end do
write(*,'(I3)') natom

!read Selective and coordinates system(usually we use directional coordinates)
read(1,*) selective,dynamics
write(*,'(A20)') selective//dynamics
write(2,'(A20)') selective//dynamics
!write(*,'(A10,1X, A10)') selective,dynamics
read(1,*)  coord_system
write(*,'(A10)') coord_system
write(2,'(A10)') coord_system

!read all initial coordinates from POSCAR
do i=1,natom
  read(1,*) coord(i,:), tag,tag,tag
  write(*,300) coord(i,1:3)
end do
300 FORMAT (3(1X,F20.18))

!write the first element: such as Bi
N=zrepeat
write(*,*) "N= ", N
do i=1,N
  write(*,300) coord(1,1), coord(1,2), (1.0/zrepeat)*(i-1) 
  write(2,300) coord(1,1), coord(1,2), (1.0/zrepeat)*(i-1) 
!Here, don't use 1/zrepeat, because 1 is an integer
end do

!write the second element: such as Fe
do i=1,N
  write(*,300) coord(2,1), coord(2,2), (1.0/zrepeat)*(i-1)+0.5/zrepeat
  write(2,300) coord(2,1), coord(2,2), (1.0/zrepeat)*(i-1)+0.5/zrepeat
!Here, don't use 1/zrepeat, because 1 is an integer
end do

!write the third element_1: such as O_1 (cause there are three oxygen atoms)
do i=1,N
  write(*,300) coord(3,1), coord(3,2), (1.0/zrepeat)*(i-1)
  write(2,300) coord(3,1), coord(3,2), (1.0/zrepeat)*(i-1)
!Here, don't use 1/zrepeat, because 1 is an integer
end do

!write the third element_2: such as O_2 (cause there are three oxygen atoms)
do i=1,N
  write(*,300) coord(4,1), coord(4,2), (1.0/zrepeat)*(i-1)+0.5/zrepeat
  write(2,300) coord(4,1), coord(4,2), (1.0/zrepeat)*(i-1)+0.5/zrepeat
!Here, don't use 1/zrepeat, because 1 is an integer
end do

!write the third element_3: such as O_3 (cause there are three oxygen atoms)
do i=1,N
  write(*,300) coord(5,1), coord(5,2), (1.0/zrepeat)*(i-1)+0.5/zrepeat
  write(2,300) coord(5,1), coord(5,2), (1.0/zrepeat)*(i-1)+0.5/zrepeat
!Here, don't use 1/zrepeat, because 1 is an integer
end do
!          
close(unit=1)
close(unit=2)
!



end
