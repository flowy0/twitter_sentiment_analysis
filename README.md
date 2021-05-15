# Sentiment Analysis with Tweets


## Objective:
 - Extract Tweets
 - Create a simple sentiment analysis model


## Create your python environment

Using Conda
```
conda create -n twitter python=3.9
conda activate twitter
pip install -r requirements.txt
```

## Install the packages
```
# pip install -r requirements.txt
or 
pip install python-twitter
pip install tweepy
pip install python-dotenv

# twint is an alternative to tweepy (doesnt require twitter api)
pip install twint
# fixes an issue in https://github.com/twintproject/twint/issues/384
pip  install --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint  

pip install spacy
python -m spacy download en_core_web_sm  
# load the package like this 
# spacy.load('en_core_web_sm')

pip install spacytextblob
# for the second part - we use pytorch for pre-processing
pip install torch torchtext
```

## Get your twitter developer account setup 
Apply for a twitter developer account https://developer.twitter.com/

Create an application and get your access keys.
See the link below for details
https://python-twitter.readthedocs.io/en/latest/getting_started.html


### Create an .env file to store your access keys
```
API_KEY= 
API_KEY_SECRET= 
ACCESS_TOKEN= 
ACCESS_SECRET= 
```

### Run the test scripts as follows:

#### Test your twitter credentials by running the script
```
python test_twitter-python-lib.py
```
You should see something like this.
```
INFO:__main__:<twitter.api.Api object at 0x1094a7ee0>
```

#### Run the test script to extract some tweets 
```
python test_tweepy.py
```


#### Modules

We get a list of tweets and export to csv 
We store the csv files, so that we dont need to keep hitting the twitter API
- get_tweets.py 

Combine the tweets 
 - combine_tweets.py

Process the tweets
 - preprocess_tweets.py (WIP)

Prepare our model 
 - model.py (WIP)

#### To-do:
- Data Preprocessing
- Model Prep
- Incorporate python modules into a data pipeline
- Deployment
- Allow variables thru config files

##### References:
- https://towardsdatascience.com/twitter-sentiment-analysis-in-python-1bafebe0b566
- https://medium.com/@swenushika/extracting-twitter-data-using-tweepy-a066d6e19be

- https://galhever.medium.com/sentiment-analysis-with-pytorch-part-1-data-preprocessing-a51c80cc15fb
- https://realpython.com/sentiment-analysis-python/
- https://www.dataquest.io/blog/tutorial-text-classification-in-python-using-spacy/