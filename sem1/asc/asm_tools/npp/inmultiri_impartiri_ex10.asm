bits 32 ; assembling for 32-bit architecture
global  start

extern  exit ; declare external exit function (defined in msvcrt.dll)
import  exit msvcrt.dll ; import exit from msvcrt.dll

segment data use32 class=data ; data segment for variables
    a db 5
    b db 8
    c db 7
segment code use32 class=code ; code segment
start:
    mov ax,0
    mov al,[b] ;b
    sub al,[a] ;b-a
    add al,2   ;b-a+2
    mov bl,20  
    mul bl     ;20*(b-a+2)
    mov bx,ax  ;mutam ax in bx pentru a putea folosi registrul ax
    mov ax,0   ;resetam registrul ax
    mov al,[c] ;c
    mov cl,10  
    mul cl     ;c*10
    sub bx,ax  ;20*(b-a+2)-10*c
    mov ax,bx  ;mutam bx in ax pentru a putea folosi mul si div
    mov bl,3   ;3*[20*(b-a+2)-10*c]
    mul bl     
    mov bl,5   
    div bl     ;3*[20*(b-a+2)-10*c]/5
    call [exit]       

    
    ;3*[20*(b-a+2)-10*c]/5

