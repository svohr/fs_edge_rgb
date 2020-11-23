

rows = [
    ["hk0", "gap_half", "esc", "f1", "f2", "f3", "f4", "f5", "f6", "gap_double", "f7", "f8", "f9", "f10", "f11", "f12", "prnt", "pause", "del"],
    ["hk1", "hk2", "gap_half", "tlde", "1", "2", "3", "4", "5", "6", "gap_double", "7", "8", "9", "0", "hyph", "=", "bspc", "home"],
    ["hk3", "hk4", "gap_half", "tab", "q", "w", "e", "r", "t", "gap_double", "y", "u", "i", "o", "p", "obrk", "cbrk", "\\", "end"],
    ["hk5", "hk6", "gap_half", "caps", "a", "s", "d", "f", "g", "gap_double", "h", "j", "k", "l", "colon", "apos", "ent", "pup"],
    ["hk7", "hk8", "gap_half", "shft", "z", "x", "c", "v", "b", "gap_double", "n", "m", "com", "per", "/", "rshft", "up", "pdn"],
    ["hk9", "hk10", "gap_half", "lctl", "lwin", "lalt", "lspc", "gap_single", "rspc", "ralt", "rctl", "lft", "dwn", "rght"],
]

board_width = sum(key_size.get(k, 1.0) for k in rows)
board_height = len(rows) + 0.5

blanks = ["gap_half", "gap_single", "gap_double"]

key_to_row = {
    k: i for i, row in enumerate(rows) for k in rows[i] if k not in blanks
}

keys_all = [k for r in rows for k in r if k not in blanks]

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
    "gap_half": 0.5,
    "gap_single": 0.75,
    "gap_double": 1.50,
}


def get_key_x_center(key):
    row = rows[key_to_row[key]]
    offset = sum(key_size.get(k, 1.0) for k in row[:row.index(key)])
    center = key_size.get(key, 1.0) / 2.0
    return offset + center


def get_key_y_center(key):
    r = key_to_row[key]
    return r + (0 if r == 0 else 0.5) + 0.5


def get_key_coords(key):
    return (get_key_x_center(key), get_key_y_center(key))


def scale_coords(c, dims):
    return ((c[0] / board_width) * dims[0], (c[1] / board_height) * dims[1])


def get_key_image_coords(k, dims):
    return scale_coords(get_key_coords(k), dims)


