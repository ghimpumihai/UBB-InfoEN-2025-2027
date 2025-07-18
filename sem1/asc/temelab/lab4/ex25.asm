bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

;Given the doublewords M and N, compute the doubleword P as follows.

segment data use32 class=data ; data segment for variables
m dw                     1001_1111_1101_0101b
n dw                     1000_1110_0011_1000b
p dd 1001_1000_1111_1001_1001_1000_1010_1011b
    ;FEDC BA98 7543 3210 FEDC BA98 7654 3210
segment code use32 class=code ; code segment
start:
;the bits 0-6 of P are the same as the bits 10-16 of M
    mov eax,[p]
    mov ebx,0
    mov bx,[m]
    shr ebx,10
    and ebx, 0000_0000_0000_0000_0000_0000_0011_1111b
    and eax, 1111_1111_1111_1111_1111_1111_1100_0000b
    or eax,ebx
;the bits 7-20 of P are the same as the bits 7-20 of (M AND N).
    mov eax,[p]
    mov ebx,0
    mov bx,[m]
    mov cx,[n]
    and bx,cx
    and ebx,0000_0000_0000_0000_1111_1111_1000_0000b
    and eax,1111_1100_0000_0000_0000_0000_0111_1111b
    or eax,ebx
;the bits 21-31 of P are the same as the bits 1-11 of N.
    mov ebx,0
    mov eax,[p]
    mov ebx,dword[n]
    and ebx,0000_0000_0000_0000_0000_1111_1111_1110b
    shl ebx,20
    ;and eax,0000_0000_0001_1111_1111_1111_1111_1111b
    or eax,ebx
