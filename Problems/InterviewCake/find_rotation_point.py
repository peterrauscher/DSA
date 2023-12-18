def find_rotation_point(words):
    for i in range(len(words) - 1):
        word = words[i - 1]
        compare = words[i]
        for c in range(len(word)):
            if word[c] == compare[c]