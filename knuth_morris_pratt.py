

def compute_prefix_function(pattern):
    m = len(pattern)
    prefix_function = [0] * m
    border = 0

    for i in range(1, m):
        while border > 0 and pattern[i] != pattern[border]:
            border = prefix_function[border - 1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        prefix_function[i] = border

    return prefix_function

def knuth_morris_pratt(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    prefix_function = compute_prefix_function(pattern)
    border = 0

    for i in range(n):
        while border > 0 and text[i] != pattern[border]:
            border = prefix_function[border - 1]
        if text[i] == pattern[border]:
            border += 1
        else:
            border = 0
        if border == m:
            occurrences.append(i - m + 1)
            border = prefix_function[border - 1]

    return occurrences

text = "magikarpgyarados"
pattern = "rpgy"
print("Occurrences found at indices:", knuth_morris_pratt(text, pattern))
