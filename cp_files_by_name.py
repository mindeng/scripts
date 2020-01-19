#! /usr/bin/env python3

import sys
import os
import shutil
import argparse


# 在目标目录中按名字查找文件，返回找到的文件路径列表。
def find_files_by_name(dst_dir, filename):
    ret = []
    for root, dirs, files in os.walk(dst_dir):
        ret.extend(map(lambda name: os.path.join(root, name),
                       filter(lambda name: name == filename, files)))
    return ret


def cp_file(src, dst):
    shutil.copy2(src, dst)


# 按文件名在目标目录中查找文件，如果只找到一个目标文件，则从源路径拷贝到目标路径；
# 否则打印警告信息。
# 注意：如果源目录中有多个文件同名，则会出现多次拷贝覆盖同一个文件的现象。
def cp_file_by_names(src_dir, dst_dir, dry_run=False):
    copied_num, ambiguous_num, not_found_num = 0, 0, 0
    for root, dirs, files in os.walk(src_dir):
        for name in files:
            found_path = find_files_by_name(dst_dir, os.path.basename(name))
            if len(found_path) > 1:
                print('warning: more than one file found:')
                print('\t%s' % '\n\t'.join(found_path))
                ambiguous_num += 1
            elif len(found_path) == 0:
                print('warning: file not found: %s' % name)
                not_found_num += 1
            else:
                src, dst = os.path.join(root, name), found_path[0]
                print('cp %s to %s' % (name, dst))
                if not dry_run:
                    cp_file(src, dst)
                copied_num += 1

    print('''total copied: \t%d
found more than one: \t%d
files not found: \t%d''' % (copied_num, ambiguous_num, not_found_num))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='copy files by matched name')
    parser.add_argument('src', type=str)
    parser.add_argument('dst', type=str)
    parser.add_argument('-n', '--dry-run', action='store_true')

    args = parser.parse_args()
    cp_file_by_names(args.src, args.dst, args.dry_run)
