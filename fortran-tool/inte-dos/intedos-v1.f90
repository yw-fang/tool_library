program intedos
!	Purpose: integrate dos to get orbital occupation
!	Record of revisions:
!	date			programmer		Description of change
!	######################################################################
!	2014/10			Y. -W. Fang		Original code
!	2014/10/25		X. -W. Shen		write the orbital occupations
!	2014/10/31		Y. -W. Fang		correction----add an "=" after total_p.
!	2015/01/15		Y. -W. Fang		write t2g and eg, as well as out of palne and in plane occupations for LORBIT=11
!	2016/01/09              Y. -W. Fang             add the part of DOS obtained in "non-spin-polarized" calculations
        implicit none
        character(len=20) :: filename
        real,allocatable,dimension(:,:) :: a
        integer :: fermi_range
        integer :: sum=0
        integer :: iostatus
        real :: value,delta=0.0,s_u=0.0,s_d=0.0,py_u=0.0,py_d=0.0,pz_u=0.0,pz_d=0.0,px_u=0.0,px_d=0.0,dxy_u=0.0,dxy_d=0.0,dyz_u=0.0,dyz_d=0.0
        real :: dz2r2_u=0.0,dz2r2_d=0.0,dxz_u=0.0,dxz_d=0.0,dx2y2_u=0.0,dx2y2_d=0.0,total_s=0.0,total_p=0.0,total_d=0.0,total=0.0
        real :: p_u=0.0,p_d=0.0,d_u=0.0,d_d=0.0,f_u=0.0,f_d=0.0 ! for lorbit 10
        real :: total_f=0.0 ! for lorbit 10
	real :: t2g=0.0,eg=0.0,in_plane=0.0,out_plane=0.0  !for lorbit=11  date:2015/01/15
        integer :: n=0,i,j,LORBIT=0
        integer :: ISPIN=0

	write(*,*) '#######################################################################################'
	write(*,"(A60)") 'Programming language: FORTRAN & Date: late Oct. 2014'
	write(*,*) 'Author: X.-W. Shen and Y.-W. Fang'
	write(*,"(A60)") 'Affiliation: CCMP headed by Prof. C.-G. Duan at ECNU, China'
	write(*,*) 'Contact: fyuewen@gmail.com'
	write(*,*) '#######################################################################################'
	


        write(*,*) 'Please enter file name:'
        read(*,*) filename
        open(10,file=filename,status='old',iostat=iostatus)
                do
                read (10,*,iostat=iostatus) value
                if (iostatus/=0) exit
                sum=sum+1
!write(*,*) value  //this line is used to test value
                end do
        close(10)
!stop

        write(*,*) 'Input the value of LORBIT:'
        read(*,*) LORBIT
!read spin
        write(*,*) "What's ISPIN?(1 or 2):"
        read(*,*) ISPIN       
outer: IF (ISPIN==2) THEN
!LORBIT CYCLE
        select  case(LORBIT)        
		case(11)
	write(*,*) "Notice: for LORBIT = 11, f-orbitals are not considerderd in our program!"
        open(11,file=filename,status='old')
        allocate (a(sum,19))
        read(11,*) ((a(i,j),j=1,19),i=1,sum)
                do i=1,sum
                if (a(i,1)>0) exit
                n=n+1
                end do
        close(11)

!this part determins the line number of fermi level
        if ((0.0-a(n,1))<(a(n+1,1)-0.0)) then
                fermi_range=n
        else
                fermi_range=n+1
        end if
!this part determins interval of the energy
        delta=a(3,1)-a(2,1)
        deallocate (a)
!write(*,*) delta  //here is test whether the interval is correct
!stop

        open(12,file=filename,status='old')
        allocate (a(fermi_range,19))
        read(12,*)  ((a(i,j),j=1,19),i=1,fermi_range)
        close(12)

        open(13,file='LORBIT11.txt')
