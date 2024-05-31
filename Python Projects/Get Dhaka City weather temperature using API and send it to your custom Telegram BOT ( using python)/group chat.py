import requests

# Replace 'YOUR_BOT_TOKEN' with your bot token
TOKEN = "6634234781:AAHmTAN2FENy-YF5lQoIFsG-_GR_3qfARjU"

# Step 1: Delete the webhook if it exists
delete_webhook_url = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"
delete_webhook_response = requests.get(delete_webhook_url).json()

if delete_webhook_response['ok']:
    print("Webhook deleted successfully.")
    
    # Step 2: Fetch updates to get the chat ID of the group
    updates_url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    updates_response = requests.get(updates_url).json()

    if updates_response['ok']:
        if updates_response['result']:
            # Step 3: Extract chat ID from the updates
            for update in updates_response['result']:
                if 'message' in update:
                    chat = update['message']['chat']
                    chat_id = chat['id']
                    chat_type = chat['type']
                    chat_title = chat.get('title', 'N/A')
                    
                    # Check if the chat is the specified group
                    if chat_type in ['group', 'supergroup'] and chat_title == "Brothers":
                        print(f"Group Name: {chat_title}, Group Chat ID: {chat_id}")
                        break
            else:
                print("No messages found from the specified group.")
        else:
            print("No updates found.")
    else:
        print("Error fetching updates:", updates_response['description'])
else:
    print("Error deleting webhook:", delete_webhook_response['description'])