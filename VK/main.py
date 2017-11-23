from ClientGetID import ClientGetID
from ClientGetFriendsAges import ClientGetFriendsAges
from Gist import Gist

friends_id_arr = None
while friends_id_arr is None:
    input_username = input()

    friends_id_arr = ClientGetID(input_username).execute()

friends_ages = ClientGetFriendsAges(friends_id_arr).execute()

if len(friends_ages) == 0:
    print('Нет друзей :(')
    input()
else:
    print("ID: ", friends_id_arr)
    print("Ages: ", friends_ages)

    Gist(friends_ages).print_hist()
