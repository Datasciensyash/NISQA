from pathlib import Path

from setuptools import setup

THIS_DIR = Path(__file__).parent


def _load_requirements(path_dir: Path):
    requirements_directory = path_dir / "requirements.txt"
    requirements = []
    with requirements_directory.open("r") as file:
        requirements.extend(line.lstrip() for line in file.readlines())
    return requirements


setup(
    name="nisqa",
    version="0.0.1",
    packages=["nisqa"],
    install_requires=_load_requirements(THIS_DIR),
)