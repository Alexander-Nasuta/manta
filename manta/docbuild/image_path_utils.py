import importlib.resources as pkg_resources
import manta.resources


def get_coala_background_abs_path() -> str:
    return str(pkg_resources.files(manta.resources).joinpath('Coala_background.svg'))


def get_manim_logo_abs_path() -> str:
    return str(pkg_resources.files(manta.resources).joinpath('Manim_icon.svg'))


def get_rwth_logo_abs_path() -> str:
    return str(pkg_resources.files(manta.resources).joinpath('RWTH_Logo.svg'))


def get_manta_logo_abs_path() -> str:
    return str(pkg_resources.files(manta.resources).joinpath('logo.png'))


def get_wzl_logo_abs_path() -> str:
    return str(pkg_resources.files(manta.resources).joinpath('wzl.svg'))


if __name__ == '__main__':
    print(get_coala_background_abs_path())
