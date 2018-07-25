from nltk import edit_distance


def lev_dl(s1,s2):
    if not min(len(s1), len(s2)):
        return max(len(s1), len(s2))
    else:
        return min(lev(s1[:-1], s2) + 1,
                   lev(s1, s2[:-1]) + 1,
                   lev(s1[:-1], s2[:-1]) + damerau_levenshtein_distance(s1[-1],s2[-1]))/3


def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1
    
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + 0)  # transposition
    
    return d[lenstr1 - 1, lenstr2 - 1]


def sub_weight(s1,s2):
    if s1 != s2:
        return edit_distance(s1,s2)/3
    return 0


def lev(s1,s2):
    if not min(len(s1), len(s2)):
        return max(len(s1), len(s2))
    else:
        return min(lev(s1[:-1], s2) + 1,
                   lev(s1, s2[:-1]) + 1,
                   lev(s1[:-1], s2[:-1]) + sub_weight(s1[-1],s2[-1]))