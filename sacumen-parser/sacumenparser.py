import utils
import yamlparser
import cfgparser
import output


def parse(inputfile, outputtype=""):
    if not inputfile:
        print('Provide Valid Input File')
        return
    dict = {}
    if ".yaml" in inputfile:
        dict = yamlparser.parse(inputfile)
    elif ".cfg" in inputfile:
        dict = cfgparser.parse(inputfile)
    else:
        print("Got Unsupported File Format.. Only Yaml/cfg/conf are supported ")
        return

    flat_dict = utils.convert_flatten(dict)
    if outputtype:
        output.write(flat_dict, outputtype)
    print(flat_dict)
    return flat_dict
