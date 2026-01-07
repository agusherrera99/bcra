from pathlib import Path

class ProjectPaths:
    ROOT_PATH = Path(__file__).resolve().parent.parent
    SRC_PATH = ROOT_PATH / 'src'
    SECRETS_PATH = ROOT_PATH / 'secrets'
    CREDENTIALS_FILE = SECRETS_PATH / 'credentials.json'
    TOKEN_FILE = SECRETS_PATH / 'token.json'

    def __init__(self):
       pass

    def get_root(self):
        return self.ROOT_PATH

    def get_src(self):
        return self.SRC_PATH

    def get_secrets(self):
        return self.SECRETS_PATH

    def get_credentials(self):
        return self.CREDENTIALS_FILE

    def get_token(self):
        return self.TOKEN_FILE

project_paths = ProjectPaths()
