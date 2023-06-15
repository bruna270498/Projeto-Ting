def exists_word(word, instance):
    data = []

    for file_info in instance._queue:
        lines = []
        file = file_info["linhas_do_arquivo"]
        for number_line, line in enumerate(file, start=1):
            if word.lower() in line.lower():
                lines.append({'linha': number_line})

        if lines:
            dictionary = {
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": lines
            }
            data.append(dictionary)
    print(data)
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
