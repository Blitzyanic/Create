import os
import sys
import webbrowser

# templates
use_lang = ['.py', '.go', '.sh', '.nggyu', '.java', '.c', '.cc', '.cpp', '.cp', '.txt', '.html', '.js', '.css', '.web']
name = 'default'
text = 'txt'
py_text = "\n\nif __name__ == '__main__':\n    pass"
sh_text = '#!/bin/sh\n'
java_text = '#!/bin/java\npublic class ' + name + ' {\n\n    public static void main(String args[]) {\n\n    //awesome Code\n    }\n}'
c_text = '#include <stdio.h>\n\nint main() {\n\n    //best code of the world\n\nreturn 0;\n}'
cc_text = '#include <iostream>\n\nint main() {\n\n    //best code of the world\n\nreturn 0;\n}'
html_text = '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <link rel="stylesheet" href="style.css">\n    <script type="text/javascript" src="main.js"></script>\n    <title>Document</title>\n</head>\n<body>\n    </body>\n</html>'
css_text = ''
js_text = ''
go_text = 'package main\n\n\n\nfunc main() {\n    \n}'


# Create
class Create:
    def __init__(self, name, lang, text):
        self.name = name
        self.lang = lang
        self.text = text

    def create_file(self):
        file = open(self.name + self.lang, 'w')  # create file
        file.write(self.text)  # write file

    def create_project(self, arr_file: list, arr_text: list):  # need [names of the file(s)] && [text for the file(s)]
        self.arr_text = arr_text
        self.arr_file = arr_file

        os.system('mkdir ' + self.name)  # create project folder
        for j in self.arr_file:
            file = open(self.name + '/' + j, 'w')  # create file(s)
            for k in self.arr_text:
                file.write(k)  # write file(s)
        os.system('git init ' + self.name)  # init git in project


if __name__ == '__main__':
    # read input & split by '.'
    inp = sys.argv[1]
    (name, lang) = os.path.splitext(inp)

    # check lang
    if not lang in use_lang:
        print(f"wrong lang\nplease only use {use_lang}")
        exit()
    # shell
    if lang == '.sh':
        Create(name, lang, sh_text).create_file()
    # Java
    elif lang == ".java":
        Create(name, lang, java_text).create_file()
    # C
    elif lang == '.c':
        Create(name, lang, c_text).create_file()
    # C++
    elif lang == '.cpp' or lang == '.cc' or lang == '.cp':
        Create(name, lang, cc_text).create_file()


    # create project
    # web
    elif lang in ['.html', '.js', '.css', '.web']:
        Create(name, lang, text).create_project(['index.html', 'style.css', 'main.js'], [html_text, css_text, js_text])
    # python
    elif lang == '.py':
        Create(name, lang, py_text).create_project(['main.py'], [py_text])
        os.system(f"python -m venv {name}/env")
    # Go
    elif lang == ".go":
        Create(name, lang, text).create_project(['main.go'], [go_text])
        os.system(f"go mod init $USER.com/{name}")
        os.system(f"mv go.mod {name}/")
    # easteregg
    elif lang == '.nggyu':
        try:
            os.system('sl')
        except:
            pass

        webbrowser.open("www.rickroll.de", 1, True)
