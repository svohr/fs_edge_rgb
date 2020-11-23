
rows = [
    ["hk0", "half_space", "esc", "f1", "f2", "f3", "f4", "f5", "f6", "gap", "f7", "f8", "f9", "f10", "f11", "f12", "prnt", "pause", "del"],
    ["hk1", "hk2", "half_space", "tlde", "1", "2", "3", "4", "5", "6", "gap", "7", "8", "9", "0", "hyph", "=", "bspc", "home"],
    ["hk3", "hk4", "half_space", "tab", "q", "w", "e", "r", "t", "gap", "y", "u", "i", "o", "p", "obrk", "cbrk", "\\", "end"],
    ["hk5", "hk6", "half_space", "caps", "a", "s", "d", "f", "g", "gap", "h", "j", "k", "l", "colon", "apos", "ent", "pup"],
    ["hk7", "hk8", "half_space", "shft", "z", "x", "c", "v", "b", "gap", "n", "m", "com", "per", "/", "rshft", "up", "pdn"],
    ["hk9", "hk10", "half_space", "lctl", "lwin", "lalt", "lspc", "half_gap", "rspc", "ralt", "rctl", "lft", "dwn", "rght"],
]

key_size = {
    "hk0": 2,
    "bspc": 2,
    "tab": 1.5,
    "\\": 1.5,
    "caps": 1.75,
    "ent": 2.25,
    "shft": 2.25,
    "rshft": 1.75,
    "lctl": 1.5,
    "lalt": 1.25,
    "lspc": 3.5,
    "rspc": 3.5,
    "ralt": 1.25,
    "rctl": 1.75,
    "half_space": 0.5,
    "gap": 1.5,
    "half_gap": 0.75,
}


def get_center_x(key, row):
    offset = sum(key_size.get(k, 1.0) for k in row[:row.index(key)]
    center = key_size.get(key, 1.0) / 2.0
    return offset + center



