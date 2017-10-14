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
    """result = [[], [], []]
    for i in range(len(text)):
        item = text[i:i + 3]

        if len(item) < 3:
            continue

        result[i % 3].append(i)
    result[1].extend(result[2])
    return result[0], result[1]"""
    b1 = [i for i in range(1, len(text) - 2, 3)]
    b2 = [i for i in range(2, len(text) - 2, 3)]

    b1.extend(b2)
    return b1


def radix_sort(list_to_sort, size=256):
    sorted_list = list_to_sort

    if len(sorted_list) == 0:
        return sorted_list[:]

    """
    for i in range(1, len(sorted_list[0][0]) + 1):
        buckets = [0] * (size + 1)

        for word in sorted_list:
            if not buckets[word[0][-i]]:
                buckets[word[0][-i]] = []
            buckets[word[0][-i]].append(word)

        sorted_list = []
        for bucket in buckets:
            if bucket:
                sorted_list.extend(bucket)

    return sorted_list"""

    for i in range(1, len(sorted_list[0][0]) + 1):
        buckets = [0] * (size + 1)

        for word in sorted_list:
            buckets[word[0][-i]] += 1

        for m in range(1, len(buckets)):
            buckets[m] += buckets[m - 1]

        new_sorted_list = [None] * len(sorted_list)

        len_sorted_list = len(sorted_list)

        for j in range(1, len_sorted_list + 1):
            word = sorted_list[len_sorted_list - j]

            buckets[word[0][-i]] -= 1
            new_sorted_list[buckets[word[0][-i]]] = word

        sorted_list = new_sorted_list

    return sorted_list


def radix_sort2(list_to_sort, text, size=8):
    sorted_list = list_to_sort

    if len(sorted_list) == 0:
        return sorted_list[:]

    for i in range(3):
        buckets = [0] * (size + 1)

        for index in sorted_list:
            char_index = index + 2 - i
            char = text[char_index]

            buckets[char] += 1

        for m in range(1, len(buckets)):
            buckets[m] += buckets[m - 1]

        new_sorted_list = [None] * len(sorted_list)

        len_sorted_list = len(sorted_list)

        for j in range(1, len_sorted_list + 1):
            index = sorted_list[len_sorted_list - j]
            char_index = index + 2 - i
            char = text[char_index]

            buckets[char] -= 1
            new_sorted_list[buckets[char]] = index

        sorted_list = new_sorted_list

    return sorted_list


def are_equal_bases(base_a, base_b, secuence):
    for i in range(3):
        if secuence[base_a + i] != secuence[base_b + i]:
            return False
    return True


def dcm(sequence, alphabet_size=256):
    base_sequence = sequence

    base_sequence += (0, 0)

    b12 = sample_suffixes_create(base_sequence)
    sorted_b12 = radix_sort2(b12, base_sequence, alphabet_size)

    rank = ["|"] * len(base_sequence)
    rank[-1] = 0
    rank[-2] = 0

    pos_rank = generate_ranks(base_sequence, rank, sorted_b12)

    if pos_rank < len(sorted_b12):
        recursive_rank_update(b12, pos_rank, rank, sorted_b12)

    alphabet_size, to_sort = create_b0_sorting(alphabet_size, rank, base_sequence)

    sorted_a0 = radix_sort(to_sort, alphabet_size)

    merge = merge_step(rank, sorted_a0, sorted_b12, base_sequence)
    return merge


def recursive_rank_update(b12, pos_rank, rank, sorted_b12):
    r_sequence = [rank[i] for i in range(1, len(rank) - 2, 3)]
    r_2 = [rank[i] for i in range(2, len(rank) - 2, 3)]
    r_2.append(0)
    r_sequence.extend(r_2)
    out = dcm(r_sequence, pos_rank + 1)
    for i in range(1, len(out)):
        rank_index = b12[out[i]]
        rank[rank_index] = i
        sorted_b12[i - 1] = rank_index


