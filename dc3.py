PATTERN_GREATER = 1
PATTERN_LESSER = -1
PATTERN_EQUAL = 0


def matches(text, index, patter):
    for i in range(len(patter)):
        if i + index >= len(text):
            return PATTERN_GREATER

        pattern_char = patter[i]
        text_char = text[i + index]

        if pattern_char == text_char:
            continue

        if pattern_char < text_char:
            return PATTERN_LESSER
        return PATTERN_GREATER

    return PATTERN_EQUAL


def string_matching_dc3(text, pattern):
    text = tuple([ord(c) - ord("a") + 1 if c != "$" else 0 for c in text] + [0])
    pattern = tuple([ord(c) - ord("a") + 1 if c != "$" else 0 for c in pattern])

    sufix_array = dcm(text)

    #    print(sufix_array)

    initial = 0
    end = len(sufix_array) - 1

    result = []

    while initial <= end:
        mid = initial + ((end - initial) // 2)

        comparation = matches(text, sufix_array[mid], pattern)

        if comparation == PATTERN_EQUAL:
            if mid == 0 or matches(text, sufix_array[mid - 1], pattern) != PATTERN_EQUAL:
                while mid < len(sufix_array) and matches(text, sufix_array[mid], pattern) == PATTERN_EQUAL:
                    result.append(sufix_array[mid])
                    mid += 1
                break

            comparation = PATTERN_LESSER

        if comparation == PATTERN_GREATER:
            initial = mid + 1
        else:
            end = mid - 1

    return result


def sample_suffixes_create(text):
    text = tuple(text)
    result = [[], [], []]
    for i in range(len(text)):
        item = text[i:i + 3]

        if len(item) < 3:
            continue

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


def radix_sort2(list_to_sort, text):
    sorted_list = sorted(list_to_sort)

    if len(sorted_list) == 0:
        return sorted_list[:]

    for i in range(3):
        buckets = {}

        for index in sorted_list:
            _index = index + 2 - i
            bucket = buckets.get(text[_index], [])
            bucket.append(index)
            buckets[text[_index]] = bucket

        sorted_list = []

        for k in sorted(buckets.keys()):
            for triplet in buckets[k]:
                sorted_list.append(triplet)

    return sorted_list


def generate_lookup(_list):
    lookup = {}

    i = 1
    for substring, _ in _list:
        if substring not in lookup:
            lookup[substring] = i
            i += 1

    return lookup


def dcm(sequence):
    base_sequence = sequence

    base_sequence += (0, 0)

    a0, a1, a2 = sample_suffixes_create(base_sequence)
    a12 = a1 + a2
    sorted_a12 = radix_sort2([m[1] for m in a12], base_sequence)

    rank = ["|" for _ in range(len(base_sequence))]
    rank[-1] = 0
    rank[-2] = 0

    temp = []
    pos_rank = 1
    compare_base = base_sequence[sorted_a12[0]:sorted_a12[0] + 3]
    for i, index in enumerate(sorted_a12):
        actual_base = base_sequence[sorted_a12[i]:sorted_a12[i] + 3]
        if compare_base != actual_base:
            compare_base = actual_base
            pos_rank += 1
        rank[index] = pos_rank

    out = sorted_a12

    if pos_rank < len(sorted_a12):
        r_sequence = []
        for a in range(1, 3):
            for i in range(a, len(rank) - 2, 3):
                r_sequence.append(rank[i])
        r_sequence.append(0)
        out = dcm(r_sequence)
        #        print(out)
        for i in range(1, len(out)):
            rank_index = a12[out[i]][1]
            rank[rank_index] = i

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
        sample_index = sorted_b12[i]
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
        sample_index = sorted_b12[i]
        merge.append(sample_index)
        i += 1

    while j < len(sorted_b0):
        nsample_index = sorted_b0[j][1]
        merge.append(nsample_index)
        j += 1

    return merge


if __name__ == '__main__':
    print(string_matching_dc3("aaaaaa", "ana"), "==", "")
    print(string_matching_dc3("yabbadabbado", "abbadab"), "==", "1")
    print(string_matching_dc3("hola mundo", "mundo"), "==", "5")
    print(string_matching_dc3("yabbadabbado", "yab"), "==", "0")
