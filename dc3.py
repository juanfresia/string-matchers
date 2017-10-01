def string_matching_dc3(text, pattern):
    return []


def sample_suffixes_create(text):
    text = tuple(text)
    result = [[], [], []]
    for i in range(len(text) - 2):
        result[i % 3].append(text[i:i + 3])
    return result


def radix_sort(list_to_sort):
    sorted_list = list_to_sort

    if len(sorted_list) == 0:
        return sorted_list[:]

    for i in range(1, len(sorted_list[0]) + 1):
        buckets = {}

        for word in sorted_list:
            bucket = buckets.get(word[-i], [])
            bucket.append(word)
            buckets[word[-i]] = bucket

        sorted_list = []
        for k in sorted(buckets.keys()):
            for triplet in buckets[k]:
                sorted_list.append(triplet)

    return sorted_list


def generate_lookup(_list):
    lookup = {}

    i = 1
    for substring in _list:
        if not substring in lookup:
            lookup[substring] = i
            i += 1

    return lookup


def DC3():
    base_str = tuple([ord(c) for c in "yabbadabbado"] + [0, 0])

    a0, a1, a2 = sample_suffixes_create(base_str)
    sorted_sample_positions = radix_sort(a1 + a2)
    lookup_table = generate_lookup(sorted_sample_positions)

    step_1 = tuple([lookup_table[i] for i in a1 + a2])

    if (len(lookup_table)) != len(a1 + a2):
        step_1 = DC3(step_1)

    sample = [n[step_1[i:i + 3]] if i % 3 != 0 else "|" for i in range(len(step_1) - 2)] + [0, 0]

    to_sort = []
    for i in range(len(a0)):
        to_sort.append((a0[i][0], sample[i * 3 + 1]))

    result = radix_sort(to_sort)
    print(result)

    base_str = tuple(base_str)
    sample = [d[base_str[i:i + 3]] if i % 3 != 0 else "|" for i in range(len(base_str) - 2)] + ["|", 0, 0]
    print(sample)


if __name__ == '__main__':
    base_str = tuple([c for c in "yabbadabbado$$"])

    a0, a1, a2 = sample_suffixes_create(base_str)
    b = radix_sort(a1 + a2)
    d = generate_lookup(b)

    step_1 = tuple([d[i] for i in a1 + a2]) + (0, 0)

    e0, e1, e2 = sample_suffixes_create(step_1)
    m = radix_sort(e1 + e2)
    n = generate_lookup(tuple(m))

    step_2 = tuple([n[i] for i in e1 + e2]) + (0, 0)

    sample = [n[step_1[i:i + 3]] if i % 3 != 0 else "|" for i in range(len(step_1) - 2)] + [0, 0]

    # Non sample
    to_sort = []
    for i in range(len(e0)):
        to_sort.append((e0[i][0], sample[i * 3 + 1]))

    result = radix_sort(to_sort)



    base_str = tuple(base_str)
    sample = [d[base_str[i:i + 3]] if i % 3 != 0 else "|" for i in range(len(base_str) - 2)] + ["|", 0, 0]
    print(sample)
