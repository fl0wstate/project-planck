from collections import Counter
from itertools import combinations, permutations, product


vertices = list(product((-1, 1), repeat=3))
vertex_index = {vertex: index for index, vertex in enumerate(vertices)}
edges = tuple(
    (i, j)
    for i, a in enumerate(vertices)
    for j, b in enumerate(vertices)
    if i < j and sum(x != y for x, y in zip(a, b)) == 1
)
edge_index = {edge: index for index, edge in enumerate(edges)}


def permutation_parity(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def spatial_maps(determinant_filter=None):
    maps = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            determinant = permutation_parity(permutation)
            determinant *= signs[0] * signs[1] * signs[2]
            if determinant_filter is not None and determinant != determinant_filter:
                continue
            vertex_map = tuple(
                vertex_index[
                    tuple(signs[i] * vertex[permutation[i]] for i in range(3))
                ]
                for vertex in vertices
            )
            maps.append((determinant, vertex_map))
    return maps


def orient_edges(bits):
    # Each bit identifies the endpoint receiving the anionic O donor.
    return tuple(edges[index][bit] for index, bit in enumerate(bits))


def is_connected(vertex_set):
    reached = {next(iter(vertex_set))}
    while True:
        expanded = reached | {
            b
            for a, b in edges
            if a in reached and b in vertex_set
        } | {
            a
            for a, b in edges
            if b in reached and a in vertex_set
        }
        if expanded == reached:
            return reached == vertex_set
        reached = expanded


def valid(bits, require_connected=True):
    o_endpoints = orient_edges(bits)
    indegree = Counter(o_endpoints)
    if any(indegree[vertex] not in (1, 2) for vertex in range(8)):
        return False
    high_valent = {vertex for vertex in range(8) if indegree[vertex] == 2}
    return not require_connected or is_connected(high_valent)


def transform(bits, vertex_map):
    transformed = [None] * len(edges)
    for index, (a, b) in enumerate(edges):
        mapped_a = vertex_map[a]
        mapped_b = vertex_map[b]
        mapped_edge = tuple(sorted((mapped_a, mapped_b)))
        mapped_index = edge_index[mapped_edge]
        o_endpoint = vertex_map[(a, b)[bits[index]]]
        transformed[mapped_index] = mapped_edge.index(o_endpoint)
    return tuple(transformed)


def orbits(states, maps):
    unseen = set(states)
    result = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {transform(seed, vertex_map) for _, vertex_map in maps}
        result.append(orbit)
        unseen -= orbit
    return result


def vertex_set_orbits(states, maps):
    unseen = set(states)
    result = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {
            frozenset(vertex_map[vertex] for vertex in seed)
            for _, vertex_map in maps
        }
        result.append(orbit)
        unseen -= orbit
    return result


proper_maps = spatial_maps(determinant_filter=1)
improper_maps = spatial_maps(determinant_filter=-1)
all_maps = proper_maps + improper_maps

locally_valid = {
    bits for bits in product((0, 1), repeat=12) if valid(bits, require_connected=False)
}
connected = {bits for bits in locally_valid if valid(bits, require_connected=True)}

proper_orbits = orbits(connected, proper_maps)
all_orbits = orbits(connected, all_maps)
unrestricted_orbits = orbits(locally_valid, proper_maps)
unrestricted_all_orbits = orbits(locally_valid, all_maps)

connected_domains = {
    frozenset(domain)
    for domain in combinations(range(8), 4)
    if is_connected(set(domain))
}
domain_orbits = vertex_set_orbits(connected_domains, proper_maps)

fixed_counts = Counter()
for _, vertex_map in proper_maps:
    fixed = sum(transform(bits, vertex_map) == bits for bits in connected)
    fixed_counts[fixed] += 1

assert len(edges) == 12
assert len(proper_maps) == 24
assert len(improper_maps) == 24
assert len(locally_valid) == 450
assert len(connected) == 216
assert len(proper_orbits) == 12
assert Counter(map(len, proper_orbits)) == {24: 8, 6: 4}
assert len(all_orbits) == 6
assert len(unrestricted_orbits) == 24
assert len(unrestricted_all_orbits) == 14
assert len(connected_domains) == 38
assert len(domain_orbits) == 4
assert fixed_counts == {0: 14, 8: 9, 216: 1}

print(f"locally_valid={len(locally_valid)}")
print(f"connected={len(connected)}")
print(f"proper_orbits={len(proper_orbits)} sizes={dict(Counter(map(len, proper_orbits)))}")
print(f"proper_fixed_counts={dict(sorted(fixed_counts.items()))}")
print(f"all_spatial_orbits={len(all_orbits)}")
print(f"unrestricted_proper_orbits={len(unrestricted_orbits)}")
print(f"unrestricted_all_spatial_orbits={len(unrestricted_all_orbits)}")
print(f"connected_domains={len(connected_domains)} domain_orbits={len(domain_orbits)}")
print("VERIFIED 12")
