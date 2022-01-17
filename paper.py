import argparse
import pyperclip, sys, os

"""
if len(sys.argv)>1:
    if os.path.exists(sys.argv[1]):
        reader= open(sys.argv[1], "r").read()
        pyperclip.copy(reader)
    else:
        print("Check than path exist")
else:
    print("Use 'paper path' to copy file to clipboard")
"""
parser = argparse.ArgumentParser(description='Process some integers.')
"""parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
"""
parser.add_argument("-cf", nargs=1, type=str, help="Copy the content of a file")
parser.add_argument("-wf", nargs=1, type=str, help="Write file content using copied text")
parser.add_argument("-ci", action="store_true", help="Copy the pipeline")
parser.add_argument("-wo", action="store_true", help="Write on pipeline the copy content")


args= parser.parse_args()

if args.cf:
    if os.path.exists(args.cf[0]):
        reader= open(args.cf[0], "r").read()
        pyperclip.copy(reader)
    else:
        print("Check than path exist")
if args.wf:
    try:
        open(args.wf[0], "w").write(pyperclip.paste())
    except:
        print("Ops you can't write that file")
if args.wo:
    print(pyperclip.paste(), end="")
if args.ci:
    pipeline= ""
    for line in sys.stdin:
        pipeline+= line
    pyperclip.copy(pipeline)
