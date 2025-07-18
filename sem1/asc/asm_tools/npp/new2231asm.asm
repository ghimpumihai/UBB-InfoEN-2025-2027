bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
    a db 5
    b db 4
    c db 2

segment code use32 class=code ; code segment
start:
     mov ah,0
     mov al,[a]
     mul byte[b]
     div byte[c]
     call exit
    ;(a*b)/c

