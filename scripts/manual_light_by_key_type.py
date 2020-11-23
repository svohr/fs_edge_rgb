

alphas = [f'[{char}]' for char in 'qwertyuiopasdfghjklzxcvbnm']
nums = [f'[{char}]' for char in '1234567890']
punctuation = [
    '[TILDE]', '[HYPH]', '[=]', '[OBRK]', '[CBRK]', '[\]',
    '[COLON]', '[APOS]', '[COM]', '[PER]', '[/]',
]
space = ['[LSPC]', '[RSPC]', '[TAB]']
esc = ['[ESC]']

modifiers = [
    '[CAPS]', '[LSHFT]', '[RSHFT]', '[LCTRL]', '[RCTRL]',
    '[LALT]', '[RALT]', '[LWIN]', '[ENT]', '[BSPC]',
]

arrows = ['[UP]', '[DWN]', '[LFT]', '[RGHT]']

nav = ['[HOME]', '[END]', '[PUP]', '[PDN]', '[PRNT]', '[PAUSE]', '[DEL]']

f_group1 = ['[F1]', '[F2]', '[F3]', '[F4]']
f_group2 = ['[F5]', '[F6]', '[F7]', '[F8]']
f_group3 = ['[F9]', '[F10]', '[F11]', '[F12]']

enter = ['[ENT]']

hot_keys = [f'[HK{hk}]' for hk in range(0, 11)]

left = (
    [f'[{char}]' for char in 'qwertasdfghzxcvb']
    + [f'[{char}]' for char in '123456']
    + f_group1
    + f_group2[:2]
    + ['[TILDE]', '[LSPC]', '[TAB]', '[ESC]',
       '[CAPS]', '[LSHFT]', '[LCTRL]', '[LALT]', '[LWIN]']
    + hot_keys
)

right = (
    [f'[{char}]' for char in 'yuiophjklnm']
    + [f'[{char}]' for char in '7890']
    + f_group2[2:]
    + f_group3
    + arrows
    + nav
    + ['[HYPH]', '[=]', '[OBRK]', '[CBRK]', '[\]',
       '[COLON]', '[APOS]', '[COM]', '[PER]', '[/]',
       '[RSPC]', '[RSHFT]', '[RCTRL]', '[RALT]', '[ENT]', '[BSPC]']
)

def print_switch_scheme():
    switch_blue = '[0][195][227]'
    switch_red = '[255][10][10]'

    for key in left:
        print(f'{key}>{switch_blue}')

    for key in right:
        print(f'{key}>{switch_red}')

    for key in left:
        print(f'fn {key}>{switch_blue}')

    for key in right:
        print(f'fn {key}>{switch_red}')


def print_lcards_scheme():
    for key in alphas + nums + punctuation:
        print(f'{key}>[255][166][77]')

    for key in modifiers + space + nav:
        print(f'{key}>[99][99][255]')

    for key in esc + f_group1 + f_group2 + f_group3 + hot_keys + arrows:
        print(f'{key}>[255][99][0]')
