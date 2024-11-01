import itchat

itchat.auto_login()

friends_list = itchat.get_friends(update=True)
print(len(friends_list))


lucky_friends = random.sample(friends_list[1:], 5) 
props = ['NickName', 'Signature', 'City']
for friend in lucky_friends:
    for prop in props:
        print(friend[prop] or '没有此项信息')    
    print('-' * 80)
