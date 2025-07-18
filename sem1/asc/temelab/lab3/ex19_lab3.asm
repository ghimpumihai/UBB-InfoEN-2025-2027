bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
     a db 4
     b dw 2122
     c dd 11_22_33_44h
     d dq 11_22_33_44_55_66_77_88h

segment code use32 class=code ; code segment
start:
     mov eax,[d]
     mov edx,[d+4]
     mov ebx,[d]
     mov ecx,[d+4]
     add eax,ebx
     adc edx,ecx
     ;edx:eax=d+d
     mov ebx,0
     mov bl,[a]
     add bl,[a]
     ;ebx=a+a
     sub eax,ebx
     sbb edx,0
     ;edx:eax=(d+d)-(a+a)
     mov ebx,0
     mov bx,[b]
     add bx,[b]
     ;ebx=b+b
     sub eax,ebx
     sbb edx,0
     ;edx:eax=(d+d)-(a+a)-(b+b)
     mov ebx,[c]
     add ebx,[c]
     ;ebx=c+c
     sub eax,ebx
     sbb edx,0
     ;edx:eax=(d+d)-(a+a)-(b+b)-(c+c)
     
     
     ;(d+d)-(a+a)-(b+b)-(c+c)
