import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    txt = ".txt"
    if txt not in path_file:
        print('Formato inválido', file=sys.stderr)
        return None
    try:
        with open(path_file, 'r') as text:
            line = text.read().split('\n')
            return line
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
        return None
