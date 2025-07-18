bits 32 

global start        

extern exit, printf, scanf            
import exit msvcrt.dll   
import printf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data
segment code use32 class=code
    start:
       mov ax,600
       cwde
       mov cx,-2
       idiv cx
       call exit