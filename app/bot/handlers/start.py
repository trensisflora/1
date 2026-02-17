# Start Command Handler

def start_command_handler(update, context):
    update.message.reply_text("Welcome! Use /help to see available commands.")

# Help Command Handler

def help_command_handler(update, context):
    help_text = "Here are the available commands:\n/start - Start the bot\n/help - Get help with using the bot"
    update.message.reply_text(help_text)