!       sum_s=sum_s+delta*((a(i,j),j=2),i=1,fermi_range)
!       sum_p=sum_p+delta*((a(i,j),j=4),i=1,fermi_range)
!       sum_d=sum_d+delta*((a(i,j),j=6),i=1,fermi_range)
!       sum_f=sum_f+delta*((a(i,j),j=8),i=1,fermi_range)
        do i=1,fermi_range
                s_u=s_u+delta*a(i,2)
                s_d=s_d-delta*a(i,3)
                py_u=py_u+delta*a(i,4)
                py_d=py_d-delta*a(i,5)
                pz_u=pz_u+delta*a(i,6)
                pz_d=pz_d-delta*a(i,7)
                px_u=px_u+delta*a(i,8)
                px_d=px_d-delta*a(i,9)
                dxy_u=dxy_u+delta*a(i,10)
                dxy_d=dxy_d-delta*a(i,11)
                dyz_u=dyz_u+delta*a(i,12)
                dyz_d=dyz_d-delta*a(i,13)
                dz2r2_u=dz2r2_u+delta*a(i,14)
                dz2r2_d=dz2r2_d-delta*a(i,15)
                dxz_u=dxz_u+delta*a(i,16)
                dxz_d=dxz_d-delta*a(i,17)
                dx2y2_u=dx2y2_u+delta*a(i,18)
                dx2y2_d=dx2y2_d-delta*a(i,19)
        end do
        total_s=s_u+s_d
        total_p=py_u+py_d+pz_u+pz_d+px_u+px_d
        total_d=dxy_u+dxy_d+dyz_u+dyz_d+dz2r2_u+dz2r2_d+dxz_u+dxz_d+dx2y2_u+dx2y2_d
        total=total_s+total_p+total_d
	t2g=dxy_u+dxy_d+dyz_u+dyz_d+dxz_u+dxz_d   !date:2015/01/15
	eg=dz2r2_u+dz2r2_d+dx2y2_u+dx2y2_d   !date:2015/01/15
	in_plane=dxy_u+dxy_d+dx2y2_u+dx2y2_d   !date:2015/01/15
	out_plane=dyz_u+dyz_d+dz2r2_u+dz2r2_d+dxz_u+dxz_d   !date:2015/01/15
        write(13,22) 's_u=',s_u, 's_d=',s_d, 'total_s=',total_s, 'py_u=',py_u, 'py_d=',py_d, 'pz_u=',pz_u, 'pz_d=',pz_d
        write(13,22) 'px_u=',px_u, 'px_d=',px_d, 'total_p=',total_p
        write(13,22) 'dxy_u=',dxy_u, 'dxy_d=',dxy_d, 'dyz_u=',dyz_u, 'dyz_d=',dyz_d, 'dz2-r2_u=',dz2r2_u, 'dz2-r2_d=',dz2r2_d
        write(13,22) 'dxz_u=',dxz_u, 'dxz_d=',dxz_d, 'dx2-y2_u=',dx2y2_u, 'dx2-y2_d=',dx2y2_d, 'total_d=',total_d, 'total=',total
	write(13,22) '######################'   !date:2015/01/15
	write(13,22) 't2g=',t2g,'eg=',eg,'in_plane=',in_plane,'out_plane=',out_plane   !date:2015/01/15
	write(13,22) '######################'   !date:2015/01/15
        22 format(1x,A,F11.8)
        close(13)
        
        case(10)
                open(11,file=filename,status='old')
        allocate (a(sum,9))
        read(11,*) ((a(i,j),j=1,9),i=1,sum)
                do i=1,sum
                if (a(i,1)>0) exit
                n=n+1
                end do
        close(11)

        if ((0.0-a(n,1))<(a(n+1,1)-0.0)) then
                fermi_range=n
        else
                fermi_range=n+1
        end if
        delta=a(3,1)-a(2,1)
        deallocate (a)
!write(*,*) delta
!stop
        open(12,file=filename,status='old')
        allocate (a(fermi_range,9))
        read(12,*)  ((a(i,j),j=1,9),i=1,fermi_range)
        close(12)

        open(13,file='LORBIT10.txt')
!       sum_s=sum_s+delta*((a(i,j),j=2),i=1,fermi_range)
!       sum_p=sum_p+delta*((a(i,j),j=4),i=1,fermi_range)
!       sum_d=sum_d+delta*((a(i,j),j=6),i=1,fermi_range)
!       sum_f=sum_f+delta*((a(i,j),j=8),i=1,fermi_range)
        do i=1,fermi_range
                s_u=s_u+delta*a(i,2)
                s_d=s_d-delta*a(i,3)
                p_u=p_u+delta*a(i,4)
                p_d=p_d-delta*a(i,5)
                d_u=d_u+delta*a(i,6)
                d_d=d_d-delta*a(i,7)
                f_u=f_u+delta*a(i,8)
                f_d=f_d-delta*a(i,9)
        end do
                total_s=s_u+s_d
                total_p=p_u+p_d
                total_d=d_u+d_d
                total_f=f_u+f_d
                total=total_s+total_p+total_d+total_f
        write(13,22) 's_u=',s_u, 's_d=',s_d, 'total_s=',total_s, 'p_u=',p_u, 'p_d=',p_d, 'total_p=',total_p
        write(13,22) 'd_u=',d_u, 'd_d=',d_d, 'total_d=',total_d, 'f_u=',f_u, 'f_d=',f_d, 'total_f=',total_f, 'total=',total
!        22 format(1x,A,F11.8)
        close(13)
		end select

ELSE
! SPIN =1 part
!LORBIT CYCLE
        select  case(LORBIT)        
		case(11)
	write(*,*) "Notice: for LORBIT = 11, f-orbitals are not considerderd in our program!"
        open(11,file=filename,status='old')
        allocate (a(sum,10))
        read(11,*) ((a(i,j),j=1,10),i=1,sum)
                do i=1,sum
                if (a(i,1)>0) exit
                n=n+1
                end do
        close(11)
        write(*,*) 'n=', n !testfang

