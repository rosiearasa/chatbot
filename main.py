from buildbot import *

# create chatbot
bot = create_bot('Onyx')

# train all data
train_all_data(bot)

#create identity
identity = input("State your identity please: ")

#rules for responding to different identities
if identity == "Rosie":
    print("Welcome Rosie, great to have you home")

elif identity =="John":
    print("glad to have you, Rosie is out right now but feel free to ask me anything")

else:
    print("Access Denied")
    exit()

# custom data
bot_owner = [
    "Who is the owner of this bot?",
    "Rosie is the owner of this bot"
]

custom_train(bot, bot_owner)

print("------ Training custom data ------")
# write and train your custom data here IF the identity is Mark
if identity == 'Rosie':
    city_born = [
        "Where was I born?",
        "Mark, you were born in Kenya."
    ]

    fav_book = [
        "What is my favourite book?",
        "That is easy. Your favourite book is The Great Gatsby."
    ]

    fav_movie = [
        "What is my favourite movie?",
        "You have watched Interstellar more times than I can count."
    ]

    fav_sports = [
        "What is my favourite sport?",
        "You have always loved running."
    ]
    # train chatbot with your custom data
    custom_train(bot, city_born)
    custom_train(bot, fav_book)
    custom_train(bot, fav_movie)
    custom_train(bot, fav_sports)



# start chatbot
start_chatbot(bot)
