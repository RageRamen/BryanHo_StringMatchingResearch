
def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    # Precompute hash value for the pattern
    pattern_hash = hash(pattern)

    # Iterate through the text
    for i in range(n - m + 1):
        # Compute hash value for the current window of text
        text_hash = hash(text[i:i + m])
        # Check if the hash values match and if the strings match
        if pattern_hash == text_hash and text[i:i + m] == pattern:
            occurrences.append(i)

    return occurrences

text = "magikarpgyarados"
pattern = "rpgy"
print("Occurrences found at indices:", rabin_karp(text, pattern))
