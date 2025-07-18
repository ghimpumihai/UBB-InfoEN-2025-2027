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
    mov ax,[a]
    imul word[a]
    ;a*a:dx:ax
    mov [r],ax
    mov [r+2],dx
    mov al,[b]
    cbw
    cwde
    mov ebx,[r]
    add eax,ebx
    ;(a*a+b)
    cdq
    mov ebx,[x]
    mov ecx,[x+4]
    add ebx,eax
    adc ecx,0
    ;(a*a+b+x) salvat in ecx:ebx
    mov al,[b]
    add al,[b]
    cbw
    cwde
    mov [r],eax
    mov eax,ebx
    mov edx,ecx
    div dword[r]
    ;(a*a+b+x)/(b+b) salvat in eax-catul edx-restul
    mov ebx,eax
    mov eax,[c]
    imul dword[c]
    ;c*c edx:eax
    add eax,ebx
    adc edx,0
    call [exit]
   ;(a*a+b+x)/(b+b)+c*c