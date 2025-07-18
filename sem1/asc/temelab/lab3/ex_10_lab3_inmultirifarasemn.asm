bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
     a db 2
     c db 3
     b dw 1
     d dd 20
     x dq 6
     r resd 1
segment code use32 class=code ; code segment
start:
    mov eax,0
    mov al,[a]
    mul word[b]
    ;rezultatul ajunge pe dx:ax
    mov [r],ax
    mov [r+2],dx
    mov eax,[r]
    mov bx,7
    sub bx,ax
    add bl,[c]
    mov ax,bx
    div byte[a]
    mov ebx,[d]
    sub ebx,eax
    sub ebx,6
    mov eax,[x]
    mov edx,[x+4]
    mov ecx,2
    div ecx
    add ebx,eax
    call exit
    ;d-(7-a*b+c)/a-6+x/2