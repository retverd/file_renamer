import os
import re

TARGET_PATTERN = r'\1.\2.\3'

ok_patterns = {'jpg': re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}\.\d{2}\.\d{2}(|\.\d{2})\.jpg$', re.IGNORECASE),
               'mp4': re.compile(r'^\d{4}-\d{2}-\d{2} \d{2}\.\d{2}\.\d{2}\.mp4$', re.IGNORECASE)}

to_patterns = {re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2})-(\d{2})-(\d{2}\.jpg)$', re.IGNORECASE): TARGET_PATTERN,
               re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2})-(\d{2})-(\d{2}\.\d{2}\.jpg)$', re.IGNORECASE): TARGET_PATTERN,
               re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2})-(\d{2})-(\d{2}\.mp4)$', re.IGNORECASE): TARGET_PATTERN,
               re.compile(r'^VID_(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2}.mp4)$',
                          re.IGNORECASE): r'\1-\2-\3 \4.\5.\6'}


def rename() -> None:
    path = input("Enter path to folder: ")
    for subdir, _, files in os.walk(path):
        for file in files:
            ok_flag = False
            for key, ok_pattern in ok_patterns.items():
                m = re.match(ok_pattern, file)
                if m is not None:
                    ok_flag = True
            if not ok_flag:
                for from_pattern, to_pattern in to_patterns.items():
                    m = re.match(from_pattern, file)
                    if m is not None:
                        new_file = re.sub(from_pattern, to_pattern, file)
                        os.rename(os.path.join(os.path.join(subdir, file)),
                                  os.path.join(os.path.join(subdir, new_file)))
                        print(f'Filename {file} was not OK. It was renamed to {new_file}.')


if __name__ == '__main__':
    rename()
    input("Press any key to exit...")
