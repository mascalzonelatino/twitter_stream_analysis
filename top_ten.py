import sys
import json
from collections import Counter 

def main():
    tweet_file_json = open(sys.argv[1],'r')

    all_tags = list() # I decide to save all the hashtags found in a list
    
    for line in tweet_file_json.readlines():
	json_data = json.loads(line)
		    	
	if 'entities' in json_data.keys():
		entities = json_data["entities"] #dictionary
		for key in entities.keys():
			if 'hashtags' in key: 
                       		this_tag_list = entities["hashtags"]  				
				if(len(this_tag_list)>0):
					#this is now a list of hashtags 					
					for tags in this_tag_list:
						if 'text' in tags.keys(): #tags have a number of properties, one of which is the 'text' 
							actual_tag_text = tags["text"] 						
							all_tags.append(actual_tag_text) #update my list with the hashtag text I've just found	
		    
    # At this point I have all the tags in my list. Use a counter object to count the 10 most common items :)
    count = Counter(all_tags).most_common(10) 
	
    # Counters return lists, so 'count' is a list of pairs, such as [(a b), (c d), (e f)]  	
    # So I'm printing item 0 and item 1 of each pair contained in the list 
    for items in count:	
	print items[0] + " " + str(float(items[1])) # ! we want floats 
 
    tweet_file_json.close()

if __name__ == '__main__':
    main()
