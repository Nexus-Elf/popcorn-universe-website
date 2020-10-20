def main():
    firstName = input("What is your name? ")
    print("Oh, Hello "  + firstName +  "," + "How are you? ")
    hru = input("I am doing ")
    print("Noice to hear you are " + hru + ", What is your Favorite Game? ")
    favoriteGame = input("My Favorite Game Is " )
    print("Oh I heard " + favoriteGame + " was a good game! ")
    print("what should we talk about now? hmmmmm.... ")
    print("Gaming, School, or Sports? ")
    topic1 = input("Let's Talk About " )
    if topic1 == 'Gaming':
        print("Ok, Let's Talk about Gaming.")
    elif topic1 == 'gaming':
        print("Ok, Let's Talk about Gaming.")
    elif topic1 == 'School':
        print("Ok, Let's Talk about school.")
    elif topic1 == 'school':
        print("Ok, Let's Talk about school.")
    elif topic1 == 'Sports':
        print("Ok, Let's Talk about sports.")
    elif topic1 == 'sports':
        print("Ok, Let's Talk about sports.")
    else: 
        print("Please choose one of the listed three, Thanks.")
    print("What is your favorite Esports Team?")
    favoriteTeam = input("My Favorite Esports team is ")
    print("Oh, That's Cool.  " + favoriteTeam + " Used to be my favorite Gaming Team also")
    print("What are your top 5 games?")
    topFiveList = []
    print("My top 5 Games are... ")
    gameOne = input("My First Favorite Game is:")
    gameTwo = input("My Second Favorite Game is:")
    gameThree = input("My Third Favorite Game is:")
    gameFour = input("My Fourth Favorite Game is:")
    gameFive = input("My Fifth Favorite Game is:")
    topFiveList.append(gameOne)
    topFiveList.append(gameTwo)
    topFiveList.append(gameThree)
    topFiveList.append(gameFour)
    topFiveList.append(gameFive)
    print("Are these Correct?")
    print(topFiveList)
    answer = input()
    if answer == 'yes':
        print("That is a nice list you have there! (:")
    elif answer == 'no':
        print("Oop")
    elif answer == 'Yes':
        print("That is a nice list you have there! (:")
    elif answer == 'No':
        print("Oop")
    else:
        print("Don't Answer then :3")

if __name__ == "__main__":
    main()
