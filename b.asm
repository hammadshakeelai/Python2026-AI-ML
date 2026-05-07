[org 0x100]

;block 1
mov ah,0 ; A <- 0
mov al,9 ; Q <- Divisor
mov dh,3 ; M <- Dividend
mov cl,8 ; N <= Count <- n

tag: ; part of block 6

;block 2
shl ax,1 ;shift A,Q

;block 3
sub ah,dh ;A <- A-M

;block 4
cmp ah,0 ;A<0?
jnl no; choose left(no) or right(yes)

;block 5.yes
and al,0xfe ;Q. <- 0
add ah,dh ;A <- A+M

jmp ahead
;block5.no
no:
or al,1
ahead:

;block 6
loop tag

mov ax,0x4c00
int 0x21

