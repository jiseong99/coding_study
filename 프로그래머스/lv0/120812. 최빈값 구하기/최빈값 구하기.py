def solution(array):
    answer = -1

    freq_check = {}

    for num in array:
        if num not in freq_check:
            freq_check[num] = 0
        freq_check[num] += 1

    freq_items = sorted(freq_check.items(), key=lambda x: (-x[1]))

    if (len(freq_items) > 1 and freq_items[0][1] != freq_items[1][1]) or len(freq_items) == 1:
        answer = freq_items[0][0]

    return answer