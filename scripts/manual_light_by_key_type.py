

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


for key in alphas:
    print(f'{key}>[255][255][153]')

for key in nums + punctuation + space:
    print(f'{key}>[255][153][51]')

for key in modifiers:
    print(f'{key}>[221][102][68]')

for key in arrows:
    print(f'{key}>[85][153][255]')

for key in nav + f_group2 + esc:
    print(f'{key}>[51][102][255]')

for key in f_group1 + f_group3:
    print(f'{key}>[0][17][238]')

for key in hot_keys:
    print(f'{key}>[187][68][17]')
