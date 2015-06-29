import sys
import json
import operator 

def lines(fp):
    print str(len(fp.readlines()))

states_with_abbreviations = [
{"name":"Alabama","abbr":"AL","score":0}, 
{"name":"Alaska","abbr":"AK","score":0}, 
{"name":"Arizona","abbr":"AZ","score":0},
{"name":"Arkansas","abbr":"AR","score":0},
{"name":"California","abbr":"CA","score":0},
{"name":"Colorado","abbr":"CO","score":0},
{"name":"Connecticut","abbr":"CT","score":0},
{"name":"Delaware","abbr":"DE","score":0},
{"name":"District of Columbia","abbr":"DC","score":0},
{"name":"Florida","abbr":"FL","score":0},
{"name":"Georgia","abbr":"GA","score":0},
{"name":"Hawaii","abbr":"HI","score":0},
{"name":"Idaho","abbr":"ID","score":0},
{"name":"Illinois","abbr":"IL","score":0},
{"name":"Indiana","abbr":"IN","score":0},
{"name":"Illinois","abbr":"IL","score":0},
{"name":"Iowa","abbr":"IA","score":0},
{"name":"Kansas","abbr":"KS","score":0},
{"name":"Kentucky","abbr":"KY","score":0},
{"name":"Louisiana","abbr":"LA","score":0},
{"name":"Maine","abbr":"ME","score":0},
{"name":"Maryland","abbr":"MD","score":0},
{"name":"Massachusetts","abbr":"MA","score":0},
{"name":"Michigan","abbr":"MI","score":0},
{"name":"Minnesota","abbr":"MN","score":0},
{"name":"Mississippi","abbr":"MS","score":0},
{"name":"Missouri","abbr":"MO","score":0},
{"name":"Montana","abbr":"MT","score":0},
{"name":"Nebraska","abbr":"NE","score":0},
{"name":"Nevada","abbr":"NV","score":0},
{"name":"New Hampshire","abbr":"NH","score":0},
{"name":"Nevada","abbr":"NV","score":0},
{"name":"New Jersey","abbr":"NJ","score":0},
{"name":"New Mexico","abbr":"NM","score":0},
{"name":"New York","abbr":"NY","score":0},
{"name":"North Carolina","abbr":"NC","score":0},
{"name":"North Dakota","abbr":"ND","score":0},
{"name":"Ohio","abbr":"OH","score":0},
{"name":"Oklahoma","abbr":"OK","score":0},
{"name":"Oregon","abbr":"OR","score":0},
{"name":"Pennsylvania","abbr":"PA","score":0},
{"name":"Rhode Island","abbr":"RI","score":0},
{"name":"South Carolina","abbr":"SC","score":0},
{"name":"South Dakota","abbr":"SD","score":0},
{"name":"Tennessee","abbr":"TN","score":0},
{"name":"Texas","abbr":"TX","score":0},
{"name":"Utah","abbr":"UT","score":0},
{"name":"Vermont","abbr":"VT","score":0},
{"name":"Virginia","abbr":"VA","score":0},
{"name":"Washington","abbr":"WA","score":0},
{"name":"West Virginia","abbr":"WV","score":0},
{"name":"Virginia","abbr":"VA","score":0},
{"name":"Wisconsin","abbr":"WI","score":0},
{"name":"Wyoming","abbr":"WY","score":0}
]

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
		for words in single_words: 			
			if words in scores.keys():
				this_tweet_score = this_tweet_score + scores[words]		
				#save the score of this tweet to the dictionary; the key is the state 
				this_tweet_location = json_data["user"] 			
				if 'location' in this_tweet_location.keys():					
					if 'US' in str(this_tweet_location["time_zone"]):
						user_location = this_tweet_location["location"]					
						#is this user_location in the dictionary of states?
						for items in states_with_abbreviations:
							user_location.encode('utf-8').lower()							
							if user_location in items["name"].encode('utf-8').lower() or user_location in items["abbr"]:
								items["score"] = items["score"]+this_tweet_score
	
    happiest_state = states_with_abbreviations[0]["abbr"]
    max_score = states_with_abbreviations[0]["score"]
    for list_item in states_with_abbreviations:
	if list_item["score"] > max_score:
		happiest_state = list_item["abbr"]
 
    print happiest_state

    sent_file.close()
    tweet_file_json.close()

if __name__ == '__main__':
    main()
