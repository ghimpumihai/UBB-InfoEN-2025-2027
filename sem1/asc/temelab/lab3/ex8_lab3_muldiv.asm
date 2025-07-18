bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
     a dw 1111
     b dw 2222
     c db 5
     d db 10
     e dd 11_22_33_44h
     x dq 11_22_33_44_55_66_77_88h

segment code use32 class=code ; code segment
start:
   mov ax,[a]
   mov bh,0
   mov bl,1
   div bx
   ;1/a= cat:ax rest:dx
   mov dx,0;nu ne intereseaza restul folosim doar catul de aceea resetam dx
   ;ax nu va trebui resetat deoarece impartirea 1/a va da catul 0
   
   mov ax,[b]
   mov bl,200
   mul bl
   ;200*b: dx:ax=b+2,b
   mov bx,0
   
   
   
   ;1/a+200*b-c/(d+1)+x/a-e


