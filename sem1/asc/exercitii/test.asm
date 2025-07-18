bits 32

global start

extern exit, fopen, fprintf, fclose, printf, scanf
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll   


segment data use32 class=data
    file_descriptor dd -1
    file_name db "test.txt", 0
    access_mode db "w", 0
    input times 100 db 0
    format_string db "%s", 0
segment code use32 class=code
start:
    push dword access_mode
    push dword file_name
    call [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    
    mov [file_descriptor], eax
    
    push dword input
    push dword format_string
    call [scanf]
    add esp, 4 * 2
                    
    push dword input
    push dword [file_descriptor]
    call [fprintf]
    add esp, 4 * 2
     stosw   
    push dword [file_descriptor]
    call [fclose]
    add esp, 4
    
final:
    push    dword 0    
    call    [exit]     
    