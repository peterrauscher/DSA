# I like parentheticals (a lot).
# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.
# Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).

def find_closing_parenthesis(str, opening):
    nested = 0
    for i in range(opening + 1, len(str)):
        if str[i] == '(':
            nested += 1
        elif str[i] == ')':
            nested -= 1
        if nested == -1: return i
    return False

print(find_closing_parenthesis("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10))