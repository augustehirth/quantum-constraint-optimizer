import json
import os
from collections import defaultdict
from matplotlib import pyplot as plt
from scipy.stats import chisquare, chi2

qmap_extra = dict([('bv', {0: 0, 2: 1, 4: 2}),
('BV4_optimized', {0: 0, 2: 1, 4: 2, 11: 3, 3: 4}),
('dj', {4: 0, 2: 1, 11: 2}),
('grover', {3: 0, 4: 1}),
('ope', {4: 0, 3: 1, 2: 2}),
('QAOA', {0: 0, 1: 1, 3: 2, 12: 3, 2: 4}),
('qft', {4: 0, 3: 1, 2: 2}),
('simon', {12: 0, 3: 1, 11: 2, 2: 3}),
('superdense', {3: 0, 4: 1}),
('teleport', {4: 0, 3: 1}),
('toffoli_optimized', {2: 0, 12: 1, 11: 2, 3: 3}),
('vqls', {2: 0, 3: 1, 4: 2}),
('vqls2', {4: 0, 3: 1, 2: 2, 11: 3}),
('vqls3', {1: 0, 2: 1, 3: 2, 4: 3, 10: 4, 11: 5, 12: 6})])

qmap_base = dict([('bv', {2: 0, 0: 1, 4: 2}),
('BV4_optimized', {0: 0, 2: 1, 11: 2, 4: 3, 3: 4}),
('dj', {4: 0, 2: 1, 11: 2}),
('grover', {3: 0, 4: 1}),
('ope', {4: 0, 3: 1, 2: 2}),
('QAOA', {0: 0, 1: 1, 3: 2, 12: 3, 2: 4}),
('qft', {4: 0, 3: 1, 2: 2}),
('simon', {12: 0, 3: 1, 11: 2, 2: 3}),
('superdense', {3: 0, 4: 1}),
('teleport', {4: 0, 3: 1}),
('toffoli_optimized', {2: 0, 12: 1, 11: 2, 3: 3}),
('vqls', {2: 0, 3: 1, 4: 2}),
('vqls2', {4: 0, 3: 1, 2: 2, 11: 3}),
('vqls3', {1: 0, 2: 1, 3: 2, 4: 3, 10: 4, 11: 5, 12: 6})])

nmap = dict([('bv', 'circuit10'),
    ('BV4_optimized', 'circuit12'),
    ('dj', 'circuit14'),
    ('grover', 'circuit16'),
    ('ope', 'circuit18'),
    ('QAOA', 'circuit20'),
    ('qft', 'circuit22'),
    ('simon', 'circuit24'),
    ('superdense', 'circuit26'),
    ('teleport', 'circuit28'),
    ('toffoli_optimized', 'circuit30'),
    ('vqls', 'circuit32'),
    ('vqls2', 'circuit34'),
    ('vqls3', 'circuit36')])

nmap = {v:k for k,v in nmap.items()}

def map_opt(string, dct): 
    #dct = {v:k for k,v in dct.items()}
    instring = [char for char in reversed(string)]
    #outstring = ''.join(reversed([instring[dct.get(x)] for x in dct.keys()]))
    #return outstring
    outstring = ['0']*len(string)
    for o,u in dct.items():
        outstring[u] = instring[o]
    return ''.join(reversed(outstring))

def map_unopt(string, dct): 
    instring = [char for char in reversed(string)]
    outstring = ['0']*len(string)
    for o,u in dct.items():
        outstring[u] = instring[u]
    return ''.join(reversed(outstring))


def from_hex(string): 
    return int(string, 16)

def from_bin(string): 
    return int(string, 2)

def fill_zeroes(numb, n): 
    string = format(numb, "0"+str(n)+"b")
    return string

finals = defaultdict(dict)
inter = defaultdict(dict)
for results in os.listdir("testing/runs"): 
    if results.endswith("_result.json"):
        with open("testing/runs/"+results) as f:
            data = json.load(f)
        ress = data['results']
        for res in ress: 
            #print(res.keys())
            name = res['header']['name']
            name = nmap.get(name, name)
            if 'unoptimized' in results:
                k1 = 'unoptimized'
            else:
                k1 = 'optimized'
            if 'real' in results: 
                k2 = 'real'
            else:
                k2 = 'simulated'
            if 'extra' in results: 
                k3 = 'extra'
            else: 
                k3 = 'base'
            assert inter[name].get((k1,k2,k3)) == None
            inter[name][(k1,k2,k3)] = res['data']['counts']
            for name,kinds in inter.items():
                for key,counts in kinds.items():
                    opt, sim,typ = key
                    newcounts = defaultdict(int)
                    if typ == 'base': 
                        qmap = qmap_base
                    elif typ == 'extra':
                        qmap = qmap_extra
                    else: 
                        raise Exception
                    for state in counts.keys():
                        newstate = fill_zeroes(from_hex(state), 15)
                        #print(state)
                        if opt == 'optimized':
                            newstate = map_opt(newstate, qmap[name])
                        elif opt == 'unoptimized':
                            newstate = map_unopt(newstate, qmap[name])
                        else: 
                            raise Exception
                            #newstate = fill_zeroes(from_bin(newstate), 15)
                            #print(qmap[name])
                            #print(newstate)
                        newcounts[newstate] += counts[state]
                    finals[name][key] = newcounts
print(finals.keys())
chis = defaultdict(dict)
for circname, exps in finals.items(): 
    print(circname)
    print(exps.keys())
    f1 = exps[('unoptimized', 'simulated', 'base')]
    print(f1.values())
    #f2 = exps[('optimized', 'simulated', 'base')]
    for f2k in exps.keys():
        f2 = exps[f2k]
        if f2k == ('unoptimized', 'simulated', 'base'): 
            continue
        allstates = set(f1.keys()).union(set(f2.keys()))
        #print(sorted(f1.keys()))
        #print(sorted(f2.keys()))
        print(f2k)
        f1l = [f1.get(x, 0) for x in sorted(allstates)]
        print(f1l)
        f1s = sum(f1l)
        f1l = [x/f1s for x in f1l]
        f2l = [f2.get(x, 0) for x in sorted(allstates)]
        print(f2l)
        f2s = sum(f2l)
        f2l = [x/f2s for x in f2l]
        crit = chi2.ppf(0.95, len(allstates)-1)
        print(chisquare(f1l,f2l))
        cs = chisquare(f1l,f2l).statistic
        chis[(f2k)][circname] = cs
        print(crit, cs, chi2.cdf(cs, len(allstates)-1))
        print(crit, cs, chi2.cdf(cs+1, len(allstates)-1))
        print(crit, cs, chi2.cdf(cs-1, len(allstates)-1))
        assert cs == 0 or crit > cs 

for x,y in chis.items():
    print(x)
    print(y.values())
                

#for remap in qmap.values():
#    for i in remap:
#        y = hex(2**i+4+32)
#        y = fill_zeroes(y,15)
#        x = map_forw(y, remap)
#        print(i, remap.get(i,i))
#        print(y)
#        print(x)
#        assert y[14-i] == x[14 - remap.get(i,i)]