import json
import sys
import difflib
from trello import TrelloApi

apikey = 0
boardName = 0
username = 0
boardID = 0

cards = list()

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


# Compares the label with a set of predetermined, correctly orthographied Labels
# ignores labels that have a %match < 0.22
def comparator(label, cutoff=0.2):
    return difflib.get_close_matches(label, dictionary, cutoff=cutoff)[0]


# initialise a dictionary that will contain the name and id of the cards which labels correspond to
#  those in the dictionary
def initialise_dictionary():
    for d in dictionary:
        fixedCardLabels[d] = list()

#adds all cards in the board
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


# show each label of a card
def show_card(name, labels):
    print "Here are the labels for card: " + name
    for l in labels:
        print l["name"]


# extracts teh labels and the cards of the user
def parse_labels():
    for board in cards:
        for card in board:
            labels = card["labels"]
            cardname = card["name"]
            show_card(cardname, labels)

#Shows the label each cards should have
def fix_labels():
    print "Here are how the labels should be fixed for each card: "
    for board in cards:
        for card in board:
            cardname = card["name"]
            for label in card["labels"]:
                fixedCardLabels[comparator(label["name"])].append(cardname)
        for fixedlabel in fixedCardLabels:
            print fixedlabel + ": "
            for fixedcard in fixedCardLabels[fixedlabel]:
                print "    " + fixedcard


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
        fix_labels()
