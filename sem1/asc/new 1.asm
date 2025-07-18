bits 32 ;asamblare si compilare pentru arhitectura de 32 biti

global  start 

; declararea functiilor externe folosite de program
extern exit,scanf,printf     
import exit msvcrt.dll 
import scanf msvcrt.dll   
import printf msvcrt.dll   

segment  data use32 class=data

segment  code use32 class=code
start:
    mov eax,2
    mov ebx,3
    add eax,ebx
    call [exit]
    
    
 