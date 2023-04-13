# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
from setuptools.command.build import build
from git import Repo
import os.path
from glob import glob

__version__ = "0.0.1"   # Verion of PyMurTree

# Clone the Murtree repository and checkout last commit before DCC changes
if not os.path.exists("murtree"):
    repo_url = "https://github.com/MurTree/murtree.git"
    Repo.clone_from(repo_url, "murtree")
    repo = Repo("murtree")
    commit = repo.commit("8f98216533eb946e7c472336dce945f335c54fec")
    repo.git.checkout(commit)


ext_modules = [
    Pybind11Extension("pymurtree",
        (["src/main.cpp"]
        + sorted(glob("murtree/code/MurTree/Utilities/*.cpp"))
        + sorted(glob("murtree/code/MurTree/Engine/*.cpp"))
        + sorted(glob("murtree/code/MurTree/Data Structures/*.cpp"))
        ),
        define_macros = [('VERSION_INFO', __version__)] # passing in the version to the compiled code
    )
]

setup(
    name="pymurtree",
    version=__version__,
    author="Jose Urra and Yasel Quintero",
    author_email="dcc@tudelft.nl",
    url="https://github.com/MurTree/pymurtree",
    description="Python wrapper for the MurTree project",
    ext_modules=ext_modules,
    python_requires=">=3.7",
    cmdclass={"build_ext": build_ext},
    dev_requires=['pytest']
)