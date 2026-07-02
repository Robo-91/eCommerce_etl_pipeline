from pathlib import Path
import yaml

def load_config():

    root = Path(__file__).resolve().parents[2]

    config_file = root / "config" / "config.yaml"

    with open(config_file, "r") as file:
        return yaml.safe_load(file)

def load_filepath():

    root = Path(__file__).resolve().parents[2]

    config_file = root / "config" / "config.yaml"

    with open(config_file, "r") as file:
        return config_file
