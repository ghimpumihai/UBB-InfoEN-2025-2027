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
   mov eax,0
   mov edx,0
   mov ax,[b]
   cwde
   add eax,[c]
   cdq
   add eax,[d]
   add edx,[d+4]
   mov ebx,[d]
   mov ecx,[d+4]
   add ebx,[c]
   adc ecx,0
   sub eax,ebx
   sbb edx,ecx
   call exit
   
   
;b+c+d+a-(d+c)


