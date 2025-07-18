bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
   
segment code use32 class=code ; code segment
start:
    mov ah, (2&7)^(23^(~31))": 
    call exit