import json
import sys
import difflib
from trello import TrelloApi

apikey = 0
boardName = 0
username = 0
boardID = 0

cards = list()
labels = []
dictionary = {"Bugs", "Release", "Product launch"}

fixedCardLabels = dict()


# TrelloLabelReader.py appkey boardName
# BoardName is optional
def get_args():
    global apikey, boardName, username
    if len(sys.argv) <= 2 or len(sys.argv) > 4:
        return False
    if len(sys.argv) >= 3:
        apikey = sys.argv[1]
        username = sys.argv[2]
    if len(sys.argv) == 4:
        boardName = sys.argv[3]
        return True


# Validates if the given application key is valid
def parse_args(appkey, username, board=None):
    if appkey and type(appkey) == str and len(appkey) == 32 and username and type(username) == str:
        if board and type(board) != str:
            return False
        return True
    else:
        return False


# initialise a dictionary that will contain the name and id of the cards which labels correspond to
#  those in the dictionary
def initialise_dictionary():
    for d in dictionary:
        fixedCardLabels[d] = list()


# adds all cards in the board
def get_board_cards(id):
    cards.append(trello.boards.get_card(id))


# gets the card of the users specified board or of all his public boards
def getCards():
    boardIds = list()

    boards = get_member_boards()
    for board in boards:
        boardIds.append(board["id"])
    for id in boardIds:
        get_board_cards(id)


# gets all the public boards of the user
def get_member_boards():
    return trello.members.get_board(username)


# gets the id of the users boards
def get_board_id():
    global boardID
    boards = get_member_boards()
    for board in boards:
        if board["name"] == boardName:
            return board["id"]


# extracts the labels and the cards of the user
def parse_labels():
    for board in cards:
        for card in board:
            for cardLabels in card["labels"]:
                labels.append(cardLabels["name"])


# Produces a list of all duplicates, the list is separated in lists of each kind of duplicate
# Function requires a list of tags to check for duplicates
def process_duplicates(list):
    duplicates_list = []
    duplicates = []
    while len(list) > 0:
        duplicates_list = difflib.get_close_matches(list[0], list, cutoff=0.25)
        if len(duplicates_list) > 1:
            duplicates.append(duplicates_list)
        else:
            for dup in duplicates:
                if difflib.get_close_matches(list[0], dup, cutoff=0.5):
                    dup.append(list[0])
        list = [d for d in list if d not in duplicates_list]
    return duplicates


# shows the duplicates in the labels of the user to him
def show_duplicates(duplicates):
    print "Here are the possible duplicates for your cards: "
    for dup in duplicates:
        print "-" + ", ".join(dup)


initialise_dictionary()
get_args()

if parse_args(apikey, username, boardName):
    trello = TrelloApi(apikey)
    if boardName and boardID:
        boardID = get_board_id()
        get_board_cards()
    else:
        getCards()
    if len(cards) > 0:
        parse_labels()
        duplicates = process_duplicates(labels)
        show_duplicates(duplicates)
