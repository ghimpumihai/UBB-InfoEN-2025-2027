bits 32 ; assembling for 32-bit architecture
global start

extern exit ; declare external exit function (from msvcrt.dll)
import exit msvcrt.dll
segment data use32 class=data ; data segment for variables
S1 db '+', '4', '2', 'a', '8', '4', 'X', '5' 
len1 equ $-S1                               
S2 db 'a', '4', '5'                          
len2 equ $-S2                                
D times len1 db 0                            

segment code use32 class=code ; code segment for code
start:
    mov ebx, 0 ; set ebx to 0
    mov esi, 0 ; index for S1
    mov edi, 0 ; index for D
    mov ecx, len1 ; set loop counter for S1

    repeta1:
        jecxz sfarsit1 ; if ecx=0, end loop                          
        mov al, [S1+esi] ; load current character from S1
        mov bh,0 ; reset index for S2
        mov bl,0 ; "found" flag set to 0 initially

    repeta2:
        cmp bh,len2 ; check if we have checked all of S2
        je add_to_D ; if S2 has been checked, add to D if not found
        mov edx,ebx
        mov ah,[S2+edx] ; load current character from S2 into ah
        cmp al,ah ; compare S1 character with S2 character
        jne next_in_S2 ; if not equal, check the next character in S2
        mov bl,1 ; set "found" flag to 1 if a match is found
        jmp skip ; skip adding to D if match found

    next_in_S2:
        inc bh ; move to next character in S2
        jmp repeta2 ; repeat inner loop for S2

    add_to_D:
        cmp bl,1 ; check if the character was found in S2
        je skip ; if found, skip adding to D
        mov [D+edi],al ; store character in D if not found
        inc edi ; increment D index

    skip:
        inc esi ; move to next character in S1
        dec ecx ; decrement outer loop counter
        jnz repeta1 ; repeat outer loop for S1

    sfarsit1:
        call exit