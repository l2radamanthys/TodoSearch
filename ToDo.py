# -*- coding: utf-8 -*-

import sys
import os


# Incluir, excluir archivos en donde desea buscar
EXT_SEARCH = [
    # 'txt',
    # 'csv',
    'py',
    'js',
    'ts',
    'css',
    'scss',
    'html',
    'hbs', #handlebars
    # Archivos C#
    'cs',
    'aspx',
]


#Nombre de la carpetas que no se analizaran
FOLDERS_IGNORE = [ #Todo
    '.git',
    'node_modules',
    'dist',
]

COLORES = {
    'red': u"\u001b[31m",
    'reset': u"\u001b[0m",
    'black': u"\u001b[30m",
    'green': u"\u001b[32m",
    'yellow': u"\u001b[33m",
    'blue': u"\u001b[34m",
    'magenta': u"\u001b[35m",
    'cyan': u"\u001b[36m",
    'white': u"\u001b[37m",
}

def colorprint(*args, **kargs):
    try:
        color = kargs['color']
        kargs.pop('color', None)
        print(COLORES[color], end='')
        print(*args, **kargs)
        print(COLORES['reset'], end='')
    except:
        print(*args, **kargs)

def get_todo_marks(file_path):
    l =  0 #line number
    result = []
    for line in open(file_path, 'r', encoding="utf8", errors='ignore').readlines():
        l += 1
        if "#todo" in line.lower():
            pos = line.lower().find("#todo") + 5
            comment = line[pos:].strip()
            if comment == "":
                comment = "*NO HAY COMENTARIOS*"
            text ="[{}][{}] - {}\n".format(file_path, l, comment)
            result.append(text)
            colorprint(f"[{file_path}][{l}] ", color='yellow', end='')
            colorprint(comment, color='green')
    print()
    return result


def main():
    if (len(sys.argv) == 2):
        sfile = sys.argv[1]
    else:
        sfile = 'todo-list.txt'
    fw = open(sfile, 'w', encoding="utf8")
    colorprint("\n# Lista ToDo del Proyecto \n", color='cyan')
    fw.write("Lista ToDo del Proyecto \n=======================\n\n")
    path = os.getcwd()
    for root, d, f in os.walk(path):
        for file in os.listdir(root):
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path) and file != 'ToDo.py':
                ext = file.split(".")[-1]
                if ext in EXT_SEARCH:
                    result = get_todo_marks(file_path)
                    for line in result:
                        fw.write(line)
    fw.close()
    

if __name__ == '__main__':
    main()
