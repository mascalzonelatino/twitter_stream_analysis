import sys
import json

def main():	

    tweet_file_json = open(sys.argv[1],'r')

    all_words = dict()      

    for line in tweet_file_json.readlines():
	json_data = json.loads(line)
    	if 'text' in json_data.keys():
		this_tweet_text = json_data["text"].encode('utf-8')         	
		single_words = this_tweet_text.split() 	
		
		for words in single_words: 
			if words not in all_words.keys(): 
				all_words[words] = 1								
			else:
				all_words[words] = all_words[words] + 1

    how_many_unique_words = len(all_words.keys())

    for words in all_words.keys(): 
	frequency = float(all_words[words]) / how_many_unique_words
	print words, frequency  
    
    tweet_file_json.close()

if __name__ == '__main__':
    main()
