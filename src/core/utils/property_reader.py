import yaml


class PropertyReader:
    #TODO: Use relative path
    def __init__(self, config_path="C:\\Users\\Admin\\Documents\\GIT\\api-testing\\pivotal-api\\config.yml"):
        self.config = yaml.safe_load(open(config_path))

    def get_base_url(self):
        return self.config["app"]["base_url"]

    def get_token(self):
        return self.config["app"]["token"]

    def get_logger_path(self):
        return self.config["app"]["logger_path"]
