from lincolnbot import LincolnBot

if __name__=="__main__":
    files = ['speeches/'+filename for filename in ['first_inaugural.txt', 'gettysburg.txt', 'lyceum_address.txt', 'meditation_on_the_divine_will.txt', 'second_inaugural.txt']]

    # initialize our bot with a Markov chain of order 3
    abe = LincolnBot(files, 3)

    speech = ""

    # write 5 sentences
    for x in range(5):
        speech += abe.write_sentence().capitalize() + " "

    print speech