import sys

# 自作クラスを追加するために参照先を追加
sys.path.append("..")
# print(sys.path)

# クラス読み込み：from <ファイル名> import <クラス名>
from notification import Notification

notify = Notification()
line_token          = "LINE の トークン をここに入力"
discord_webhook_url = "Discord の Webhook URL をここに入力"
slack_webhook_url   = "Slack の Webhook URL をここに入力"

notify.set_line(line_token)
notify.set_discord(discord_webhook_url, "bot")
notify.set_slack(slack_webhook_url, "bot")

notify.send_message("test message")

