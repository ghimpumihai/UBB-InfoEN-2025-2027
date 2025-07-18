;IV. A string of doublewords is given. From each of these doublewords form a new word by taking the higher byte of the higher word and the higher byte of the lower word. All these new obtained words will be stored in a word string. Then compute the number of bits of value 1 from the new formed word string and print it on the screen in base 10. Explain the algorithm, justify and comment accordingly the source code.
;if the string of doublewards is:
;sir dd 1234A678h, 12783634h, 1A4D3C25h,
;then the string of words
;containing the higher byte of the higher word and the higher byte of the lower word for each doubleword is: 12A6h, 1256h, 1A3Ch and the number of bits 1 from all the words of this string is. 6+6+7=19. The number 19 will be printed on the

bits 32
global start        

extern scanf, printf, exit            
import scanf msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll

segment data use32 class=data
    a db 256
    b db -255
    
segment code use32 class=code
start:
   
    
    
   
   
   
