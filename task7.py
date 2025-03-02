raw = input('Enter number: ')
def check_int(raw):
    return isinstance(raw, int)
if check_int(raw):
    print(int(raw))
else: 
    print(str(raw))

'''
raw = input('Enter number: ')
try:
    num = int(raw)
    print(num)
except ValueError:
    print(str(raw)) 
'''