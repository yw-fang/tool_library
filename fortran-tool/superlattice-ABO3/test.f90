program main
implicit none
character*8::a
a='ini'
write(*,*) a
if(a=='ini') then
write(*,*) "POSCAR was read successfully!"
end if
if(a=='ini') write(*,*) "logical IF"



end
