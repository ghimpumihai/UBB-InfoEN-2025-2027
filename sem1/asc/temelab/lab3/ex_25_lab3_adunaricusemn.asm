bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
     a db 3
     b dw 1122
     c dd 11_22_33_44h
     d dq 11_22_33_44_55_66_77_88h
segment code use32 class=code ; code segment
start:
    mov al,[a]
    cbw
    add ax,[b]
    cwde
    sub eax,[c]
    mov eax,ebx
    mov eax,0
    mov al,[a]
    cbw
    add ax,[b]
    cwd
    cdq
    add eax,ebx
    adc edx,0
    mov ebx,eax
    mov ecx,edx
    mov al,[a]
    cbw
    add ax,[b]
    cwd
    cdq
    sub ebx,eax
    sbb ecx,edx
    call exit
   
   
;(a + b - c) + (a + b + d) - (a + b)


