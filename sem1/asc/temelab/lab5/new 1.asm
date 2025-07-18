bits 32 ; assembling for 32-bit architecture
global start

extern exit ; declare external exit function (from msvcrt.dll)
import exit msvcrt.dll
segment data use32 class=data ; data segment for variables
a dw 0x109,0x23AB,0x1234                     
lena equ ($-a)/2
b resb lena
c resb lena
segment code use32 class=code ; code segment for code
start:
    mov ecx,lena
    cld
    jecxz final
    mov esi,a
    mov edi,b
    repeat:
        lodsw ;salveaza in ax
        stosb ;il pune la adresa edi si edi+=2
    loop repeat    
    
    final:
    call exit