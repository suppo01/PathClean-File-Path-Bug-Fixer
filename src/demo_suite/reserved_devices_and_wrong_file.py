"""This module contains code that targets reserved devices and wrong file paths for static analysis testing."""

def main():
    """Code Targeting Reserved Devices and Wrong File Paths for Static Analysis Testing."""
    # This is a reserved device name on Windows
    with open(r"/test_suite/NUL", "w", encoding="utf-8") as f:
        f.write("This will cause an error on Windows.")

    # This is a wrong file path that may cause issues
    with open(r"/test_suite/invalid/path/to/file.txt", "w", encoding="utf-8") as f:
        f.write("This will cause an error due to invalid path.")

    # This is a reserved device name on Windows and an invalid path
    with open(r"/test_suite/COM8/invalid/path/to/file.txt", "w", encoding="utf-8") as f:
        f.write("This will cause an error due to reserved device name and invalid path.")

if __name__ == "__main__":
    main()
