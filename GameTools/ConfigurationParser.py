from GameTools.ConfigurationRepo import MasterParameter
import configparser
import ConfigFiles

def parse_master_config_file(master_config_file_location):
    parser = configparser.ConfigParser()
    parser.read("../ConfigFiles/Master.ini")
    MasterParameter.CellCount = int(parser["Board"]["cells"])
    MasterParameter.CircuitType = str(parser["Board"]["circuit"])
    MasterParameter.branching = bool(parser["Board"]["branching"])
