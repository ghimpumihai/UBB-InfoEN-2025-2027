bits 32 


global strFind
segment code use32 class=code
strFind:
  mov ecx, [esp + 4] ; haystack
  mov edx, [esp + 8] ; needle

.looop:
  mov al, [ecx]
  cmp al, 0
  je .retFalse

  push edx
  push ecx
  call strEq
  add esp, 8

  cmp eax, 1
  je .retTrue

  inc ecx
  jmp .looop

.retTrue:
  mov eax, 1
  ret

.retFalse:
  mov eax, 0
  ret
  
