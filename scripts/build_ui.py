from pathlib import Path
import subprocess

# Paths
ROOT = Path(__file__).resolve().parents[1]
UI_SRC = ROOT / "ui"
UI_DST = ROOT / "src" / "fcontrol" / "ui" / "qt_generated"

# Ensure output dir exists
UI_DST.mkdir(parents=True, exist_ok=True)


def compile_ui_file(ui_file: Path):
    output_file = UI_DST / f"{ui_file.stem}.py"

    cmd = [
        "pyside6-uic",
        str(ui_file),
        "-o",
        str(output_file),
    ]

    subprocess.run(cmd, check=True)
    print(f"Compiled: {ui_file.name} -> {output_file.name}")


def main():
    ui_files = list(UI_SRC.glob("*.ui"))

    if not ui_files:
        print("No .ui files found.")
        return

    for ui_file in ui_files:
        compile_ui_file(ui_file)


if __name__ == "__main__":
    main()
