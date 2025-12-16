from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# 1. 服務帳號認證
gauth = GoogleAuth()
# 使用 JSON 檔案進行非互動式認證
gauth.settings['client_config_file'] = 'client_secrets.json' 
gauth.settings['oauth_scope'] = ['https://www.googleapis.com/auth/drive']
gauth.settings['save_credentials'] = False # 不儲存憑證
gauth.ServiceAuth()

drive = GoogleDrive(gauth)

# 2. 下載檔案 (使用檔案ID)
file_id = '1CfTrj0xN_lo8wxUzltVP_zst97bYRE5murppyhW3UW4' 
file = drive.CreateFile({'id': file_id})
file.GetContentFile('downloaded_file.txt')
print(f"File {file['title']} downloaded successfully.")
