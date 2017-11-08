import argparse
import os
import datetime
import shutil
import re

# Работа с аргументами командной строки
parser = argparse.ArgumentParser(prog='Convert pictures and docs to article',
                                description='This is help')

def readable_dir(prospective_dir):
    if not os.path.isdir(prospective_dir):
        raise argparse.ArgumentTypeError("readable_dir:{0} "
                                        "is not a valid path".
                                        format(prospective_dir))
    if os.access(prospective_dir, os.R_OK):
        return prospective_dir
    else:
        raise Exception("readable_dir:{0} is not a readable dir".
                        format(prospective_dir))

parser.add_argument('-p', '--path',
                    help='path to dir with input files',
                    type=readable_dir, default='/tmp/non_existent_dir')
args = parser.parse_args()
paramerts = vars(args)
path = paramerts['path']

# Список файлов в дирректории
list_files = []
for entry in os.scandir(path):
   if not entry.name.startswith('.') and entry.is_file():
       list_files.append(entry.name)

# Текущая дата
date_today = datetime.date.today().strftime("%d_%m_%Y")

# Создание каталога
dir_for_images = path + date_today
try:
    os.mkdir(dir_for_images, mode=0o755,)
except FileExistsError:
    print("Дирректория с именем {0} уже существует".format(dir_for_images))

# Копирование и переименование картинок
i = 0
for file in list_files:
    # print(path + file)
    pattern = re.compile(r".*\.(jpg|png|jpeg)$", re.I)
    pattern_glav = re.compile(r"glav\.(jpg|png|jpeg)$", re.I)
    if pattern.match(file) and not pattern_glav.match(file):
        name_without_extension = os.path.splitext(file)[0]
        print(i)
        shutil.copyfile(path + file, dir_for_images + "/" +
                        file.replace(name_without_extension, str(i)).lower())
        i += 1
    elif pattern_glav.match(file):
        shutil.copyfile(path + file, dir_for_images + "/" + file.lower())
