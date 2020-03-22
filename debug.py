import sys

# 自作クラスを追加するために参照先を追加
sys.path.append("..")
# print(sys.path)

# クラス読み込み：from <ファイル名> import <クラス名>
from notification import Notification

notify = Notification()
discord_webhook_url = "Discord の Webhook URL をここに入力"

notify.set_discord(discord_webhook_url, "bot")
notify.send_message("test message")