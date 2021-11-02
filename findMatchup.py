import slippi
from slippi import Game

class ReplaySorter:

    def __init__():

        this.args = sys.argv[1:]
        this.baseDir = "."
        this.tag = "DAB#823"
        this.myChar = ""
        this.vsChar = ""

        try i = args.index("-d"):
            baseDir = args[i+1]
        except ValueError:
            baseDir = "."

        try i = args.index("m"):
            myChar = args[i+1]
            vsChar = args[i+2]
        except ValueError:
            myChar = args[0]
            vsChar = args[1]
