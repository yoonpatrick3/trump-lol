from textgenrnn import textgenrnn

if input("Do you need to get data? ") == "yes":
    import getdata
    getdata.get_reddit()
    getdata.get_all_tweets()

textFile = "data"
numEpochs = int(input("Enter number of epochs: "))

#Change path to find text file here!
pathToFile = "C:/Users/12244/yoonp/independentCS/trump-league/" + textFile + ".txt"

t = textgenrnn()

t.train_from_file(pathToFile, num_epochs=numEpochs)