stack_16 = ('bucket',
            'sign',
            'window_pane',
            'ender_pearl',
            'ender_eye',
            'eye_of_ender',
            'snowball')


def stacks(total):
    print(f'stacks({total})')
    stacks = (total//64, total % 64)
    string = f'{total//64} stacks + {total%64}'
    print(string)
    return stacks


def batch_stacks(file):
    print(f'batck_stacks({file})')
    with open(file, 'r') as f:
        data = [line.strip().split(' ') for line in f]
        print(data)

    dct = {}
    for x in data:
        dct[x[1]] = x[0]
    print(dct)

    new_dct = {}

    with open(file, 'a') as f:

        f.write(f'''
        
---STACKED---
''')
        for block, total in dct.items():
            if block in stack_16:
                stacks = (int(total)//16)
                rem = (int(total) % 16)

            else:
                stacks = (int(total)//64)
                rem = (int(total) % 64)

            if stacks == 0:
                string = f"{rem} '{block}'"
            elif rem == 0:
                string = f"{stacks} stacks '{block}'"
            else:
                string = f"{stacks} stacks + {rem} '{block}'"
            print(string)
            new_dct[block] = (stacks, rem)

            f.write(f'''{string}
''')

    print(new_dct)

    return new_dct
'''
def batch_dict(file):
    with open(file, 'r') as f:
        data = [line.strip().split(' ') for line in f]
        print(data)

    dct = {}
    for x in data:
        dct[x[1]] = x[0]
    print(dct)
    return(dct)
'''
