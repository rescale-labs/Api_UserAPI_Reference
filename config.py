import configparser
from pathlib import Path

config_path = Path(Path.home(), ".config", "rescale")
config_file_name = "apiconfig"
config_file_path = Path(config_path, config_file_name)


def _init_config():
    Path(config_path).mkdir(parents=True, exist_ok=True)

    cfg = configparser.ConfigParser()
    cfg["default"] = {"apibaseurl": "<PROVIDE_VALUE>", "apikey": "<PROVIDE_VALUE>"}

    with open(config_file_path, "w") as configfile:
        cfg.write(configfile)


def get_profile(profile="default"):
    cfg = configparser.ConfigParser()
    if not config_file_path.exists():
        _init_config()
        raise Exception(
            f"{config_file_path} did not exist. Created a template configuration file. Please fill in the blanks."
        )

    cfg.read(config_file_path)
    return cfg[profile]["apibaseurl"], cfg[profile]["apikey"]
