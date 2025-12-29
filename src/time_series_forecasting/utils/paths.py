from pathlib import Path


def project_root() -> Path:
    """
    Return the project root directory.

    Works reliably because this file is part of an installed package.
    """
    return Path(__file__).resolve().parents[3]


def data_dir() -> Path:
    return project_root() / "data"


def raw_data_dir() -> Path:
    return data_dir() / "01_raw_data"


def processed_data_dir() -> Path:
    return data_dir() / "02_processed_data"

def feature_engineering_data_dir() -> Path:
    return data_dir() / "03_feature_engineering_data"

def config_dir() -> Path:
    return project_root() / "config"

def final_path() -> Path:
    return data_dir() / "final_data"
