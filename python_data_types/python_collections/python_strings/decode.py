the_string = b'\x00\x15\xe7\x01\x02d\x01\x00\xa0\x03\x00\x02\x00\x00\x00\x02\x00\x00\x08\x02\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80@\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x91\x00!\x00\x00\x00\x00\x00\x00'

the_list = list(the_string)
print(f"{the_list=}")
print(the_string.decode("idna"))
