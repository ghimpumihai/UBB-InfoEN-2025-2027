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
   mov al,[a]
   cbw
   add ax,[b]
   cwde
   mov ebx,[c]
   sub eax,ebx
   ;(a+b-c)
   mov ecx,eax
   mov eax,0
   mov al,[a]
   cbw
   add ax,[b]
   cwd
   cdq
   mov ebx,[d]
   mov edx,[d+4]
   add ebx,eax
   adc edx,0
   ;(a+b+d)
   mov eax,0
   mov al,[a]
   add ax,[b]
   cwd
   cdq
   ;(a+b)
   add ebx,ecx
   adc edx,0
   sub ebx,eax
   sbb edx,0
   call exit
   
   
   
   ;(a + b - c) + (a + b + d) - (a + b)


