from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "raw"
def generated_path(value):
    value = Path(value)
    if value.is_absolute(): value = Path(value.name)
    path = ROOT / "results" / "generated" / value
    path.parent.mkdir(parents=True, exist_ok=True)
    return str(path)
