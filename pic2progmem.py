# -*- coding: UTF-8 -*-
import sys
import re

inl = 12
pattern = r''
subs = r''
sstart = 'static const uint8_t binary[] PROGMEM = {'
send = '};'
def create_ptrn(ln):
    global pattern, subs
    pattern = r'(..)'
    subs = r'0x\g<1>'
    for i in range(1, int(ln)):
        pattern += r'(..)?'
        subs +=r', 0x\g<'+str(i+1)+'>'

bname = ''
oname = ''
usage = '''Usage:
python.exe pic2progmem.py byte_in_line binary_file_name
Where:
byte_in_line - the number of bytes in each line in the output
binary_file_name - binary file name to convert

The result is output to stdout
Example:
python.exe pic2progmem.py 12 d:\pictures\foto.png
'''

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print('Error !!!')
        print(usage)
        sys.exit(1)
    else:
        try:
            inl = int(sys.argv[1])
        except Exception as e:
            print('Error !!!')
            print(e)
            print(usage)
            sys.exit(2)

        bname = sys.argv[2]
        if len(sys.argv) > 3:
            oname = sys.argv[3]

    try:
        with open(bname,"rb") as bn:
            print(sstart)
            while True:
                data = bn.read(inl)
                if not data:
                    break
                create_ptrn(len(data))
                print(re.sub(pattern,subs,data.hex()))
            print(send)
    except Exception as e:
        print('Error !!!')
        print(e)
        print(usage)
        sys.exit(3)