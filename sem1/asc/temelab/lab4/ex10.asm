bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
b db           1101_0101b
a dw 1000_1110_0011_1000b
    ;FEDC BA98 7654 3210
segment code use32 class=code ; code segment
start:
    mov ax,[a]
    shr ax,8
    ;0000_0000_1000_1110b
    mov bl,[b]
    and ax,0000_0000_0000_1111b
    and bl,1111_0000b
    or bl,al

    
;Replace the bits 0-3 of the byte B by the bits 8-11 of the word A.
