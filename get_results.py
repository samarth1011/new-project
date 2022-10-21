import requests
auth_token = '7bd84746e96045e3ad4a4014d1955973'

headers = {
  "Authorization": auth_token,
  "Content-Type": "application/json"
}


def upload_to_AssemblyAI(audio_file):

    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    upload_endpoint = 'https://api.assemblyai.com/v2/upload'

    upload_response = requests.post(
        upload_endpoint,
        headers=headers, 
        data=audio_file
    )
    print(upload_response)
    audio_url = upload_response.json()['upload_url']

    json = {
        "audio_url": audio_url,
        "iab_categories": True,
        "auto_chapters": True
    }
    
    response = requests.post(
    	transcript_endpoint, 
        json=json, 
        headers=headers)

    polling_endpoint = transcript_endpoint + "/" + response.json()['id']
    return polling_endpoint

def convertMillis(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((start_ms / (1000 * 60)) % 60)
    hours = int((start_ms / (1000 * 60 * 60)) % 24)
    btn_txt = ''
    if hours > 0:
        btn_txt += f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        btn_txt += f'{minutes:02d}:{seconds:02d}'
    return btn_txt
