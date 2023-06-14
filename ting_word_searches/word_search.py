def exists_word(word, instance):
    """Aqui irá sua implementação"""
    data = []
    for arquivo in instance._queue:
        occurrences = []
        with open(arquivo['linhas_do_arquivo'], 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if word.lower() in line.lower():
                    occurrences.append({"linha": line_number})

    if occurrences:
        data.append({
                "palavra": word,
                "arquivo": arquivo['linhas_do_arquivo'],
                "ocorrencias": occurrences
            })
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
