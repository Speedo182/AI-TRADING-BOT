import requests
import json
import datetime
import smtplib

# Telegram API endpoint to get group members
GROUP_MEMBERS_ENDPOINT = "https://api.telegram.org/bot{token}/getChatMembersCount?chat_id={chat_id}"

# Telegram API endpoint to get user data
USER_DATA_ENDPOINT = "https://api.telegram.org/bot{token}/getChatMember?chat_id={chat_id}&user_id={user_id}"

# Telegram bot token and group chat id
TELEGRAM_TOKEN = "your_bot_token"
TELEGRAM_GROUP_CHAT_ID = "your_group_chat_id"

# Email server settings
EMAIL_SERVER = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "your_email_username"
EMAIL_PASSWORD = "your_email_password"
EMAIL_FROM = "your_email_address"
EMAIL_TO = "recipient_email_address"

# Time threshold for inactive members (in days)
INACTIVE_TIME_THRESHOLD = 14

def get_group_members():
    """
    Get all members of the Telegram group
    """
    url = GROUP_MEMBERS_ENDPOINT.format(token=TELEGRAM_TOKEN, chat_id=TELEGRAM_GROUP_CHAT_ID)
    response = requests.get(url)
    members_count = response.json()["result"]
    return members_count

def get_user_data(user_id):
    """
    Get user data for a specific Telegram user
    """
    url = USER_DATA_ENDPOINT.format(token=TELEGRAM_TOKEN, chat_id=TELEGRAM_GROUP_CHAT_ID, user_id=user_id)
    response = requests.get(url)
    user_data = response.json()["result"]
    return user_data

def get_inactive_members():
    """
    Get inactive members of the Telegram group
    """
    inactive_members = []
    members_count = get_group_members()
    for i in range(members_count):
        user_data = get_user_data(i)
        last_activity = user_data["status"]
        if last_activity == "left" or last_activity == "kicked":
            continue
        joined_date = datetime.datetime.fromtimestamp(user_data["joined_date"])
        current_date = datetime.datetime.now()
        days_since_joined = (current_date - joined_date).days
        if days_since_joined > INACTIVE_TIME_THRESHOLD:
            inactive_members.append(user_data["user"]["first_name"])
    return inactive_members

def send_email(inactive_members):
    """
    Send an email with the list of inactive members
    """
    message = "Inactive members: \n"
for member in inactive_members:
message += f"{member}\n"
# send email to specified address
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, email_password)
server.sendmail(email_address, recipient_email, message)
server.quit()

# create a schedule to run the function every 14 days
schedule.every(14).days.do(clean_telegram_group)
while True:
schedule.run_pending()
time.sleep(1)
