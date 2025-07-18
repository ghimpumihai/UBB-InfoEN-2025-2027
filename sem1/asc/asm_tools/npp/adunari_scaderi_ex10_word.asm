bits 32 ; Assembling for 32-bit architecture
global start
extern exit
import exit msvcrt.dll ; Import exit function from msvcrt.dll

segment data use32 class=data ; Data segment for variables
    a dw 5230   
    b dw 5000  
    c dw 6000  
    d dw 7000  

segment code use32 class=code ; Code segment
start:
    mov ax,[b] ;b
    add ax,[c] ;b+c
    add ax,[d] ;b+c+d
    add ax,[a] ;b+c+d+a
    mov dx,[d] ;d
    add dx,[c] ;d+c
    sub ax,dx  ;b+c+d+a-(d+c)
    call [exit]
    ;b+c+d+a-(d+c)