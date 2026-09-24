# main.py
import argparse
import os

from detect_static_analysis import analyze_folder_access
from OpenCode_runner import run_opencode_prompt_sync
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="WinClean - Windows Path Cleaning Engine"
    )


    parser.add_argument("--root", help="Filesystem root path")
    parser.add_argument("--script-path", help="Python script file")
    parser.add_argument("--path-command", help="Command path for static analysis")

    args = parser.parse_args()

    def validate_and_normalize_path(path):
        if path:
            normalized = str(Path(path).resolve())
            if not os.path.exists(normalized):
                raise FileNotFoundError(f"Path does not exist: {normalized}")
            return normalized
        return None

    try:
        root = validate_and_normalize_path(args.root)
        script_path = validate_and_normalize_path(args.script_path)
        path_command = args.path_command  # Don't validate - it's a command string

        input_path = (
            script_path or path_command
        )  # Use script_path if available, else path_command

        if not input_path:
            raise ValueError(
                "--script-path or --path-command required for analysis."
            )

        print("Running static analysis...")
        # Pass the original path_command string for command analysis
        analysis = analyze_folder_access(input_path, root or "")

        print("Analysis complete.")
        print("\nIssues found:")
        if analysis:
            for err in analysis:
                print(" -", err)
        else:
            print("No issues detected using static analysis.")
            print("Proceeding to OpenCode prompt for further analysis...")
            print(run_opencode_prompt_sync(broken_code=input_path or ""))

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
