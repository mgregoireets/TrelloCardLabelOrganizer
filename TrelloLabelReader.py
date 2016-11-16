import json
import sys
import difflib
from trello import TrelloApi

apikey = 0
boardName = 0
username = 0
boardID = 0

cards=list()

dictionary = {"Bugs", "Release", "Product launch"}

fixedCardLabels = {}


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


# Compares the label with a set of predetermined, correctly orthographied Labels
# ignores labels that have a %match < 0.22
def comparator(label, cutoff=0.22):
    return difflib.get_close_matches(label, dictionary, cutoff=cutoff)[0]


# initialise a dictionary that will contain the name and id of the cards which labels correspond to
#  those in the dictionary
def initialise_dictionary():
    for d in dictionary:
        fixedCardLabels[d] = 0


def getCards():
    boardIds=list()
    cards=list()

    boards=get_member_boards()
    for board in boards:
        boardIds.append(board["id"])
    for id in boardIds:
        cards.append(trello.boards.get_card(id))
    print(json.dumps(cards, indent=4, sort_keys=True))
def get_member_boards():
    return trello.members.get_board(username)

def get_board_cards():
    print(json.dumps(trello.boards.get_card(boardID), indent=4, sort_keys=True))


def get_board_id():
    global boardID
    boards=get_member_boards()
    for board in boards:
        if board["name"] == boardName:
            return board["id"]


initialise_dictionary()
get_args()

if parse_args(apikey, username, boardName):
    trello = TrelloApi(apikey)
    if boardName:
        boardID = get_board_id()
    if boardName and boardID:
        get_board_cards()
    else:
        getCards()
