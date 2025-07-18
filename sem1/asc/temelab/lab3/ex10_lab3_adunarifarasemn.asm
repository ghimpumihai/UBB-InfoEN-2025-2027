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
   mov eax,[d]
   mov edx,[d+4]
   add eax,[d]
   adc edx,[d+4]
   add eax,[a]
   ;(a+d+d)
   adc edx,0
   sub eax,[c]
   sbb edx,0
   ;(a+d+d)-c
   mov ebx,0
   mov bx,[b]
   add bx,[b]
   add eax,ebx
   adc edx,0
   call exit
   
   
;(a+d+d)-c+(b+b)


