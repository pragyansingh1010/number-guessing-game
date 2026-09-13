from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source_files = list(ROOT.glob("*.py")) + list(ROOT.glob("*.html"))
assert source_files, "no project source file found"
assert all(p.stat().st_size > 0 for p in source_files)
print("Number Guessing Game smoke check passed")
