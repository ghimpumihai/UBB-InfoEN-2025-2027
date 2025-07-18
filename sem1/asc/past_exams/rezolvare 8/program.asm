bits 32 ;asamblare si compilare pentru arhitectura de 32 biti

global  start 

; declararea functiilor externe folosite de program
extern exit     
import exit msvcrt.dll    

segment  data use32 class=data
    
   
segment  code use32 class=code ; segmentul de cod
    start:
        mov eax,-1
        mov ebx,-2
        imul ebx
       
            
        final:
            push dword 0
            call [exit]