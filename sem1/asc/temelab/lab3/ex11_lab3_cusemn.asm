bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
     a db 10
     b dw 8422
     c dd 11_22_33_44h
     d dq 11_22_33_44_55_66_77_88h

segment code use32 class=code ; code segment
start:
    mov ebx,[d]
    mov ecx,[d+4]
    ;ecx:ebx=d
    mov al,[a]
    cbw
    add ax,[b]
    cwd
    add eax,[c]
    cdq
    ;a+b+c
    sub ecx,eax
    sbb ebx,0
    ;d-(a+b+c)
    mov eax,0
    mov al,[a]
    add al,[a]
    cbw
    cwd
    cdq
    sub ecx,eax
    sbb ebx,edx
    call exit
    ;d-(a+b+c)-(a+a)

