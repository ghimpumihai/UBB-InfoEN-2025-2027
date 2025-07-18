bits 32  ; assembling for 32-bit architecture
global start

extern exit ; declare external exit function (from msvcrt.dll)
import exit msvcrt.dll ; import exit function from msvcrt.dll

segment data use32 class=data ; data segment for variables
S1 db '+', '4', '2', 'a', '8', '4', 'X', '5' 
len1 equ $-S1                                
S2 db 'a', '4', '5'                          
len2 equ $-S2                                
D times len1 db 0                           

segment code use32 class=code ; code segment for code
start:
    mov eax,0
    mov al,1
    mov ah,2