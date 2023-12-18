# Write a recursive function for generating all permutations of an input string. Return them as a set.
# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.
# To start, assume every character in the input string is unique.
# Your function can have loops—it just needs to also be recursive.

def generate_all_permutations(s: str, c: str = None) -> list[str]:
    if c == None: return generate_all_permutations(s[:-1], s[-1:])
    if c == "": return []
    result = []
    

# cats
## ast
## sat
## sta
## tsa
## tas


# cat
# ca
# c