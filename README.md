## Introduction

Twitter represents a fundamentally new instrument to make social measurements. Millions of people voluntarily express opinions across any topic imaginable --- this data source is incredibly valuable for both research and business.

For example, researchers have shown that the "mood" of communication on twitter [**reflects biological rhythms**](http://www.nytimes.com/2011/09/30/science/30twitter.html) and can even used to [**predict the stock market**](http://arxiv.org/pdf/1010.3003&embedded=true). A student here at UW used geocoded tweets to [**plot a map of locations where "thunder" was mentioned in the context of a storm system in Summer 2012.**](http://cliffmass.blogspot.com/2012/07/thunderstorm-fest.html)

Researchers from Northeastern University and Harvard University studying the characteristics and dynamics of Twitter [**have an excellent resource**](http://www.ccs.neu.edu/home/amislove/twittermood/) for learning more about how Twitter can be used to analyze moods at national scale.

In this repository you will find Python scripts offering solutions to simple data analysis problems such as:

*   access the Twitter API to obtain a sample of Twitter stream data
*   estimate the public's perception (the _sentiment_) of a particular term or phrase
*   analyze the relationship between location and mood based on a sample of twitter data

#### The Twitter Application Programming Interface

Twitter provides a very rich REST API for querying the system, accessing data, and control your account. You can [read more about the Twitter API](https://dev.twitter.com/docs)

### Get Twitter Data

To access the live stream, you will need to install the [**oauth2 library**](http://pypi.python.org/pypi/oauth2/) so you can properly authenticate.

The steps below will help you set up your twitter account to be able to access the live 1% stream.

1.  Create a twitter account if you do not already have one.
2.  Go to [**https://dev.twitter.com/apps**](https://dev.twitter.com/apps) and log in with your twitter credentials.
3.  Click "Create New App"
4.  Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
5.  On the next page, click the "API Keys" tab along the top, then scroll all the way down until you see the section "Your Access Token"
6.  Click the button "Create My Access Token". You can [**Read more about Oauth authorization.**](https://dev.twitter.com/docs/auth)
7.  You will now copy four values into twitterstream.py. These values are your "API Key", your "API secret", your "Access token" and your "Access token secret". All four should now be visible on the API Keys page. (You may see "API Key" referred to as "Consumer key" in some places in the code or on the web; they are synonyms.) Open twitterstream.py and set the variables corresponding to the api key, api secret, access token, and access secret. You will see code like the below:

    <pre>api_key = "<Enter api key>"
    api_secret = "<Enter api secret>"
    access_token_key = "<Enter your access token key here>"
    access_token_secret = "<Enter your access token secret here>"

    </pre>

8.  Run the following: 

    <pre>$ python twitterstream.py > output.txt</pre>

    This command pipes the output to a file. Stop the program with Ctrl-C when you have obtained enough data (tip: wait at least **3 minutes** for data to accumulate). 

### Derive the sentiment of each tweet

The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.

The script `tweet_sentiment.py` accepts two arguments on the command line: a _sentiment file_ and a tweet file like the one you generated in the above section. You can run it like this:

<pre>$ python tweet_sentiment.py AFINN-111.txt output.txt</pre>

The file AFINN-111.txt contains a list of pre-computed sentiment scores. Each line in the file contains a word or phrase followed by a sentiment score. Each word or phrase that is found in a tweet but not found in AFINN-111.txt should be given a sentiment score of 0\. See the file AFINN-README.txt for more information.

The script provides a score for **every** tweet in the sample file, even if that score is zero. 

### Derive the sentiment of new terms

The script `term_sentiment.py` accepts two arguments on the command line: a _sentiment file_ and a tweet file like the one you generated in the above section and computes the sentiment for the terms that **do not** appear in the file AFINN-111.txt:

<pre>$ python term_sentiment.py AFINN-111.txt output.txt</pre>

The strategy used to compute the sentiment of new terms is rather simple: we calculate the number of positive words and the number of negative words in each tweet. Then we use the ratio between positive words and negative words to assign a sentiment score to any word that is present in a tweet but not in our the dictionary file. 

### Compute Term Frequency

The script `frequency.py` computes the _term frequency histogram_ from the input livestream data file.

The frequency of a term can be calculated as `[# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]`. For example: 

<pre>$ python frequency.py test/output.txt </pre>

### Which State is happiest?

The script `happiest_state.py` returns the name of the happiest state. It accepts two arguments: a sentiment file and a livestream data file. For example:

<pre>$ python happiest_state.py AFINN-111.txt test/output.txt </pre>

There are different ways you might assign a location to a tweet. Here are three:

*   Use the `coordinates` field (a part of the `place` object, if it exists, to geocode the tweet. This method gives the most reliable location information, but unfortunately this field is not always available and you must figure out some way of translating the coordinates into a state.
*   Use the other metadata in the `place` field. Much of this information is hand-entered by the twitter user and may not always be present or reliable, and may not typically contain a state name.
*   Use the `user` field to determine the twitter user's home city and state. This location does not necessarily correspond to the location where the tweet was posted, but it's reasonable to use it as a proxy.

Any tweets for which a location in the United States cannot be assigned is ignored. 

### Top ten hash tags

The script `top_ten.py` computes the ten most frequently occurring hashtags from a livestream data file. To see it in action, run it against the test data provided in this repository: 

<pre>$ python top_ten.py test/output.txt</pre>

