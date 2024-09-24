import pathlib as pl

path_of_this_file = pl.Path(__file__).resolve()
docbuild_dir = path_of_this_file.parent
manta_dir = docbuild_dir.parent
manta_project_root_fir = manta_dir.parent
manta_resources_dir = manta_project_root_fir / "resources"


def get_coala_background_abs_path() -> str:
    return str(manta_resources_dir / "background" / "Coala_background.svg")


def get_manim_logo_abs_path() -> str:
    return str(manta_resources_dir / "logos" / "Manim_icon.svg")


def get_rwth_logo_abs_path() -> str:
    return str(manta_resources_dir / "logos" / "RWTH_Logo.svg")


def get_manta_logo_abs_path() -> str:
    return str(manta_resources_dir / "logos" / "logo.png")


def get_wzl_logo_abs_path() -> str:
    return str(manta_resources_dir / "logos" / "wzl.svg")


if __name__ == '__main__':
    print(get_coala_background_abs_path())
