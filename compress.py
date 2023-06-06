# Imports
import distutils.dir_util
import os
import shutil

from pathlib import Path

import python_minifier

from rich import print


def sizeof_fmt(num):
    for unit in ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}"
        num /= 1024.0


def ig_f(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]


print("Preparing directories...")
shutil.rmtree("./output/", ignore_errors=True)
os.mkdir("./output")
shutil.copytree('ebyte_e32', 'output/ebyte_e32', ignore=ig_f)

print("Scanning files...")
result = list(Path("./ebyte_e32/").rglob("*.[Pp][Yy]"))
# print(result)

print("Minifying files...")
for input_path in result:
    input_path: Path
    output_path = os.path.abspath(os.path.join(input_path.cwd(), "./output", input_path))
    
    print(f"> {input_path}")
    
    with open(input_path, "r") as file_in:
        source_code = file_in.read()
        source_code_min = python_minifier.minify(
            source=source_code,
            remove_annotations=True,
            remove_pass=True,
            remove_literal_statements=True,
            combine_imports=True,
            hoist_literals=False,
            rename_locals=True,
            preserve_locals=[],
            rename_globals=False,
            preserve_globals=[],
            remove_object_base=True,
            #convert_posargs_to_args=True,
            preserve_shebang=False,
            remove_asserts=True,
            remove_debug=True,
            remove_explicit_return_none=True,
        )
        print("-> {} => {} ({:.1f}%)".format(
            sizeof_fmt(len(source_code.encode('utf-8'))),
            sizeof_fmt(len(source_code_min.encode('utf-8'))),
            len(source_code_min.encode('utf-8')) / len(source_code.encode('utf-8')) * 100
        ))
        
        with open(output_path, "x") as file_out:
            file_out.write(source_code_min)
