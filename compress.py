"""
Compresses the `ebyte_e32` module using `python_minifier` into the `output` folder.
"""

import os
import shutil

from pathlib import Path

import python_minifier

from rich import print as printf


def sizeof_fmt(num):
    """Formats a given number into a human-friendly byte size."""
    for unit in ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}"
        num /= 1024.0
    return None  # Prevents pylint from having a fit about inconsistent returns


def ig_f(directory, files):
    """Callback used to filter files in a given directory."""
    return [file for file in files if os.path.isfile(os.path.join(directory, file))]


printf("Preparing directories...")
shutil.rmtree("./output-min/", ignore_errors=True)
os.mkdir("./output-min")
shutil.rmtree("./output-mpy/", ignore_errors=True)
shutil.rmtree("./output-min-mpy/", ignore_errors=True)

printf("Copying some files...")
shutil.copytree('ebyte_e32', 'output-min/ebyte_e32', ignore=ig_f)

printf("Scanning files...")
result = list(Path("./ebyte_e32/").rglob("*.[Pp][Yy]"))

printf("Minifying files...")
for input_path in result:
    input_path: Path
    output_path = os.path.abspath(os.path.join(input_path.cwd(), "./output-min", input_path))
    
    printf(f"> {input_path}")
    
    with open(input_path, "r", encoding="utf-8") as file_in:
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
            # convert_posargs_to_args=True,
            preserve_shebang=False,
            remove_asserts=True,
            remove_debug=True,
            remove_explicit_return_none=True,
        )
        
        original_size = sizeof_fmt(len(source_code.encode('utf-8')))
        minimized_size = sizeof_fmt(len(source_code_min.encode('utf-8')))
        compression_ratio = len(source_code_min.encode('utf-8')) / len(source_code.encode('utf-8')) * 100
        
        printf(f"-> {original_size} => {minimized_size} ({compression_ratio:.1f}%)")
        
        with open(output_path, "x", encoding="utf-8") as file_out:
            file_out.write(source_code_min)
