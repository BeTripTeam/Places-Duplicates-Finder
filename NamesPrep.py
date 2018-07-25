def prep_name(name):
    s = name.lower()
    for c in '«»"': s = s.replace(c, "")
    for c in "'": s = s.replace(c, "")
    s = s.replace(' им.', ' ')
    s = s.replace(' им ', ' ')
    s = s.replace(' на ', ' ')
    s = s.replace(' в ', ' ')
    s = s.replace(' the ', ' ')
    return s.split()


def mk_names(s):
    if not s: return s
    s = s.lower()
    for c in '«»"': s = s.replace(c, "")
    for c in "'": s = s.replace(c, "")
    for c in ')': s = s.replace(c, "##")
    for c in '(': s = s.replace(c, "##")
    for c in '/': s = s.replace(c, "##")
    for c in "\\": s = s.replace(c, "##")
    s = set(s.split('##'))
    if '' in s:
        s.remove('')
    if ' ' in s:
        s.remove(' ')
    s = list(s)
    for i, si in enumerate(s):
        if si[0] == ' ':
            s[i] = si[1:]
        if si[-1] == ' ':
            s[i] = si[:-1]
    return s