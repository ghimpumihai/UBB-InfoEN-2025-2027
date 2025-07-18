bits 32 ; assembling for 32-bit architecture
global start

extern exit ; declare external exit function (defined in msvcrt.dll)
import exit msvcrt.dll ; import exit from msvcrt.dll


segment data use32 class=data ; data segment for variables
S1 db '+', '1', '2', 'b', '8', '6', 'X', '8'
len1 equ $-S1
S2 db '4','5'
len2 equ $-S2
D times len1/2+len2 db 0
segment code use32 class=code ; code segment

start:
    mov ecx,len2 ; set loop counter for S2
    mov esi,0 ; index for S2
    repeta1:
        jecxz sfarsit1 ; if ecx=0 jump to label
        mov al,[S2+ecx-1] ; take the last element from S2
        mov [D+esi],al ; move the element in D
        inc esi ; increase index
        dec ecx ; decrease loop counter
        jnz repeta1; jump back to label if ecx!=0
    sfarsit1:
    
    mov ecx,len1/2 ; set loop counter for S1
    mov esi,0 ; index for S1
    repeta2:
        jecxz sfarsit2 ; if ecx=0 jump to label
        mov al,[S1+esi+1] ; take the elements from the even positions
        mov [D+esi+len2],al ; move the element in D
        add esi,2; increase index
        dec ecx ; decrease loop counter
        jnz repeta2; jump back to label if ecx!=0
    sfarsit2:
    call exit
;Se dau doua siruri de caractere S1 si S2. Sa se construiasca sirul D prin concatenarea elementelor sirului S2 in ordine inversa cu elementele de pe pozitiile pare din sirul S1.

