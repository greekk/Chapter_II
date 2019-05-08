import configparser
import os

class MyConfigParser:

    def __init__(self, path):
        self.path = path



    def create_config(self):
        """ Create a config file """
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("Settings", "font", "Courier")
        config.set("Settings", "font_size", "10")
        config.set("Settings", "font_style", "Normal")
        config.set("Settings", "font_info", "You are using %(font)s at %(font_size)s pt")

        with open(self.path, "w") as config_file:
            config.write(config_file)

    def get_config(self):
        """ Returns the config object """
        if not os.path.exists(self.path):
            self.create_config()
        config = configparser.ConfigParser()
        config.read(self.path)
        return config

    def get_setting(self, section,setting):
        """  Print out a setting """

        config = self.get_config()
        value = config.get(section, setting)
        msg = "{section} {setting} is {value}".format(section=section, setting=setting, value=value)
        print(msg)
        return value

    def update_setting(self, section, setting, value):

        """  Update a setting """
        config = self.get_config()
        config.set(section, setting, value)
        with open(path, "w") as config_file:
            config.write(config_file)

    def delete_setting(self, section, setting):

        """ Delete setting """
        config = self.get_config()
        config.remove_option(section, setting)
        with open(path, "w") as config_file:
            config.write(config_file)

if __name__ == "__main__":

    path = "data\settings.ini"
    my_config_parser = MyConfigParser(path)
    #my_config_parser.create_config()
    font = my_config_parser.get_setting('Settings', 'font')
    font_size = my_config_parser.get_setting('Settings', 'font_size')
    my_config_parser.update_setting('Settings', 'font_size', '12')
    my_config_parser.delete_setting('Settings', 'font_style')

