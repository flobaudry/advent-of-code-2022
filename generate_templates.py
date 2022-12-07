import os
import shutil


def generate_templates():
    for i in range(1, 26):
        dir_name = f"problem_{i:02d}"
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            shutil.copy('template/inputs.txt', f'{dir_name}/inputs.txt')
            shutil.copy('template/problem.py', f'{dir_name}/{dir_name}.py')


if __name__ == '__main__':
    generate_templates()
