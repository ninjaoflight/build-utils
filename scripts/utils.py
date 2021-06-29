import fnmatch
import os

class unit_file:
    def __init__(self, name, path) -> None:
        self.name = name
        self.path = path

    def __repr__(self) -> str:
        return f"unit_file({self.name}, {self.path})"
    def __str__(self) -> str:
        return self.name


def find_files(directories, extensions):
    res = []
    for directory in directories:
        for file in os.listdir(directory):
            for extension in extensions:
                if fnmatch.fnmatch(file, f'*.{extension}'):
                    res.append(unit_file(file, directory))
                    break
    return res