!this part determins the line number of fermi level
        if ((0.0-a(n,1))<(a(n+1,1)-0.0)) then
                fermi_range=n
        else
                fermi_range=n+1
        end if
!this part determins interval of the energy
        delta=a(3,1)-a(2,1)
        deallocate (a)
!write(*,*) delta  //here is test whether the interval is correct
!stop

        open(12,file=filename,status='old')
        allocate (a(fermi_range,10))
        read(12,*)  ((a(i,j),j=1,10),i=1,fermi_range)
        close(12)

        open(13,file='LORBIT11.nospin.txt')
!       sum_s=sum_s+delta*((a(i,j),j=2),i=1,fermi_range)
!       sum_p=sum_p+delta*((a(i,j),j=4),i=1,fermi_range)
!       sum_d=sum_d+delta*((a(i,j),j=6),i=1,fermi_range)
!       sum_f=sum_f+delta*((a(i,j),j=8),i=1,fermi_range)
        do i=1,fermi_range
                s_u=s_u+delta*a(i,2)
                py_u=py_u+delta*a(i,3)
                pz_u=pz_u+delta*a(i,4)
                px_u=px_u+delta*a(i,5)
                dxy_u=dxy_u+delta*a(i,6)
                dyz_u=dyz_u+delta*a(i,7)
                dz2r2_u=dz2r2_u+delta*a(i,8)
                dxz_u=dxz_u+delta*a(i,9)
                dx2y2_u=dx2y2_u+delta*a(i,10)
        end do
        total_s=s_u
        total_p=py_u+pz_u+px_u
        total_d=dxy_u+dyz_u+dz2r2_u+dxz_u+dx2y2_u
        total=total_s+total_p+total_d
	t2g=dxy_u+dyz_u+dxz_u   !date:2016/01/10
	eg=dz2r2_u+dx2y2_u   !date:2016/01/10
	in_plane=dxy_u+dx2y2_u   !date:2016/01/10
	out_plane=dyz_u+dz2r2_u+dxz_u  !date:2016/01/10
        write(13,22) 's_u=',s_u, 'total_s=',total_s, 'py_u=',py_u, 'pz_u=',pz_u
        write(13,22) 'px_u=',px_u, 'total_p=',total_p
        write(13,22) 'dxy_u=',dxy_u, 'dyz_u=',dyz_u, 'dz2-r2_u=',dz2r2_u
        write(13,22) 'dxz_u=',dxz_u, 'dx2-y2_u=',dx2y2_u, 'total_d=',total_d, 'total=',total
	write(13,22) '######################'   !date:2016/01/10
	write(13,22) 't2g=',t2g,'eg=',eg,'in_plane=',in_plane,'out_plane=',out_plane   !date:2015/01/15
	write(13,22) '######################'   !date:2016/01/10
!        22 format(1x,A,F11.8)
        close(13)
        
        case(10)
                open(11,file=filename,status='old')
        allocate (a(sum,5))
        read(11,*) ((a(i,j),j=1,5),i=1,sum)
                do i=1,sum
                if (a(i,1)>0) exit
                n=n+1
                end do
        close(11)

        if ((0.0-a(n,1))<(a(n+1,1)-0.0)) then
                fermi_range=n
        else
                fermi_range=n+1
        end if
        delta=a(3,1)-a(2,1)
        deallocate (a)
!write(*,*) delta
!stop
        open(12,file=filename,status='old')
        allocate (a(fermi_range,5))
        read(12,*)  ((a(i,j),j=1,5),i=1,fermi_range)
        close(12)

        open(13,file='LORBIT10.nospin.txt')
!       sum_s=sum_s+delta*((a(i,j),j=2),i=1,fermi_range)
!       sum_p=sum_p+delta*((a(i,j),j=4),i=1,fermi_range)
!       sum_d=sum_d+delta*((a(i,j),j=6),i=1,fermi_range)
!       sum_f=sum_f+delta*((a(i,j),j=8),i=1,fermi_range)
        do i=1,fermi_range
                s_u=s_u+delta*a(i,2)
                p_u=p_u+delta*a(i,3)
                d_u=d_u+delta*a(i,4)
                f_u=f_u+delta*a(i,5)
        end do
                total_s=s_u
                total_p=p_u
                total_d=d_u
                total_f=f_u
                total=total_s+total_p+total_d+total_f
        write(13,22) 's_u=',s_u, 'total_s=',total_s, 'p_u=',p_u, 'total_p=',total_p
        write(13,22) 'd_u=',d_u, 'total_d=',total_d, 'f_u=',f_u, 'total_f=',total_f, 'total=',total
!        22 format(1x,A,F11.8)
        close(13)
		end select


END IF  outer



end program intedos
