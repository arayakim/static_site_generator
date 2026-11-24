import os
import shutil
from generate_pages_recursive import generate_pages_recursive
import sys


def copy_directory(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    source_contents = os.listdir(source)

    for item in source_contents:
        file_or_dir = os.path.join(source, item)
        new_path = os.path.join(destination, item)

        if os.path.isfile(file_or_dir):
            print(f"Copying file: {file_or_dir}")
            shutil.copy(file_or_dir, destination)
        else:
            os.mkdir(new_path)
            copy_directory(file_or_dir, new_path)


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    copy_directory("static", "docs")
    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath
    )

main()
