import struct
import os

def tamper(student_id):
  name=os.path.abspath(__file__)
  lname=os.path.dirname(name)
  full_name=os.path.join(lname,"lenna.bmp")
  f=open("lenna.bmp", "r+b")
  f.seek(54+2*3)
  a=bytes([0,0,0])
  f.write(a)
  for l in range(1,12):
      flag=int(student_id[l])
      if flag==0:
          flag=10
      f.seek((flag-1)*3,1)
      a=bytes([0,0,0])
      f.write(a)
  f.close()


def detect():
  with open('lenna.bmp', 'rb') as f:
    bmp_file_header = f.read(14)

    bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

    f.seek(offset)

    count = 12
    offset = 0
    last_offset = 0
    while count > 0:
      color = f.read(3)

      if color == b'\x00\x00\x00':

        if offset - last_offset == 10:
          print(0)
        else:
          print(offset - last_offset)

        last_offset = offset
        count -= 1

      offset += 1


if __name__ == '__main__':
  import sys
  tamper(sys.argv[1])

  detect()
