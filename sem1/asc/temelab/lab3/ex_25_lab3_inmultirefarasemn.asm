bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
     a dw 2
     c dd 3
     b db 1
     x dq 6
     r resd 1
segment code use32 class=code ; code segment
start:
    mov eax,0
    mov ax,[a]
    mul word[a]
    ;a*a salvat pe dx:ax
    add al,[b]
    adc dx,0
    ;a*a+b salvat pe dx:ax
    mov [r],ax
    mov [r+2],dx
    ;eliberam dx:ax pentru operatii viitoare
    mov ebx,0
    mov ebx,[r]
    ;dx:ax mutat in ebx
    mov eax,[x]
    mov edx,[x+4]
    ;x este de tip qword il punem in edx:eax
    add eax,ebx
    adc edx,0
    ;(a*a+b+x)
    mov ebx,0
    mov bl,[b]
    add bl,[b]
    div ebx
    ;(a*a+b+x)/(b+b)
    mov ebx,eax
    mov eax,0
    mov eax,[c]
    mul dword[c]
    ;(c*c)
    add eax,ebx
    adc edx,0
    call [exit]
   ;(a*a+b+x)/(b+b)+c*c