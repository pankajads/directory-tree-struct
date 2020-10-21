import os

def treegen(startpath):
    num_dirs = 0
    num_files = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 2 * (level)
        print('{}|{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 2 * (level + 1)
        num_dirs = num_dirs + 1
        for f in files:
            print('{}|--{}'.format(subindent, f))
            num_files = num_files + 1
    print('{} directories, {} files'.format(num_dirs,num_files))