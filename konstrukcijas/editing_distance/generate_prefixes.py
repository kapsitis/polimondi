def generate_strings(n):
    if n <= 0:
        return []

    # letters = ['A', 'C', 'E']
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    opp_letters = {'A': 'D', 'B': 'E', 'C': 'F', 'D': 'A', 'E': 'B', 'F': 'C'}

    results = []

    def dfs(current_string):
        if len(current_string) == n:
            results.append(current_string)
            return
        for letter in letters:
            if not current_string or (current_string[-1] != letter and opp_letters[current_string[-1]] != letter):
                dfs(current_string + letter)

    dfs('')
    results = list(filter(lambda x: x[0:2] in ['AB', 'AC'], results))
    return sorted(results)

# Example usage:
n = 5
print(generate_strings(n))