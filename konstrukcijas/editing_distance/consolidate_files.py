import re
from pathlib import Path
import sys

def concat_matching_files(directory, pattern, output_file):
    """
    Concatenate contents of files in `directory` whose names match `pattern`
    and write the result to `output_file`.

    - `pattern` is a regex matched against the filename (not the full path).
    - Files are sorted alphabetically by filename.
    - `output_file` is excluded from inputs even if it matches the pattern.
    """
    dir_path = Path(directory)
    if not dir_path.is_dir():
        raise NotADirectoryError(f"{directory!r} is not a directory")

    out_path = Path(output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    regex = re.compile(pattern)

    # Collect matching files (top level only), excluding the output file if in the same dir
    try:
        out_resolved = out_path.resolve()
    except FileNotFoundError:
        out_resolved = out_path.absolute()  # Fallback; resolution may fail if not yet created

    matches = []
    for entry in dir_path.iterdir():
        if entry.is_file() and regex.search(entry.name):
            try:
                if entry.resolve() == out_resolved:
                    continue  # don't include the output file
            except FileNotFoundError:
                pass
            matches.append(entry)

    # Sort alphabetically by filename
    matches.sort(key=lambda p: p.name)

    # Concatenate into output_file
    with out_path.open("w", encoding="utf-8", newline="") as w:
        for path in matches:
            with path.open("r", encoding="utf-8") as r:
                while True:
                    chunk = r.read(1024*1024)
                    if not chunk:
                        break
                    w.write(chunk)

    return [p.name for p in matches]

def main():
    if len(sys.argv) < 2:
        print("Usage: python consolidate_files.py <n>")
        sys.exit(1)
    i = int(sys.argv[1])
    pattern = r"^obtuse_{}_([A-Z]+).txt$".format(i)
    concat_matching_files("../../docs/obtuse", pattern, f"xx_obtuse_{i}.txt")

if __name__=='__main__':
    main()