def create_b0_sorting(alphabet_size, rank, sequence):
    to_sort = [None] * (len(sequence) // 3)

    for i in range(len(to_sort)):
        to_sort[i] = [None, None], i * 3
        c = to_sort[i]
        c[0][1] = rank[c[1] + 1]
        c[0][0] = sequence[c[1]]
        if c[1] > alphabet_size:
            alphabet_size = c[1]
    return alphabet_size, to_sort


def generate_ranks(base_sequence, rank, sorted_b12):
    pos_rank = 1
    compare_base = sorted_b12[0]
    for i, index in enumerate(sorted_b12):
        actual_base = sorted_b12[i]
        if not are_equal_bases(compare_base, actual_base, base_sequence):
            compare_base = actual_base
            pos_rank += 1
        rank[index] = pos_rank
    return pos_rank


def merge_step(ranks, sorted_b0, sorted_b12, original_sequence):
    i = 0
    j = 0
    merge = [None] * len(sorted_b0) + [None] * len(sorted_b12)

    while i < len(sorted_b12) and j < len(sorted_b0):
        sample_index = sorted_b12[i]
        nsample_index = sorted_b0[j][1]

        if original_sequence[sample_index] < original_sequence[nsample_index]:
            merge[i + j] = sample_index
            i += 1
            continue

        if original_sequence[sample_index] > original_sequence[nsample_index]:
            merge[i + j] = nsample_index
            j += 1
            continue

        # B1 case
        if sample_index % 3 == 1:
            if ranks[sample_index + 1] < ranks[nsample_index + 1]:
                merge[i + j] = sample_index
                i += 1
            else:
                merge[i + j] = nsample_index
                j += 1
            continue

        # B2 case
        if original_sequence[sample_index + 1] < original_sequence[nsample_index + 1]:
            merge[i + j] = sample_index
            i += 1
            continue

        if original_sequence[sample_index + 1] > original_sequence[nsample_index + 1]:
            merge[i + j] = nsample_index
            j += 1
            continue

        if ranks[sample_index + 2] < ranks[nsample_index + 2]:
            merge[i + j] = sample_index
            i += 1
        else:
            merge[i + j] = nsample_index
            j += 1

    while i < len(sorted_b12):
        sample_index = sorted_b12[i]
        merge[i + j] = sample_index
        i += 1

    while j < len(sorted_b0):
        nsample_index = sorted_b0[j][1]
        merge[i + j] = nsample_index
        j += 1

    return merge


if __name__ == '__main__':
    print(dcm((1, 1, 1, 1, 1, 1, 1, 0)), "==", ["aa"])
    print(string_matching_dc3("aaaaaa", "ana"), "==", "")
    print(string_matching_dc3("aaaaaaa", "ana"), "==", "")
    print(string_matching_dc3("ba", "b"), "==", "0")
    print(string_matching_dc3("aba", "b"), "==", "1")
    print(string_matching_dc3("aaba", "b"), "==", "2")
    print(string_matching_dc3("aaaba", "b"), "==", "3")
    print(string_matching_dc3("aaaaba", "b"), "==", "4")
    print(string_matching_dc3("aaaaaba", "b"), "==", "5")
    print(string_matching_dc3("aaaaaaba", "b"), "==", "6")
    print(string_matching_dc3("aaaaaaaba", "b"), "==", "7")
    print(string_matching_dc3("aaaaaaaaba", "b"), "==", "8")
    print(string_matching_dc3("aaaaaaaaaba", "b"), "==", "9")
    print(string_matching_dc3("aaaaaaaaaaba", "b"), "==", "10")
    print(string_matching_dc3("yabbadabbado", "abbadab"), "==", "1")
    print(string_matching_dc3("hola mundo", "mundo"), "==", "5")
    print(string_matching_dc3("yabbadabbado", "yab"), "==", "0")
    print(string_matching_dc3("banana", "ban"), "==", "0")
    print(string_matching_dc3("banana", "ana"), "==", "1,3")
