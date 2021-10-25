import yaml


def parse(inputfile):
    with open(inputfile, "r") as stream:
        try:
            dict = yaml.safe_load(stream)
            return dict
        except yaml.YAMLError as exc:
            print(exc)
