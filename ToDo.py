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
    # Archivos C#
    'cs',  
    'aspx',
]


#Nombre de la carpetas que no se analizaran
FOLDERS_IGNORE = [ #Todo
    '.git',
]


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
            print(text[:-1])
    return result


def main():
    if (len(sys.argv) == 2):
        sfile = sys.argv[1]
    else:
        sfile = 'todo-list.txt'
    fw = open(sfile, 'w', encoding="utf8")
    print("=======================\nLista ToDo del Proyecto \n=======================")
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