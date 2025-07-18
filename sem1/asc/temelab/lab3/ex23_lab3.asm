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
    mov ebx,0
    mov ah,0
    mov al,[a]
    add al,[a]
    ;al=a+a
    mov bx,[b]
    add bx,[b]
    ;bx=a+a
    mov ecx,[c]
    ;ecx=c
    add ecx,[c]
    ;ecx=c+c
    add bx,ax
    ;bx=a+a+b+b
    add ecx,ebx
    ;ecx=a+a+b+b+c+c
    mov eax,[d]
    mov edx,[d+4]
    ;edx:eax=d
    sub ecx,eax;???????
    ;((a + a) + (b + b) + (c + c)) - d
