import sys
apikey=0
boardName=0

def get_args():
    if len(sys.argb)<=1 or len(sys.argv)>3:
        return False
    if len(sys.argv)==2:
        apikey=sys.argv[1]
    if len(sys.argv)==3:
        boardName=sys.argv[2]
        return True


def parse_args(appkey,board=None):
    if appkey and type(appkey)==str and len(appkey)==32:
        if board and type(board)!=str:
            return False
        return True
    else:
        return False
