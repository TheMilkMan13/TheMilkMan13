def where():
    initial = input("Is Lyric in the living room? Enter y for yes or n for no:")
    if initial == "y":
        print("Ok, she's fine.")
        where()
    else:
        answer = input("Does she answer when called? Enter y for yes or n for no:")
        if answer == "y":
            print("Ok, she's fine.")
            where()
        else:
            find_her = input("Which room is she in? Enter bathroom, her room, or bedroom:")
            if find_her == "bathroom":
                print("Get her out of there, the toilet is deep and full of mystery!")
                where()
            elif find_her == "her room":
                print("Ok, she's just bouncing in her chair as usual.")
                where()
            elif find_her == "bedroom":
                print("Oh look, she's in the dog cage again.")
                where()
where()    