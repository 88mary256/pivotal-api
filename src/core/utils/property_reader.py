import yaml


class PropertyReader:
    def __init__(self, config_path="config.yml"):
        self.config = yaml.safe_load(open(config_path))

    def get_base_url(self):
        return self.config["app"]["base_url"]

    def get_token(self):
        return self.config["app"]["token"]

    def get_logger_path(self):
        return self.config["app"]["logger_path"]

    def get_logger_format(self):
        return self.config["app"]["logger_format"]

    def get_content_tyoe(self):
        return self.config["app"]["content_type"]
