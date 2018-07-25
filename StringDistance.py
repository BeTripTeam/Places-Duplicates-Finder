from difflib import SequenceMatcher


class StringDistance:
    def __init__(self):
        self.sm = SequenceMatcher(lambda x: x == " ", '', '')
    
    def replacement_cost(self, s1, s2, debug=False):
        if debug:
            print("Replacement cost counting...")
            print(f"s1 = {s1}")
            print(f"s2 = {s2}")
        
        sm = SequenceMatcher(lambda x: x == " ", ' '.join(s1), ' '.join(s2))
        # sm = SequenceMatcher(lambda x: x == " ", s1,s2)
        # self.sm.set_seqs(s1,s2)
        rep_c = sm.ratio()
        
        if debug:
            print(f"Replacement cost: {1 - rep_c}")
        
        return 1 - rep_c

    def opcodes(self, s1, s2):
        self.sm.set_seqs(s1, s2)
        op = {}
        for tag, i1, i2, j1, j2 in self.sm.get_opcodes():
            opt = op.get(tag, ([], []))
            opt[0].extend(self.sm.a[i1:i2])
            opt[1].extend(self.sm.b[j1:j2])
            op[tag] = opt
        return op
    
    
s = StringDistance()
print(s.replacement_cost('stuf', 'stuff'))