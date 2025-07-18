bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
    a db 2
    b db 7
    e dw 300
    f dw 400 
    g dw 500

segment code use32 class=code ; code segment
start:
     mov ax,[e] ;e
     add ax,[f] ;e+f
     add ax,[g] ;e+f+g
     mov bx,[a] ;a
     add bx,[b] ;a+b
     div bx     ;(e+f+g)/(a+b)

    call [exit]
    ;(e+f+g)/(a+b)

