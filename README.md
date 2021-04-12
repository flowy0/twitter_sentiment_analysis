# Sentiment Analysis with Tweets

## Create your python environment

Using Conda
```
conda create -n twitter python=3.9
conda activate twitter
```

Using pyenv
```
pyenv virtualenv 3.9.4 twitter
pyenv activate twitter
python -m pip install --upgrade pip
```

## Install the packages
```
pip install python-twitter
pip install tweepy
pip install python-dotenv

# for the second part - we use pytorch for pre-processing
pip install torch torchtext
```

## Get your twitter developer account setup 
Apply for a twitter developer account https://developer.twitter.com/

Create an application and get your access keys.
See the link below for details
https://python-twitter.readthedocs.io/en/latest/getting_started.html


## Create an .env file to store your access keys
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


#### Our Pipeline

We get a list of tweets using 
- get_tweets.py 

Process the tweets
 - preprocess_tweets.py (WIP)

Prepare our model 
 - model.py (WIP)




### References:
- https://towardsdatascience.com/twitter-sentiment-analysis-in-python-1bafebe0b566
- https://medium.com/@swenushika/extracting-twitter-data-using-tweepy-a066d6e19be

- https://galhever.medium.com/sentiment-analysis-with-pytorch-part-1-data-preprocessing-a51c80cc15fb
