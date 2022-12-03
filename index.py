import datetime
import googleapiclient.discovery
import google.auth
# ①Google APIの準備をする


SCOPES = ['https://www.googleapis.com/auth/calendar']
calendar_id = 'YourcalendarId'
# Googleの認証情報をファイルから読み込む
gapi_creds = google.auth.load_credentials_from_file('token.json', SCOPES)[0]
# APIと対話するためのResourceオブジェクトを構築する
service = googleapiclient.discovery.build('calendar', 'v3', credentials=gapi_creds)
# ②予定を書き込む
# 書き込む予定情報を用意する
year = 2022
manth = 1
day=[1]
starttime = 12
endtime =20


for i in day:
    body = {
        # 予定のタイトル
        'summary': summary,
        # 予定の開始時刻
        'start': {
            'dateTime': datetime.datetime(year, 12, i, starttime, 0).isoformat(),
            'timeZone': 'Japan'
        },
        # 予定の終了時刻
        'end': {
            'dateTime': datetime.datetime(year, 12, i, endtime, 0).isoformat(),
            'timeZone': 'Japan'
        },
    }
    # # 用意した予定を登録する
    event = service.events().insert(calendarId=calendar_id, body=body).execute()
