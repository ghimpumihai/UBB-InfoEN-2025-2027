bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
    a db 5
    b db 10
    c db 20
    d dw 500

segment code use32 class=code ; code segment
start:
    mov ax,0
    mov al,[b] ;b
    add al,[c] ;b+c
    mov bl,4   
    mul bl     ;4*(b+c)
    mov cx,ax  ;folosim cx pentru a tine o copie lui ax
    
    mov ax,0
    mov al,[a] ;a
    mov dl,10  
    mul dl     ;a*10
    
    mov bx,100
    sub bx,ax  ;100-10*a
    add bx,cx  ;100-10*a+4*(b+c)
    sub bx,[d] ;[100-10*a+4*(b+c)]-d
    call exit       

    
    ;[100-10*a+4*(b+c)]-d