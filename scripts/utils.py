import fnmatch
import os

class unit_file:
    def __init__(self, name, path, ext) -> None:
        self.name = name
        self.path = path
        self.ext = ext

    def __repr__(self) -> str:
        return f"unit_file({self.name}, {self.path}, {self.ext})"
    def __str__(self) -> str:
        return self.name + self.ext


def find_files(directories, extensions):
    res = []
    for directory in directories:
        for file in os.listdir(directory):
            for extension in extensions:
                if fnmatch.fnmatch(file, f'*.{extension}'):
                    (name, ext) = os.path.splitext(file)
                    res.append(unit_file(name, directory, ext))
                    break
    return res