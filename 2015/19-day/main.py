import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

rxns_raw = lines[:-2]

rxns = {}
for r in rxns_raw:
    in_, out_ = r.strip().split(' =>')
    rxns[in_] = rxns.get(in_, []) + [out_.strip()]

chain_str = lines[-1].strip()
chain = re.findall("([A-Z][a-z]?|[e])", chain_str)

resultants = set()
for i, atom in enumerate(chain):
    possible_output = rxns.get(atom, [])
    for poss in possible_output:
        chain_copy = chain.copy()
        chain_copy[i] = poss
        new_chain = ''.join(chain_copy)
        resultants.add(new_chain)

n_res = len(resultants)
print(f'A ::: Number of possible new molecules: {n_res}')

rev_rxns = {}
for k, v in rxns.items():
    for out_ in v:
        rev_rxns[out_] = k

old_chains = {chain_str}

counter = 0
for _ in range(10):
    new_chains = set()

    for ch in old_chains:
        for out_, in_ in rev_rxns.items():
            if out_ in ch:
                match_locs = [(m.start(), m.end()) for m in re.finditer(out_, ch)]
                for a, b in match_locs:
                    new_chain = ch[:a] + in_ + ch[b:]
                    new_chains.add(new_chain)

    counter += 1
    if 'e' in new_chains:
        break
    else:
        old_chains = new_chains.copy()

    if counter == 4:
        import pdb; pdb.set_trace()

