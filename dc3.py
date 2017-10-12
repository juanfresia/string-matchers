from string_encoder import encode_string

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
    text = encode_string(text)
    text.append(0)
    pattern = encode_string(pattern)
    suffix_array = dcm(text)
    result = binary_search_pattern(pattern, suffix_array, text)

    return result


def binary_search_pattern(pattern, suffix_array, text):
    initial = 0
    end = len(suffix_array) - 1

    while initial <= end:
        mid = initial + ((end - initial) // 2)
        comparator = matches(text, suffix_array[mid], pattern)

        if comparator == PATTERN_EQUAL:
            left = binary_search_left(pattern, suffix_array, text, mid)
            right = binary_search_right(pattern, suffix_array, text, mid)

            return suffix_array[left:right + 1]

        if comparator == PATTERN_GREATER:
            initial = mid + 1
        else:
            end = mid - 1

    return []


def binary_search_right(pattern, suffix_array, text, index):
    initial = index
    end = len(suffix_array) - 1

    while initial <= end:
        mid = initial + ((end - initial) // 2)

        comparator = matches(text, suffix_array[mid], pattern)

        if comparator == PATTERN_EQUAL:
            if mid == len(suffix_array) - 1 or matches(text, suffix_array[mid + 1], pattern) != PATTERN_EQUAL:
                return mid
            comparator = PATTERN_GREATER

        if comparator == PATTERN_GREATER:
            initial = mid + 1
        else:
            end = mid - 1


def binary_search_left(pattern, suffix_array, text, index):
    initial = 0
    end = index

    while initial <= end:
        mid = initial + ((end - initial) // 2)

        comparator = matches(text, suffix_array[mid], pattern)

        if comparator == PATTERN_EQUAL:
            if mid == len(suffix_array) or matches(text, suffix_array[mid - 1], pattern) != PATTERN_EQUAL:
                return mid
            comparator = PATTERN_LESSER

        if comparator == PATTERN_GREATER:
            initial = mid + 1
        else:
            end = mid - 1


def multiple_string_matching_dc3(text, patterns):
    text = encode_string(text)
    text.append(0)

    suffix_array = dcm(text)

    result = []

    for pattern in patterns:
        pattern = encode_string(pattern)
        result.append(binary_search_pattern(pattern, suffix_array, text))

    return result


def sample_suffixes_create(text):
    text = text
    result = [[], [], []]
    for i in range(len(text)):
        item = text[i:i + 3]

        if len(item) < 3:
            continue

        result[i % 3].append((item, i))
    result[1].extend(result[2])
    return result[0], result[1]


def radix_sort(list_to_sort, size=256):
    sorted_list = list_to_sort

    if len(sorted_list) == 0:
        return sorted_list[:]

    for i in range(1, len(sorted_list[0][0]) + 1):
        buckets = [[] for _ in range(size)]

        for word in sorted_list:
            # print(word[0][-i])
            buckets[word[0][-i]].append(word)

        sorted_list = []
        for i in range(len(buckets)):
            for triplet in buckets[i]:
                sorted_list.append(triplet)

    return sorted_list


def radix_sort2(list_to_sort, text, size=256):
    sorted_list = list_to_sort

    if len(sorted_list) == 0:
        return sorted_list[:]

    for i in range(3):
        buckets = [[] for _ in range(max(len(list_to_sort), size))]

        for index in sorted_list:
            _index = index + 2 - i
            buckets[text[_index]].append(index)

        sorted_list = []

        for i in range(len(buckets)):
            for triplet in buckets[i]:
                sorted_list.append(triplet)

    return sorted_list


def dcm(sequence, alphabet_size=256):
    base_sequence = sequence

    base_sequence += (0, 0)

    b0, b12 = sample_suffixes_create(base_sequence)
    sorted_b12 = radix_sort2([m[1] for m in b12], base_sequence, alphabet_size)

    rank = ["|" for _ in range(len(base_sequence))]
    rank[-1] = 0
    rank[-2] = 0

    pos_rank = 1
    compare_base = base_sequence[sorted_b12[0]:sorted_b12[0] + 3]
    for i, index in enumerate(sorted_b12):
        actual_base = base_sequence[sorted_b12[i]:sorted_b12[i] + 3]
        if compare_base != actual_base:
            compare_base = actual_base
            pos_rank += 1
        rank[index] = pos_rank

    if pos_rank < len(sorted_b12):
        r_sequence = []
        for a in range(1, 3):
            for i in range(a, len(rank) - 2, 3):
                r_sequence.append(rank[i])
        r_sequence.append(0)
        out = dcm(r_sequence, pos_rank + 1)

        sorted_b12 = []
        for i in range(1, len(out)):
            rank_index = b12[out[i]][1]
            rank[rank_index] = i
            sorted_b12.append(rank_index)

    to_sort = []
    for i in range(len(b0)):
        rank_value = rank[i * 3 + 1]
        to_sort.append(((b0[i][0][0], rank_value), b0[i][1]))
        if rank_value > alphabet_size:
            alphabet_size = rank_value
        if b0[i][1] > alphabet_size:
            alphabet_size = b0[i][1]

    sorted_a0 = radix_sort(to_sort, alphabet_size)

    merge = merge_step(rank, sorted_a0, sorted_b12, base_sequence)
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
    print(dcm((1, 1, 1, 1, 1, 0)), "==", ["aa"])
    print(string_matching_dc3("aaaaaa", "ana"), "==", "")
    print(string_matching_dc3("yabbadabbado", "abbadab"), "==", "1")
    print(string_matching_dc3("hola mundo", "mundo"), "==", "5")
    print(string_matching_dc3("yabbadabbado", "yab"), "==", "0")
