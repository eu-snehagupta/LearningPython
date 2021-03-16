def solu2(N):
    first_idx_1 = N.find('1')
    if first_idx_1 == -1:
        return 0
    else:
        return len(N.replace("0", "")) + len(N) - first_idx_1 - 1