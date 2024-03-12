def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    mutated_string = ''.join(string_list)

    return mutated_string

