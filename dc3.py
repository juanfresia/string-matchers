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

    for i in range(1, 4):
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
        print(substring)
        if not substring in lookup:
            lookup[substring] = i
            i += 1

    return lookup


if __name__ == '__main__':
    base_str = "yabbadabbado$$"

    a0, a1, a2 = sample_suffixes_create(base_str)
    b = radix_sort(a1 + a2)
    d = generate_lookup(b)

    step_1 = [d[i] for i in a1 + a2]

    e0, e1, e2 = sample_suffixes_create(step_1 + [0, 0])
    m = radix_sort(e1 + e2)
    n = generate_lookup(m)

    step_2 = [n[i] for i in e1 + e2]

    print(step_2)
    base_str = tuple(base_str)
    sample = [str(d[base_str[i:i + 3]]) if i % 3 != 0 else "|" for i in range(len(base_str) - 2)] + ["|", "0", "0"]
    print(sample)
