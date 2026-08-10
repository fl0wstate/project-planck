from itertools import combinations, permutations, product


vertices = list(product((-1, 1), repeat=3))
vertex_index = {vertex: index for index, vertex in enumerate(vertices)}


def edge(a, b):
    return tuple(sorted((a, b)))


edges = {
    edge(i, j)
    for i, a in enumerate(vertices)
    for j, b in enumerate(vertices)
    if i < j and sum(x != y for x, y in zip(a, b)) == 1
}


def perfect_matchings(remaining):
    if not remaining:
        yield frozenset()
        return

    first = min(remaining)
    for candidate in remaining:
        current_edge = edge(first, candidate)
        if current_edge not in edges:
            continue
        for rest in perfect_matchings(remaining - {first, candidate}):
            yield rest | {current_edge}


def parity(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def spatial_maps(proper_only):
    maps = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            determinant = parity(permutation) * signs[0] * signs[1] * signs[2]
            if proper_only and determinant != 1:
                continue
            maps.append(
                tuple(
                    vertex_index[
                        tuple(signs[i] * vertex[permutation[i]] for i in range(3))
                    ]
                    for vertex in vertices
                )
            )
    return maps


def transform(state, spatial_map):
    matching, a_edges = state
    mapped_matching = frozenset(
        edge(spatial_map[a], spatial_map[b]) for a, b in matching
    )
    mapped_a_edges = frozenset(
        edge(spatial_map[a], spatial_map[b]) for a, b in a_edges
    )
    return mapped_matching, mapped_a_edges


def orbits(states, maps):
    unseen = set(states)
    result = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {transform(seed, spatial_map) for spatial_map in maps}
        result.append(orbit)
        unseen -= orbit
    return result


matchings = set(perfect_matchings(set(range(8))))
states = {
    (matching, frozenset(a_edges))
    for matching in matchings
    for a_edges in combinations(matching, 2)
}

proper_maps = spatial_maps(proper_only=True)
all_maps = spatial_maps(proper_only=False)
proper_orbits = orbits(states, proper_maps)
all_orbits = orbits(states, all_maps)

assert len(edges) == 12
assert len(matchings) == 9
assert len(states) == 54
assert len(proper_maps) == 24
assert len(all_maps) == 48
assert len(proper_orbits) == 5
assert sorted(map(len, proper_orbits)) == [6, 12, 12, 12, 12]
assert len(all_orbits) == 4

print(f"edges={len(edges)}")
print(f"perfect_matchings={len(matchings)}")
print(f"colored_states={len(states)}")
print(f"proper_orbits={len(proper_orbits)} sizes={sorted(map(len, proper_orbits))}")
print(f"all_spatial_orbits={len(all_orbits)} sizes={sorted(map(len, all_orbits))}")
print("VERIFIED 5")
