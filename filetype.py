import sys
if len(sys.argv)<2:print("Invalid")
else:
    filename=sys.argv[1].lower()
    if filename.endswith(".txt"):
        print("It is a txt file")
    elif filename.endswith(".c"):
        print("It is a C file")
    elif filename.endswith(".json"):
        print("It is a JSON file")
    else:print("Unknown file type")
