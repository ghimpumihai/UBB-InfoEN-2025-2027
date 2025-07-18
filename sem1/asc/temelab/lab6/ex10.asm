bits 32 
global start
extern exit
import exit msvcrt.dll

segment data use32 class=data
    A dw 0x1234, 0x5678, 0x9ABC, 0xDEF0
    lenA equ ($ - A) / 2
    B1 times lenA db 0
    B2 times lenA db 0

segment code use32 class=code
start:
    mov si, A
    mov ecx, lenA
    mov edi, B1

repeta_superior:
    lodsw
    mov al, ah
    stosb
    loop repeta_superior

    mov si, A
    mov ecx, lenA
    mov edi, B2

repeta_inferior:
    lodsw
    stosb
    loop repeta_inferior

    call exit
;Se da un sir A de cuvinte. Construiti doua siruri de octeti  
; - B1: contine ca elemente partea superioara a cuvintelor din A
; - B2: contine ca elemente partea inferioara a cuvintelor din A