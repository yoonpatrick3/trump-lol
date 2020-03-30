import praw
import os
import init

#Path to where text files save, change on own device
save_path = "C:/Users/12244/yoonp/independentCS/trump-league"

screen_name = 'realdonaldtrump'
subreddits = ["leagueoflegends", "LeagueOfMemes", "summonerschool"]

# creates a new file
with open(os.path.join(save_path,'data.txt'), 'w+', encoding='utf-8') as file:
    pass
	
def get_reddit():

    print("Getting reddit comments...")
        
    reddit = init.reddit
    numComments = 0

    cm = input("Num comments limit (or no limit say none): ")

    for sb in subreddits:
        subreddit = reddit.subreddit(sb)

        comments = []

        banned = "*I am a bot, and this action was performed automatically"

        for comment in subreddit.comments(limit=None):
            if banned.lower() not in str(comment.body).lower():
                comments.append(str(comment.body)) 

        if cm == "none" or len(comments) < int(cm):
            limit = len(comments)
        else:
            limit = int(cm)

        with open(os.path.join(save_path,'data.txt'), 'a+', encoding='utf-8') as file:
            for i in range(limit):
                numComments += 1
                file.write(comments[i] + "\n")

    print("Got " + str(numComments) +" reddit comments.")

def get_all_tweets():

    alltweets = []	
    api = init.api

    dec = input("Tweet limit number? (say none if none) ")
    print("Getting tweets...")
    if dec == "none":        
        #make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            print("getting tweets before %s" % (oldest))
            
            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
            #save most recent tweets
            alltweets.extend(new_tweets)
            
            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1
            
            print("...%s tweets downloaded so far" % (len(alltweets)))
    else:
        count = int(dec)
        if count <= 200:
            alltweets.extend(api.user_timeline(screen_name = screen_name,count=count))
        else:
            #make initial request for most recent tweets (200 is the maximum allowed count)
            new_tweets = api.user_timeline(screen_name = screen_name,count=200)
            
            #save most recent tweets
            alltweets.extend(new_tweets)
            
            #save the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1

            #keep grabbing tweets until there are no tweets left to grab
            while len(new_tweets) > 0 and count > 0:
                print("getting tweets before %s" % (oldest))
                
                #all subsiquent requests use the max_id param to prevent duplicates
                new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
            
                #save most recent tweets
                alltweets.extend(new_tweets)
                
                #update the id of the oldest tweet less one
                oldest = alltweets[-1].id - 1
                
                print("...%s tweets downloaded so far" % (len(alltweets)))
                count -= 1

    with open(os.path.join(save_path,'data.txt'), 'a+', encoding='utf-8') as file:
        for tweet in alltweets:
            file.write(str(tweet.text.encode("utf-8")) + "\n")
    print("Got " + str(len(alltweets)) + " tweets")

#get_reddit()
#get_all_tweets()