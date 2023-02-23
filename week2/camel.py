def camel_to_snake(camel):
    words = []
    start = 0
    for i in range(1, len(camel)):
        if camel[i].isupper():
            words.append(camel[start:i].lower())
            start = i
    words.append(camel[start:].lower())
    return "_".join(words)


camel = input("camelCase: ").strip()
snake = camel_to_snake(camel)
print("snake_case:", snake)
