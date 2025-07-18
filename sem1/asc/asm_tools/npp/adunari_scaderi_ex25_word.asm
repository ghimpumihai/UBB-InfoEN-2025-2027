bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
    a dw 1300
    b dw 1400
    c dw 1215
    d dw 1397

segment code use32 class=code ; code segment
start:
    mov ax,[a] ;a
    add ax,[b] ;a+b
    sub ax,[c] ;a+b-c
    sub ax,[d] ;a+b-c-d
    call [exit]     

    
    ;(a+b-c)-d
