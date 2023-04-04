def flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)
    count = len(name1) + len(name2)
    flames_word = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
    while len(flames_word) > 1:
        split_index = (count % len(flames_word) - 1)
        if split_index >= 0:
            right = flames_word[split_index + 1:]
            left = flames_word[:split_index]
            flames_word = right + left
        else:
            flames_word = flames_word[:-1]
    return flames_word[0]

name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")
result = flames(name1, name2)
print("Relationship between", name1, "and", name2, "is", result)
