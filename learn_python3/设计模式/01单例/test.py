num = int('0x1F5A4', base=16)
u_str = r'\u' + str(num)
print(num)
print(chr(num), chr(num).isprintable())