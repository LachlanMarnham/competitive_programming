def end_zeros(num: int) -> int:
    num_str = str(num)
    zeros_count = 0
    for idx in range(len(num_str) - 1, -1, -1):
        if num_str[idx] == "0":
            zeros_count += 1
        else:
            break
    return zeros_count
