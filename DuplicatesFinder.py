from Place import Place, Point
from StringDistance import StringDistance
from Levenstain import lev_dl
from LandDistance import dis_eval
from NamesPrep import prep_name, mk_names


class DuplicatesFinder:
    def __init__(self):
        self.sd = StringDistance()
    
    def are_same(self, p1: Place, p2: Place, debug=False):
        if debug:
            print(f'Comparing {p1} and {p2}...')
            print()
        
        de = dis_eval(p1, p2)
        
        if de > 4:
            if debug:
                print(de)
            return False
        
        p1_names = mk_names(p1.name)
        p2_names = mk_names(p2.name)
        if debug:
            print('After mk names:')
            print(p1_names)
            print(p2_names)
            print()
        
        for n1 in p1_names:
            nn1 = prep_name(n1)
            
            for n2 in p2_names:
                
                if debug:
                    print(f"Title 1: {n1}")
                    print(f"Title 2: {n2}")
                
                nn2 = prep_name(n2)
                
                is_sim = self.are_same_names(nn1, nn2, debug)
                
                if debug:
                    print(f"Similarity: {is_sim}")
                    print()
                
                if is_sim:
                    return True
        return False
    
    def are_same_names(self, a, b, debug=False):
        ops = self.sd.opcodes(a, b)
        if debug:
            print('Opcodes:')
            print(ops)
        
        w = 0
        
        # Counting equals
        equals = ops.get('equal', [])
        rep_eqs = []
        not_eq1 = []
        not_eq2 = []
        
        if equals:
            equals = equals[0]
        
        r = ops.get('replace', [])
        if r:
            rep_eqs, not_eq1, not_eq2 = self.are_equal(*r, debug)
        
        if not equals and not rep_eqs:
            if debug:
                print('No equals found')
            return False
        
        d = ops.get('delete', [])
        i = ops.get('insert', [])
        if d:
            not_eq1.extend(d[0])
            not_eq2.extend(d[1])
        if i:
            not_eq1.extend(i[0])
            not_eq2.extend(i[1])
        
        c = self.sd.replacement_cost(not_eq1, not_eq2, debug)
        
        fe = self.count_fraction_of_equals4(equals, rep_eqs, a, b, debug)
        
        if debug:
            print(f'Max number of words: {max(len(a),len(b))}')
            print(f"Equals: {len(equals)}")
            print(f"Fraction of equals: {fe}")
        
        if rep_eqs:
            lre = len(rep_eqs[0])
        else:
            lre = 0
        if fe > 0.8 or c < 0.19 or len(equals) + lre > 4:
            if True:
                print(a)
                print(b)
                print(f"Fraction of equals: {fe}")
                print(f"Replacement cost: {c}")
                print()
            return True
        return False
    
    def count_fraction_of_equals4(self, equals, rep_eq, a, b, debug=False):
        if rep_eq:
            l1 = len(rep_eq[0])
        else:
            l1 = 0
        eq_count = len(equals) + l1
        ne_count = max(len(a), len(b))
        if debug:
            print('===')
            print(f'Equal count {eq_count}')
            print(f'Not Equal count {ne_count}')
        if ne_count == 0:
            return 1
        return eq_count / ne_count
    
    def are_equal(self, s1, s2, debug=False):
        if debug:
            print("Looking for equals...")
            print(f"s1 = {s1}")
            print(f"s2 = {s2}")
        
        equal = []
        for w1 in s1:
            for w2 in s2:
                if lev_dl([w1], [w2]) == 0:
                    equal.append((w1, w2))
                    if debug:
                        print(f'Found equal: {w1} and {w2} ')
        for e in equal:
            s1.remove(e[0])
            s2.remove(e[1])
        
        if debug:
            print("After finding equals:")
            print(f"s1 = {s1}")
            print(f"s2 = {s2}")
        return equal, s1, s2


# df = DuplicatesFinder()
# p1 = Place(Point(55.7714676, 49.0887294), 'plaja stuff')
# p2 = Place(Point(55.7714676, 49.0887294), 'plaja stuf')
# print(df.are_same(p1, p2, debug=True))
