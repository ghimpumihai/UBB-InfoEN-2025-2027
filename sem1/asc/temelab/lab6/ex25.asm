bits 32
global start
extern exit
import exit msvcrt.dll

segment data use32 class=data
    s db 01011100b, 10001001b, 11100101b
    lens equ $-s
    d times lens dw 0

segment code use32 class=code
start:
    mov ecx, lens      
    mov esi, s          
    mov edi, d          

repeta:
    lodsb               
    mov bl, 8          
    xor ah, ah         

oglindire:
    shl al, 1           
    rcr ah, 1           
    dec bl              
    jnz oglindire       
    
    mov [edi], ah      
    inc edi             
loop repeta             

    call exit          
;Se da un sir de octeti. Sa se obtina sirul oglindit al reprezentarii binare a acestui sir de octesi.
