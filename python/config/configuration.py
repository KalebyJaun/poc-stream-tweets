import configparser
from shutil import copyfile
import os
DEFAULT_SECTION = "DEFAULT"

class GlobalConfiguration():
    config_parser = None
    
    def load_config_parser(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config
    
    def save_config_parser(self):
        copyfile(self.config_file, self.config_file + "_bkp")
        
        with open(self.config_file, 'wb') as configfile:
            self.config_parser.write(configfile)
    
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_parser = self.load_config_parser()
        
    def treat_value(self, treat_value):
        if "|" in treat_value:
            return [x for x in treat_value.split("|")]
        else:
            return treat_value
            
            
    def get_value(self,key, section=None, default_section = False):
        if not default_section:
            return self.treat_value(self.config_parser.get(section,key))
        else:
            return self.treat_value(self.config_parser.get(DEFAULT_SECTION,key))
    
    def set_value(self,key, section, value, default_section = False):
        if not default_section:
            self.config_parser.set(section, key, value)
        else:
            self.config_parser.set(DEFAULT_SECTION, key, value)
        

