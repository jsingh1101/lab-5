#!/usr/bin/env python3
# Author ID: jsingh1101

def read_file_string(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f]

if _name_ == '_main_':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
    def append_file_string(file_name, string_of_lines):
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    with open(file_name_read, 'r') as fr, open(file_name_write, 'w') as fw:
        for i, line in enumerate(fr, 1):
            fw.write(f"{i}:{line}")
