bits 32 

global _maximum      

segment code use32 class=code
_maximum:
    
    mov eax, [esp+4]    ;put in eax the last value
    cmp eax, ebx    ;compare eax to the current maximum in ebx
    jb skip    ;if eax is below ebx jump to skip
    mov ebx, eax    ;if not update the maximum value
    skip:
    ret