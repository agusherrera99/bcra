from pathlib import Path

class ProjectPath:
    ROOT_PATH = Path(__file__).resolve().parent.parent
    SRC_PATH = ROOT_PATH / 'src'
    SECRETS_PATH = ROOT_PATH / 'secrets'

    def __init__(self):
       pass

    def get_root(self):
        return self.ROOT_PATH

    def get_src(self):
        return self.SRC_PATH

    def get_secrets(self):
        return self.SECRETS_PATH

project_path = ProjectPath()
