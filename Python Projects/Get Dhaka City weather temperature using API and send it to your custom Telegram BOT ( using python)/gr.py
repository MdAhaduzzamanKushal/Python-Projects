import requests 
 
# Replace 'YOUR_BOT_TOKEN' with your bot token 
TOKEN = "6634234781:AAHmTAN2FENy-YF5lQoIFsG-_GR_3qfARjU" 
 
# Fetch updates to get the chat ID of the group 
updates_url = f"https://api.telegram.org/bot{TOKEN}/getUpdates" 
updates_response = requests.get(updates_url).json() 
 
if updates_response['ok']: 
    chat_id = updates_response['result'][0]['message']['chat']['id'] 
    print("Chat ID:", chat_id) 
else: 
    print("Error fetching updates:", updates_response['description'])