from pyrogram import Client

# Log in here to get your personal API ID and API hash:
# https://my.telegram.org/auth?to=apps
api_id = *********
api_hash = "****************************"
group_url = "ByteBustersCoders"    # Enter the URL address of the group you want to analyze.
users = 'BuildBo smailjk neithermeow Polygonri'  # enter usernames (1 or more) SEPARATED BY a SPACE
num_of_fav_words = 7
limit_of_messages = 9000  # affects the execution time and accuracy of the result
ignore_length = 7    # ignore words shorter than...


def parse_user(app, user):
    messages = app.search_messages(group_url, from_user=user, limit=limit_of_messages)
    words_counter = {}
    for message in messages:
        message_text = message.text
        if message_text is None:
            continue
        words = message_text.lower().split()
        for word in words:
            if len(word) < ignore_length or not word.isalpha():
                continue
            words_counter[word] = words_counter.get(word, 0) + 1

    sorted_dict = {}
    for word, n in sorted(words_counter.items(), key=lambda tu: tu[1], reverse=True)[:num_of_fav_words]:
        sorted_dict[word] = n

    print(f"{user}'s favourite words:")
    [print(f'    {word}: {n}') for word, n in sorted_dict.items()]
    print()


application = Client("my_session", api_id=api_id, api_hash=api_hash)
with application as app:
    users = users.split()
    for user in users:
        parse_user(app, user)
