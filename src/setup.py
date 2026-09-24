# setup.py

from setuptools import setup


setup(
    name="pathclean",
    version="0.1.0",
    description="Windows Path Cleaning Engine",
    py_modules=["main", "detect_static_analysis", "OpenCode_runner", "symbolic_class"],
    entry_points={
        "console_scripts": [
            "pathclean=main:main",
        ],
    },
)
