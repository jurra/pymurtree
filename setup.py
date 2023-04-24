# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup
from git import Repo
import os.path
from glob import glob

# Define package metadata
package_name = 'pymurtree'
extension_name = 'lib'
__version__ = "0.0.1"

# Clone the Murtree repository and checkout last commit before DCC changes
if not os.path.exists("murtree"):
    repo_url = "https://github.com/MurTree/murtree.git"
    Repo.clone_from(repo_url, "murtree")
    repo = Repo("murtree")
    commit = repo.commit("8f98216533eb946e7c472336dce945f335c54fec")
    repo.git.checkout(commit)


ext_modules = [
    Pybind11Extension(package_name + '.' + extension_name,
        (["src/pymurtree/bindings.cpp"]
        + sorted(glob("murtree/code/MurTree/Utilities/*.cpp"))
        + sorted(glob("murtree/code/MurTree/Engine/*.cpp"))
        + sorted(glob("murtree/code/MurTree/Data Structures/*.cpp"))
        ),
        include_dirs = ["murtree/code/MurTree/Utilities/",
                        "murtree/code/MurTree/Engine/",
                        "murtree/code/MurTree/Data Structures/"],
        define_macros = [('VERSION_INFO', __version__)] # passing in the version to the compiled code
    )
]

setup(
    name=package_name,
    version=__version__,
    author="Jose Urra and Yasel Quintero",
    author_email="dcc@tudelft.nl",
    url="https://github.com/MurTree/pymurtree",
    description="Python wrapper for the MurTree project",
    packages=[package_name],        # only look for a packages called <package_name>
    package_dir={"": "src"},        # look for the root package in the src directory
    ext_modules=ext_modules,
    #python_requires=">=3.7",
    dev_requires=['pytest']
)