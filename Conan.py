import struct
import os

def tamper(student_id):
  name=os.path.abspath(__file__)
  lname=os.path.dirname(name)
  full_name=os.path.join(lname,"lenna.bmp")
  f=open("lenna.bmp", "r+b")
  a=[2,0,1,8,1,1,1,1,3,0,2,7]
  for l in a:
      b=53
      f.seek(b+l)
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
