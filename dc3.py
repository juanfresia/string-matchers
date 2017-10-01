def string_matching_dc3(text, pattern):
    return []


def sample_suffixes_create(text):
    text = tuple(text)
    result = [[], [], []]
    for i in range(len(text)):
        item = text[i:i + 3]

        if len(item) < 3:
            item += (0,) * (3 - len(item))

        print(item)

        result[i % 3].append((item, i))

    print(result)
    return result


def radix_sort(list_to_sort):
    sorted_list = list_to_sort

    if len(sorted_list) == 0:
        return sorted_list[:]

    for i in range(1, len(sorted_list[0][0]) + 1):
        buckets = {}

        for word in sorted_list:
            bucket = buckets.get(word[0][-i], [])
            bucket.append(word)
            buckets[word[0][-i]] = bucket

        sorted_list = []
        for k in sorted(buckets.keys()):
            for triplet in buckets[k]:
                sorted_list.append(triplet)

    return sorted_list


def generate_lookup(_list):
    lookup = {}

    i = 1
    for substring, _ in _list:
        if not substring in lookup:
            lookup[substring] = i
            i += 1

    return lookup


def DC3():
    pass


def dcm():
    base_str = tuple([ord(c) if c != "$" else 0 for c in "yabbadabbado$"])

    a0, a1, a2 = sample_suffixes_create(base_str)
    a12 = a1 + a2
    sorted_a12 = radix_sort(a12)
    d = generate_lookup(sorted_a12)

    step_1 = tuple([d[i[0]] for i in a12]) + (0,)

    e0, e1, e2 = sample_suffixes_create(step_1)
    sorted_e12 = radix_sort(e1 + e2)
    n = generate_lookup(tuple(sorted_e12))

    rank = [n[step_1[i:i + 3]] if i % 3 != 0 else "|" for i in range(len(step_1) - 2)] + [0, 0]

    # Non sample
    to_sort = []
    for i in range(len(e0)):
        to_sort.append(((e0[i][0][0], rank[i * 3 + 1]), e0[i][1]))

    sorted_e0 = radix_sort(to_sort)

    merge = merge_step(rank, sorted_e0, sorted_e12, step_1)

    print(a12)
    rank = [d[base_str[i:i + 3]] if i % 3 != 0 else "|" for i in range(len(base_str) - 2)] + [0, 0, 0]

    print(rank)
    for i in range(1, len(merge)):
        rank_index = a12[merge[i]]
        rank[rank_index[1]] = i
    print(rank)

    to_sort = []
    for i in range(len(a0)):
        print(i * 3 + 1, rank)
        rank_value = rank[i * 3 + 1]
        to_sort.append(((a0[i][0][0], rank_value), a0[i][1]))

    sorted_a0 = radix_sort(to_sort)

    merge = merge_step(rank, sorted_a0, sorted_a12, base_str)
    print(merge)
    print(a0)

def merge_step(ranks, sorted_b0, sorted_b12, original_secuence):
    i = 0
    j = 0
    merge = []

    while i < len(sorted_b12) and j < len(sorted_b0):
        sample_index = sorted_b12[i][1]
        nsample_index = sorted_b0[j][1]

        if original_secuence[sample_index] < original_secuence[nsample_index]:
            merge.append(sample_index)
            i += 1
            continue

        if original_secuence[sample_index] > original_secuence[nsample_index]:
            merge.append(nsample_index)
            j += 1
            continue

        # B1 case
        if sample_index % 3 == 1:
            if ranks[sample_index + 1] < ranks[nsample_index + 1]:
                merge.append(sample_index)
                i += 1
            else:
                merge.append(nsample_index)
                j += 1
            continue

        # B2 case
        if original_secuence[sample_index + 1] < original_secuence[nsample_index + 1]:
            merge.append(sample_index)
            i += 1
            continue

        if original_secuence[sample_index + 1] > original_secuence[nsample_index + 1]:
            merge.append(nsample_index)
            j += 1
            continue

        if ranks[sample_index + 2] < ranks[nsample_index + 2]:
            merge.append(sample_index)
            i += 1
        else:
            merge.append(nsample_index)
            j += 1

    while i < len(sorted_b12):
        sample_index = sorted_b12[i][1]
        merge.append(sample_index)
        i += 1

    while j < len(sorted_b0):
        nsample_index = sorted_b0[j][1]
        merge.append(nsample_index)
        j += 1

    return merge


if __name__ == '__main__':
    dcm()
