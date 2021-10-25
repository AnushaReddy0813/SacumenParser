from configparser import ConfigParser


def parse(inputfile):
    try:
        config = ConfigParser()
        config.read(inputfile)
        conf_dict = {section: dict(config.items(section)) for section in config.sections()}
        return conf_dict
    except:
        print("Not a valid conf file")
        return
