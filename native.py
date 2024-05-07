
def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences

text = "magikarpgyarados"
pattern = "rpgy"
print("Occurrences found at indices:", naive_string_matching(text, pattern))
