GREATER = 1
LESSER = -1
EQUAL = 0


def matches(text, index, patter):
    for i in range(len(patter)):
        if i + index >= len(text):
            return GREATER

        pattern_char = patter[i]
        text_char = text[i + index]

        if pattern_char == text_char:
            continue

        if pattern_char < text_char:
            return LESSER
        return GREATER

    return EQUAL


def string_matching_dc3(text, pattern):
    sufix_array = dcm(text)

    initial = 0
    end = len(sufix_array) - 1

    while initial <= end:
        mid = initial + ((end - initial) // 2)
        # print("{} {} {}".format(initial, mid, end))
        # print("{}".format(text[sufix_array[mid]:]))
        comparation = matches(text, sufix_array[mid], pattern)
        #print(">{}<".format(comparation))
        if comparation == EQUAL:
            return [sufix_array[mid]]

        if comparation == GREATER:
            initial = mid + 1
        else:
            end = mid - 1

    return []


def sample_suffixes_create(text):
    text = tuple(text)
    result = [[], [], []]
    for i in range(len(text)):
        item = text[i:i + 3]

        if len(item) < 3:
            item += (0,) * (3 - len(item))

        result[i % 3].append((item, i))

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


def dcm(sequence):
    base_sequence = sequence
    if isinstance(sequence, str):
        base_sequence = tuple([ord(c) if c != "$" else 0 for c in sequence])

    base_sequence += (0,)

    a0, a1, a2 = sample_suffixes_create(base_sequence)
    a12 = a1 + a2
    sorted_a12 = radix_sort(a12)
    d = generate_lookup(sorted_a12)

    r_sequence = tuple([d[i[0]] for i in a12])
    out = [sorted_a12]

    if len(d) != len(sorted_a12):
        out = dcm(r_sequence)

    rank = [d[base_sequence[i:i + 3]] if i % 3 != 0 else "|" for i in range(len(base_sequence) - 2)] + [0, 0, 0]

    for i in range(1, len(out)):
        rank_index = a12[out[i]]
        rank[rank_index[1]] = i

    to_sort = []
    for i in range(len(a0)):
        rank_value = rank[i * 3 + 1]
        to_sort.append(((a0[i][0][0], rank_value), a0[i][1]))

    sorted_a0 = radix_sort(to_sort)

    merge = merge_step(rank, sorted_a0, sorted_a12, base_sequence)
    return merge


def merge_step(ranks, sorted_b0, sorted_b12, original_sequence):
    i = 0
    j = 0
    merge = []

    while i < len(sorted_b12) and j < len(sorted_b0):
        sample_index = sorted_b12[i][1]
        nsample_index = sorted_b0[j][1]

        if original_sequence[sample_index] < original_sequence[nsample_index]:
            merge.append(sample_index)
            i += 1
            continue

        if original_sequence[sample_index] > original_sequence[nsample_index]:
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
        if original_sequence[sample_index + 1] < original_sequence[nsample_index + 1]:
            merge.append(sample_index)
            i += 1
            continue

        if original_sequence[sample_index + 1] > original_sequence[nsample_index + 1]:
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
    print(dcm("yabbadabbado"))
    print(string_matching_dc3("banana", "ana"))
