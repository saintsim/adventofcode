#!/usr/bin/env python3

FILE_SYSTEM = []
DIRECTORY_PTRS = dict()
previous_dir = None
current_dir = None


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

    def calc_size(self, empty, depth):
        if empty:
            if not self.child_dirs:
                self.dir_size = self.file_sizes
            return self.dir_size
        if self.dir_size is None:
            dir_size = 0
            for child_dir in self.child_dirs:
                if depth > 2000:
                    return None
                # print(self.dir_name, ' -> ', child_dir)
                child_size = DIRECTORY_PTRS.get(child_dir).calc_size(empty, depth + 1)
                if child_size is None:
                    return None
                else:
                    dir_size += child_size
            self.dir_size = self.file_sizes + dir_size
        return self.dir_size


def change_directory(dir):
    global current_dir, previous_dir
    if dir == '..':
        current_dir = previous_dir
    else:
        dir_ptr = get_dir_ptr(dir)
        if dir not in DIRECTORY_PTRS:
            DIRECTORY_PTRS[dir] = dir_ptr
        previous_dir = current_dir
        current_dir = dir


def get_dir_ptr(dir):
    if dir not in DIRECTORY_PTRS:
        ptr = Directory(dir, current_dir)
        DIRECTORY_PTRS[dir] = ptr
    else:
        ptr = DIRECTORY_PTRS.get(dir)
    return ptr


def list_files(files):
    for file in files:
        file_tokens = file.split()
        if file_tokens[0] == 'dir':
            dir_name = file_tokens[1]
            get_dir_ptr(dir_name)
            DIRECTORY_PTRS.get(current_dir).add_child_dir(dir_name)
        else:
            file = File(file_tokens[1], int(file_tokens[0]))
            DIRECTORY_PTRS.get(current_dir).add_file(file)


def command_processor(line):
    if line.startswith('cd'):
        change_directory(line.replace('cd ', ''))
    else:
        list_files(line.split('\n')[1:])


def total():
    sum_threshold = 100000
    total_size = 0
    # for dir_name, dir_ptr in DIRECTORY_PTRS.items():
    #     if dir_name == 'scarps':
    #         continue
    #     dir_ptr.calc_size(True)

    while DIRECTORY_PTRS.get('/').dir_size is None:
        for dir_name, dir_ptr in DIRECTORY_PTRS.items():
            if dir_ptr.dir_size is None:
                DIRECTORY_PTRS.get(dir_name).dir_size = dir_ptr.calc_size(False, 0)
        count = 0
        for dir_name, dir_ptr in DIRECTORY_PTRS.items():
            count += dir_ptr.dir_size is None
        print('foo...: ', count, "/", len(DIRECTORY_PTRS))

    return 0
    #     if dir_size <= sum_threshold:
    #         total_size += dir_size
    # return total_size


def linux(file_str):
    commands = file_str.split('$')
    global current_dir
    current_dir = 'scarps'
    DIRECTORY_PTRS[current_dir] = Directory('None', None)
    for line in commands:
        if line == "":
            continue
        command_processor(line.strip())

    return total()


if __name__ == '__main__':
    with open('input', 'r') as file:
        print('Result: ' + str(linux(file.read())))