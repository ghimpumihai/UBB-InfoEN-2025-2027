bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
a db 2
segment code use32 class=code ; code segment
start:
    mov bh,[a]
    mov edx,dword[bh]
    call exit

    
;Replace the bits 0-3 of the byte B by the bits 8-11 of the word A.
