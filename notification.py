import requests
import json

class Notification():
    """
    @brief : 通知クラス
    @note  : 
    """
    line_notify_token = ''
    discord_webhook_url = ''
    discord_username = ''
    slack_webhook_url = ''
    slack_username = ''
    
    def __init__(self):
        print("Notification クラスをインスタンス化")

    # ----- LINE, DISCORD, SLACK にメッセージを送るための初期設定 関連----
    def set_line(self, token):
        self.line_notify_token = token

    def set_discord(self, url, username):
        self.discord_webhook_url = url
        self.discord_username = username
    
    def set_slack(self, url, username):
        self.slack_webhook_url = url
        self.slack_username = username        

    # ----- Notify（メッセージを送る） 関連-----
    def send_message(self, text) :
        try:
            self.__line(text)
        except:
            pass
        try:
            self.__discord(text)
        except:
            pass
        try:
            self.__slack(text)
        except:
            pass
        
    def __line(self, message):
        if len(self.line_notify_token) > 0:
            requests.post('https://notify-api.line.me/api/notify', headers={'Authorization': 'Bearer ' + self.line_notify_token}, data={'message': '\n' + message})
            print(message + " by Line")

    def __discord(self, message):
        if len(self.discord_webhook_url) > 0:
            requests.post(self.discord_webhook_url, data={'username': self.discord_username, 'content': message})
            print(message + " by Discord")

    def __slack(self, message):
        if len(self.slack_webhook_url) > 0:
            requests.post(self.slack_webhook_url, data=json.dumps({'username': self.slack_username, 'text':message}))
            print(message + " by Slack")
