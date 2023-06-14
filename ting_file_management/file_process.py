from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for file in instance._queue:
        if file["nome_do_arquivo"] == path_file:
            return None
    fileTxt = txt_importer(path_file)
    dictionary = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(fileTxt),
        "linhas_do_arquivo": fileTxt
    }
    instance.enqueue(dictionary)
    print(dictionary)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        print('Não há elementos')
        return None
    data = instance.dequeue()
    fileRemove = data["nome_do_arquivo"]
    print(f'Arquivo {fileRemove} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if position < 0 or position >= len(instance):
        print('Posição inválida', file=sys.stderr)
        return "Posição inválida"
    metadata = instance.search(position)
    return print(f'{metadata}', file=sys.stdout)
