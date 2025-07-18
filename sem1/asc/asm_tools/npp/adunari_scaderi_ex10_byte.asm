bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
    a db 9
    b db 7
    c db 10
    d db 20

segment code use32 class=code ; code segment
start:
    mov AL, [a];a   
    add AL, [d];a+d
    add AL, [d];a+d+d
    mov DL, [b];b
    add DL, [b];b+b
    sub AL, [c];a+d+d-c
    add AL,DL;a+d+d-c+b+b
    call [exit]      
    ;(a+d+d)-c+(b+b)