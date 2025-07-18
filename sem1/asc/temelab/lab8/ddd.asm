bits 32

global start

; declare external functions needed by our program
extern exit, fopen, fprintf, fclose, printf, scanf,fscanf
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll    
import printf msvcrt.dll    ; tell the assembler that function printf is found in msvcrt.dll library
import scanf msvcrt.dll     ; similar for scanf
import fscanf msvcrt.dll

segment data use32 class=data
    file_name resb 100
    caracter resb 1
    access_mode db 'r', 0
    file_descriptor dd -1
    stringformat db "%s", 0
    caracterformat db "%c",0
    text resb 100
    
segment code use32 class=code
start:
    push dword caracter
    push dword caracterformat
    call [scanf]
    add esp, 4 * 2

    push dword file_name
    push dword stringformat
    call [scanf]
    add esp, 4 * 2
   
    push dword access_mode
    push dword file_name
    call [fopen]
    add esp, 4 * 2
   
    cmp eax, 0
    je final
   
    mov [file_descriptor], eax
    
    read:
        push dword text         
        push dword stringformat  
        push dword [file_descriptor]  
        call [fscanf]            
        add esp, 4 * 3            
        cmp eax, 0               
        jle close
        
        push dword text
        push dword stringformat
        call [printf]
   
        jmp read
    
    close:
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
    final:
    call [exit]