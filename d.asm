[org 0x100]

mov cx,[n]
mov bx,old_arr

outerloop:
        mov ax,[bx]
        mov [s_index],bx
        mov [loop_cx],cx
        mov cx,[n]

        mov dx,new_arr

        mov [d_index],dx
        mov bx,old_arr

        innerloop:
                mov dx,[bx]
                cmp ax,dx
                jnc inc_di
                back:
                add bx,2
                loop innerloop

        mov bx,[d_index]
        sub bx,2
        mov [bx],ax

        mov bx,[s_index]
        add bx,2
        mov cx,[loop_cx]
        loop outerloop

mov ax,0x4c00
int 0x21

inc_di:
        add word [d_index],2
        jmp back

old_arr: dw 7,4,0,1,3,5,2,6
new_arr: dw 0,0,0,0,0,0,0,0
s_index: dw 0
d_index: dw 0
loop_cx: dw 0
n: dw 8
