import subprocess


def test_package_installed():
    """
    Test if the package is installed (imports work)
    """
    from xmidas.main import start_xmidas  # noqa: F401


def test_entry_point_installed():
    """
    Test that the entry point is installed and the application can be started.
    """
    assert subprocess.call(["xmidas", "-h"]) == 0
