from os import walk, rename, remove

delim = '\\'
list_to_remove = ["[SW.BAND] ", "[www.slifki.info] "]
list_to_delete = ["[SW.BAND] Прочти перед изучением!.docx",
                  "SHAREWOOD_ZERKALO_COM_90000_курсов_на_нашем_форуме!.url",
                  "[www.slifki.info]Спасибо за загрузку!.docx"]


def clean_up_folders(path: str) -> None:
    for subdir, dirs, _ in walk(path):
        for dir in dirs:
            for to_remove in list_to_remove:
                if dir.startswith(to_remove):
                    rename(subdir + dir, subdir + dir.replace(to_remove, ''))
                    print(f"Переименовал папку {dir} в папке {subdir}")


def clean_up_files(path: str) -> None:
    for subdir, _, files in walk(path):
        for file in files:
            if file in list_to_delete:
                remove(subdir + delim + file)
                print(f"Удалил файл {file} в папке {subdir}")
            else:
                for to_remove in list_to_remove:
                    if file.startswith(to_remove):
                        rename(subdir + delim + file, subdir + delim + file.replace(to_remove, ''))
                        print(f"Переименовал файл {file} в папке {subdir}")


if __name__ == '__main__':
    path = input("Enter path to folder or press Enter to process data in O:\\ ")
    if path == '':
        path = 'O:\\'

    clean_up_folders(path)
    clean_up_files(path)
    input("Press any key to exit...")
