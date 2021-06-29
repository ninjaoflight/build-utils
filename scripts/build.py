from os import spawnl
from utils import find_files

project_path = "source"

compiler = "clang++"
linker = "lld-link"

include_dirs = [
    f"{project_path}/include"
]
source_dirs = [
    f"{project_path}/src"
]
include_extensions = ["hpp"]
source_extensions = ["cpp"]


include_files = find_files(include_dirs, include_extensions)
sources = find_files(source_dirs, source_extensions)

print(" -- CONFIG -- ")
print(f"project path:        {project_path}")
print(f"compiler:            {compiler}")
print(f"linker:              {linker}")
print(f"include directories: {[f"{x}" for x in include_dirs]}")
print(f"source directories:  {[f"{x}" for x in source_dirs]}")
print(" -- FILES --")
print(f"hpp: {include_files}")
print(f"cpp: {sources}")


print(" -- BUILD --")
for source in sources:
    print(f" -> {source}")
    command = f"{compiler} -c {source} -I "

