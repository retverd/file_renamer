from os import walk, rename, remove

delim = '\\'
to_remove = "[SW.BAND] "
to_delete = ["[SW.BAND] Прочти перед изучением!.docx", "SHAREWOOD_ZERKALO_COM_90000_курсов_на_нашем_форуме!.url"]


def clean_up() -> None:
    path = input("Enter path to folder or press Enter to process data in O:\\ ")
    if path == '':
        path = 'O:\\'
    for subdir, dirs, _ in walk(path):
        for dir in dirs:
            if dir.startswith(to_remove):
                rename(subdir + dir, subdir + dir.replace(to_remove, ''))
                print(f"Переименовал папку {dir} в папке {subdir}")
    for subdir, _, files in walk(path):
        for file in files:
            if file in to_delete:
                remove(subdir + delim + file)
                print(f"Удалил файл {file} в папке {subdir}")
            elif file.startswith(to_remove):
                rename(subdir + delim + file, subdir + delim + file.replace(to_remove, ''))
                print(f"Переименовал файл {file} в папке {subdir}")


if __name__ == '__main__':
    clean_up()
    input("Press any key to exit...")
