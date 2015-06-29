import sys
import json

def main():
    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
    	term, score  = line.split("\t")  
  	scores[term] = int(score)
  	
    tweet_file_json = open(sys.argv[2],'r')
    
    for line in tweet_file_json.readlines():
	json_data = json.loads(line)
    	if 'text' in json_data.keys():
		this_tweet_text = json_data["text"].encode('utf-8')
                this_tweet_score = 0         	
		single_words = this_tweet_text.split() 
		for words in single_words: #go through the words again
			if words in scores.keys(): #this time pick the ones which are contained in the sentiment file 
				this_tweet_score = this_tweet_score + scores[words]

		print this_tweet_score
    
    sent_file.close()
    tweet_file_json.close()

if __name__ == '__main__':
    main()
