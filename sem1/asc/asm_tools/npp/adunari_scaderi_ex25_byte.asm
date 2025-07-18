bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
    a db 115
    b db 120
    c db 121
    d db 139

segment code use32 class=code ; code segment
start:
    mov AX,0
    mov AL, [c]     ;c
    add AX, [d]     ;c+d
    add AX, [d]     ;c+d+d
    mov DX, 0
    add DL, [a]     ;a
    add DX, [a]     ;a+a
    add DX, [b]     ;a+a+b
    SUB AX,DX;      ;(c+d+d)-(a+a+b)
    call [exit]       

    
    ;(c+d+d)-(a+a+b)
