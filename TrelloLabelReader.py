import sys
import difflib
apikey=0
boardName=0
dictionary={"Bugs","Release","Product launch"}

#TrelloLabelReader.py appkey boardName
#BoardName is optional
def get_args():
    if len(sys.argb)<=1 or len(sys.argv)>3:
        return False
    if len(sys.argv)==2:
        apikey=sys.argv[1]
    if len(sys.argv)==3:
        boardName=sys.argv[2]
        return True

#Validates if the given application key is valid
def parse_args(appkey,board=None):
    if appkey and type(appkey)==str and len(appkey)==32:
        if board and type(board)!=str:
            return False
        return True
    else:
        return False
#Compares the label with a set of predetermined, correctly orthographied Labels
#ignores labels that have a %match < 0.22
def comparator(label,cutoff=0.22):
    return difflib.get_close_matches(label,dictionary,cutoff=cutoff)[0]