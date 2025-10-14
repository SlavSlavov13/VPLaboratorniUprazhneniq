num = '1234'                    # decimal text
n_dec = int(num, 10)            # 1234
b = format(n_dec, 'b')          # '10011010010'
h = format(n_dec, 'X')          # '4D2'

n_from_b = int(b, 2)            # 1234
n_from_h = int(h, 16)           # 1234

print(f'Decimal: {n_dec}')      # 1234
print(f'Binary: {b}')           # 10011010010
print(f'Hexadecimal: {h}')      # 4D2

print(f"b -> dec: {n_from_b}")
print(f"h -> dec: {n_from_h}")