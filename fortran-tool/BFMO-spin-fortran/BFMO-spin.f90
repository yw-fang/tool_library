program spin
!	Purpose: Generate all the spin configurations for 2*2*2 cubic BFMO double perovskite
!	Record of revisions:
!	date			programmer		Description of change
!	######################################################################
!	2015/01/30		Y. -W. Fang		Original code

        implicit none
!        character(len=20) :: filename=allspin
        integer :: atom_1,atom_2,atom_3,atom_4,atom_5,atom_6,atom_7,atom_8
        integer :: i,j,k,l,m,n,o,p
	open(10,file='allspin.dat')


	write(*,*) '#######################################################################################'
	write(*,"(A60)") 'Programming language: FORTRAN & Date: late Jan. 2015'
	write(*,*) 'Author: Y.-W. Fang'
	write(*,"(A60)") 'Affiliation: CCMP headed by Prof. C.-G. Duan at ECNU, China'
	write(*,*) 'Contact: fyuewen@gmail.com'
	write(*,*) '#######################################################################################'

	do i=-1,1,2	
	  atom_1=i
	    do j=-1,1,2
              atom_2=j
		do k=-1,1,2
		  atom_3=k
		  do l=-1,1,2
		    atom_4=l
		    do m=-1,1,2
		       atom_5=m
		      do n=-1,1,2
		        atom_6=n
			do o=-1,1,2
			  atom_7=o
			  do p=-1,1,2
			    atom_8=p
        write(10,'(1x8I)') atom_1,atom_2,atom_3,atom_4,atom_5,atom_6,atom_7,atom_8
			  end do
			end do
		      end do
		    end do
		  end do
		end do
	    end do
	end do
	close(10)
	      
	
end program spin 
