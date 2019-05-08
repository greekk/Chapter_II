import configparser
from parsers.config_parser import createConfig
import os

def crudConfig(path):
    """ Create, Update, Delete config"""
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    #read values from config
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")

    print(font, font_size)

    #change value in the config
    config.set("Settings", "font_size", "12")

    font_size = config.get("Settings", "font_size")
    print(font_size)

    #delete value from config
    config.remove_option("Settings", "font_style")

    #write changes back to the config file
    with open(path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    path = "settings.ini"
    crudConfig(path)

