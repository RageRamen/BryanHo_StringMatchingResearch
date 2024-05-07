
def build_transition_table(pattern, alphabet):
    m = len(pattern)
    transition_table = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for char in alphabet:
            next_state = min(m, state + 1)
            while next_state > 0 and pattern[:next_state] != pattern[state - next_state + 1:state] + char:
                next_state -= 1
            transition_table[state][char] = next_state

    return transition_table

def finite_automaton(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    alphabet = set(text + pattern)
    transition_table = build_transition_table(pattern, alphabet)
    state = 0

    for i in range(n):
        state = transition_table[state].get(text[i], 0)
        if state == m:
            occurrences.append(i - m + 1)

    return occurrences

text = "magikarpgyarados"
pattern = "rpgy"
print("Occurrences found at indices:", finite_automaton(text, pattern))
