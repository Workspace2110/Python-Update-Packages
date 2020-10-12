"""
Warning:
It will override dependency packages to the latest version.
If you want to easy control dependency packages version, please use poetry to control version.
"""

# import packages
import pkg_resources
from subprocess import call


def update_with_pip():
    print("Warning: It will override dependency packages to the latest version. \
        If you want to easy control dependency packages version, please use poetry to control version.")

    print("Start updating packages")

    # load all packages names
    packages = [dist.project_name for dist in pkg_resources.working_set]

    # Do command: Update packages with pip
    try:
        call("pip install --upgrade " + ' '.join(packages), shell=True)
    except Exception as e:
        print("Error: {error}".format(error=e))

    print("Update finish")


if __name__ == "__main__":
    update_with_pip()
