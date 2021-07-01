import subprocess
from utils import find_files

project_path = "source"

compiler = "clang++"
linker = "lld-link"
output_dir = "build"

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
print(f"output path         : {output_dir}")
print(f"project path        : {project_path}")
print(f"compiler            : {compiler}")
print(f"linker              : {linker}")
print(f"include directories : {include_dirs}")
print(f"source directories  : {source_dirs}")
print(" -- FILES --")
print(f"hpp: {[str(x) for x in include_files]}")
print(f"cpp: {[str(x) for x in sources]}")


print(" -- BUILD --")

for source in sources:
    print(f" -> {source}")
    command = f"{compiler} -c {f'{source.path}/{source}'} {' '.join([f'-I {x}' for x in include_dirs])} -o {output_dir}/{source.name}.o "
    print(command)
    subprocess.call(command)

