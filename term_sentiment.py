import sys
import json

def main():
    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
    	term, score  = line.split("\t")  
  	scores[term] = int(score)
  	
    tweet_file_json = open(sys.argv[2],'r')
    
    results = {} # empty dictionary to host the solution, i.e. the terms and their sentiment score 

    for line in tweet_file_json.readlines():
	json_data = json.loads(line)
    	if 'text' in json_data.keys():
		this_tweet_text = json_data["text"].encode('utf-8')
                this_tweet_score = 0         	
		single_words = this_tweet_text.split() 
		no_of_positive = 0
		no_of_negative = 0		
		for words in single_words: 			
			#so far the logic has been the same as Problem 2. Here's where it starts being problem 3-specific:
			#Instead of calculating the score of a tweet, I want to calculate the number of positive words vs 
                        #the number of negative words in the tweet. Then I'll use the ratio between these two to decide 
                        #on the sentiment score of any word that is present in this tweet but not in AFINN-111.			
			if words in scores.keys():
				if scores[words] > 0 :
					no_of_positive = no_of_positive + 1
				elif scores[words] < 0 :
					no_of_negative = no_of_negative + 1
		
		for words in single_words: #go through the words again
			if words not in scores.keys(): #this time pick the ones which are contained in the sentiment file 
				if(no_of_negative==0): 
					no_of_negative = 1 # we don't want to divide by zero! 				
				term_score = float (no_of_positive) / float(no_of_negative) #calculate the score of this term 
				
    				if words in results.keys(): #if this term is already in 'results', update its score 
					results[words] = results[words] + term_score
				else: #else, simply add it to the dictionary 
					results[words] = term_score 

    #at this point the dictionary should contain all the new terms with a sentiment score associated with them 
    for key in results.keys():
	print key,results[key]
    
    sent_file.close()
    tweet_file_json.close()

if __name__ == '__main__':
    main()
