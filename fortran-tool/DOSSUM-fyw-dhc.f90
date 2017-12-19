!Date: 2013/11/13
!Author: Yue-Wen Fang; Hang-Chen Ding
!Purpose: This program is used to calculate the summation of the specified atoms in a huge structure. Take LAO/STO interface as an example,
!if you want to acquire the layer projected DOS, you can use this program instead of using Excel.

      program main
      implicit none 
  character(len=50):: string
  real*8 ::  D1(2000,2), D2(2000,2), TDOS(2000,2)
  integer*8:: i,j
  
  open(10,file='tot-DOS1')   !open tot-DOS1
  open(11,file='tot-DOS3')  !open tot-DOS2
  open(20,file='SUM-DOS') !open SUM-DOS
  
   read(10,"(A50)") string   ! read the title of tot-DOS.
   read(11,"(A50)") string

       do j=1,999
     read(10,*) (D1(j,i),i=1,2)   
     read(11,*) (D2(j,i),i=1,2) 
        end do

        do i=1,999
        TDOS(i,1)= D1(i,1)
        TDOS(i,2)= D1(i,2)+D2(i,2)   !summation of  tot-DOS1 and tot-DOS2
        end do

        do j=1,999
      write(20,*) (TDOS(j,i),i=1,2)  !wirte the TDOS into the file named SUM-DOS
        end do


end 
