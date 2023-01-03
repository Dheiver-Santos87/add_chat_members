# add_chat_members

This code snippet is using the Python telegram library to add members from one group to another group in the Telegram messaging service.

The code configures a telegram.Bot object with a given token, which is used to authenticate the bot and grant it access to the Telegram API. The bot can then use the get_chat_members method to retrieve a list of members in the group specified by the chat_id parameter, which in this case is @grupo_origem. The for loop iterates over this list of members, and for each member, it tries to add them to the new group specified by @novo_grupo using the add_chat_members method. If an error occurs, it is caught and printed to the console.
