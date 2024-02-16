import os
import zipfile
import http.client
from datetime import datetime

def send_msg_tg(msg):
    conn = http.client.HTTPSConnection("api.telegram.org")
    api = ""
    chat_id = "275702269"
    conn.request("GET", f"/bot{api}/sendMessage?chat_id={chat_id}&text={msg}")
    response = conn.getresponse()
    result = response.read()
    print(result.decode("utf-8"))

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%d_%m_%Y")

zip_file_name = f"{formatted_datetime}.zip"
zip_dir = "./backup"
zipfile_path = os.path.join(zip_dir, zip_file_name)

source_file_name = "file.1CD"
source_dir = "./db"
sourcefile_path = os.path.join(source_dir, source_file_name)



try:
    with zipfile.ZipFile(zipfile_path, "a", zipfile.ZIP_DEFLATED) as zip_object:
        zip_object.write(sourcefile_path,source_file_name)
    send_msg_tg("ok")
except:
    send_msg_tg("wrong")



