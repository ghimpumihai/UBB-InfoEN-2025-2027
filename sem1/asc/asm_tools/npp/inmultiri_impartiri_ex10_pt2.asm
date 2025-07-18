bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
    a db 2
    b db 7
    c db 3
    d db 6

segment code use32 class=code ; code segment
start:
    mov al,[a] ;a
    mov dl,[d]
    mul dl;a*d; d*ax
    mov bl,al  ;copiem al in bl
    mov al,[c] ;c
    mov cl,[b] ;b
    mul cl     ;c
    mov bh,0
    add ax,bx  ;a*d+b*c
    call [exit]    

    
    ;a*d+b*c

