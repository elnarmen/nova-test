from environs import Env
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

env = Env()
env.read_env()

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def create_file_in_google_drive(title: str, content: str) -> None:
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({"title": title})
    file.SetContentString(content)
    file.Upload()
