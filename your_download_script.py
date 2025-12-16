from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

# --- 1. 服務帳號認證 (利用 settings.yaml) ---
# PyDrive2 會自動從當前目錄載入 settings.yaml 中配置的服務帳號路徑。
gauth = GoogleAuth()

# 由於我們在 YAML 中已經設定了 settings.yaml，這裡只需載入並認證。
# 顯式載入設定檔
#gauth.#gauth.LoadSettings('settings.
# 執行服務帳號認證。
# 由於 settings.yaml 已經被自動載入，這裡可以直接認證。
# 執行服務帳號認證。
# 注意：您的服務帳號必須被授權存取這個 Google Drive 檔案。

gauth.ServiceAuth()

drive = GoogleDrive(gauth)

# --- 2. 下載 Colab 筆記本 ---
# 替換成您 Colab 筆記本的檔案 ID
colab_file_id = '11LMuYAmsnUL295ny7V1Tg-Ng5KQurdJ1'  

# 建立檔案物件
file = drive.CreateFile({'id': colab_file_id})
file.FetchMetadata(fields='title') # 獲取檔案名稱

# 設定下載檔案名稱（使用 Drive 上的原始名稱）
download_filename = file['title']
if not download_filename.endswith('.ipynb'):
    download_filename += '.ipynb'
    
# 將 Colab 筆記本內容下載到 Actions 運行環境
file.GetContentFile(download_filename)

print(f"✅ 檔案 '{download_filename}' 已成功下載到 GitHub Actions 工作目錄。")

# --- 3. 執行 Colab 筆記本 (使用 Papermill) ---
import papermill as pm

input_notebook = download_filename
output_notebook = 'executed_' + download_filename

print(f"🚀 開始執行筆記本: {input_notebook}...")

# 執行筆記本，並將結果存入一個新的檔案
try:
    pm.execute_notebook(
        input_notebook,
        output_notebook,
        # 您可以在此處傳遞參數給 Colab 筆記本，例如:
        # parameters={'input_data_path': '/data/input.csv'} 
    )
    print(f"🎉 執行完成！結果儲存於 {output_notebook}")
except Exception as e:
    print(f"❌ 筆記本執行錯誤: {e}")
    # 讓 Actions 失敗
    raise
