import warnings
import pytest


def pytest_configure(config):
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydub.utils")
