import roblox

# Хочу рассказать друзьям, как сильно я их люблю
with roblox.RobloxSession(username="iLoveBricks", password="password123") as rbx:
    for friendship in rbx.friendships():
        try:
            convo = rbx.chat.start_conversation(friendship.user1)
            convo.send_message("ily! ~ iLoveBricks")
        except roblox.errors.RobloxException:
            print("Couldn't send message to {}".format(friendship.user1))
