import math
import sys


def hoursToMinSec(time, milliseconds=False, txt=False):
    hours = math.floor(time)
    minutes = (time - hours) * 60
    seconds = (minutes % 1) * 60

    data = {
        "hours": int(hours),
        "minutes": int(math.floor(minutes)),
        "seconds": int(math.floor(seconds))
    }

    if(txt):
        data["txt"] = str(data["hours"]) + ' hour ' + \
            str(data["minutes"]) + " min " + str(data["seconds"]) + " sec" if(
                hours) else str(data["minutes"]) + " min " + str(data["seconds"]) + " sec"

    if(milliseconds):
        data["milliseconds"] = int(math.floor((seconds % 1) * 1000))
        if(data["milliseconds"]):
            data["txt"] = data["txt"] + " " + \
                str(data["milliseconds"]) + " millisecond"
    return data


def main():
    length = len(sys.argv)
    if length > 1:
        try:
            print(hoursToMinSec(float(sys.argv[1])))
        except:
            print("argument must be a number")
    else:
        print("missing argument")


if __name__ == '__main__':
    main()
