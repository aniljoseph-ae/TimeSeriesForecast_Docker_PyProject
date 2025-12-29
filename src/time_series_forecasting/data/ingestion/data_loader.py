import pandas as pd
from pathlib import Path

def _load_csv(file_path: Path):
    return pd.read_csv(file_path)

def _load_parquet(file_path: Path):
    return pd.read_parquet(file_path)

FILE_LOAD_REGISTRY = {
    '.csv': _load_csv,
    '.parquet': _load_parquet,
}

def load_data(file_path: Path):
    # 1. Convert to Path object in case a string was passed
    file_path = Path(file_path)
    
    # 2. Check existence
    if not file_path.exists():
        raise FileNotFoundError(f"File does not exist at: {file_path.absolute()}")
    
    # 3. Get suffix and normalize
    ext = file_path.suffix.lower()
    file_loader = FILE_LOAD_REGISTRY.get(ext)
    
    if file_loader:
        try:
            return file_loader(file_path)
        except Exception as e:
            raise RuntimeError(f"Error loading file with {ext} loader: {e}")
    else:
        raise ValueError(f"Extension '{ext}' not found in registry. Supported: {list(FILE_LOAD_REGISTRY.keys())}")