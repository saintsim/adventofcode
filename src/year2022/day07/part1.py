#!/usr/bin/env python3

DIRECTORY_PTRS = dict()
CURRENT_DIR_PATH = ""


class File:

    def __init__(self, file_name, file_size):
        self.file_name = file_name
        self.file_size = file_size


class Directory:

    def __init__(self, dir_name, parent_dir):
        self.dir_name = dir_name
        self.files = []
        self.child_dirs = []
        self.parent_dir = parent_dir
        self.file_sizes = 0
        self.dir_size = None

    def add_file(self, file):
        if file not in self.files:
            self.files.append(file)
            self.file_sizes += file.file_size

    def add_child_dir(self, dir):
        if dir not in self.child_dirs:
            self.child_dirs.append(dir)

    def calc_size(self):
        if self.dir_size is None:
            dir_size = 0
            for child_dir in self.child_dirs:
                # print(self.dir_name, ' -> ', child_dir)
                child_size = DIRECTORY_PTRS.get(child_dir).calc_size()
                dir_size += child_size
            self.dir_size = self.file_sizes + dir_size
        return self.dir_size


def change_directory(dir):
    global CURRENT_DIR_PATH
    if dir == '..':
        CURRENT_DIR_PATH = "/".join(CURRENT_DIR_PATH.split('/')[:-1])
    else:
        if dir == '/':
            CURRENT_DIR_PATH = '/'
        else:
            CURRENT_DIR_PATH += (('/' if CURRENT_DIR_PATH != '/' else "") + dir)
        get_dir_ptr(CURRENT_DIR_PATH)


def get_dir_ptr(dir):
    if dir not in DIRECTORY_PTRS:
        ptr = Directory(dir, CURRENT_DIR_PATH)
        DIRECTORY_PTRS[dir] = ptr
    else:
        ptr = DIRECTORY_PTRS.get(dir)
    return ptr


def get_path(sub_dir):
    if CURRENT_DIR_PATH == '/':
        return '/' + sub_dir
    else:
        return CURRENT_DIR_PATH + '/' + sub_dir


def list_files(files):
    for file in files:
        file_tokens = file.split()
        if file_tokens[0] == 'dir':
            dir_name = file_tokens[1]
            get_dir_ptr(CURRENT_DIR_PATH)
            get_dir_ptr(get_path(dir_name))
            DIRECTORY_PTRS.get(CURRENT_DIR_PATH).add_child_dir(get_path(dir_name))
        else:
            file = File(file_tokens[1], int(file_tokens[0]))
            DIRECTORY_PTRS.get(CURRENT_DIR_PATH).add_file(file)


def command_processor(line):
    if line.startswith('cd'):
        change_directory(line.replace('cd ', ''))
    else:
        list_files(line.split('\n')[1:])


def total():
    sum_threshold = 100000
    total_size = 0
    for dir_name, dir_ptr in DIRECTORY_PTRS.items():
        dir_size = dir_ptr.calc_size()
        if dir_size <= sum_threshold:
            print('-->', dir_name, dir_size)
            total_size += dir_size
    return total_size


def linux(file_str):
    commands = file_str.split('$')
    for line in commands:
        if line == "":
            continue
        command_processor(line.strip())
    return total()


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(linux(file.read())))