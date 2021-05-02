import logging
import utils
import os
import pandas as pd


if __name__ == '__main__':
    OUTPUT_DATA = 'data'
    OUTPUT_TWEETS ='data/csv'
    OUTPUT_FILENAME='raw/all_tweets.csv'
    # get list of files 
    files_path = [os.path.join(r,file) for r,d,f in os.walk(OUTPUT_TWEETS) for file in f]
    print(files_path)

    # create folder for appended data 
    utils.create_dir('data/raw')
    #combine all files in the list
    combined_df = pd.concat([pd.read_csv(f) for f in files_path ])
    print(combined_df.info())
    print(combined_df.head())

    # combine into a new file 
    combined_df.to_csv( f"{OUTPUT_DATA}/{OUTPUT_FILENAME}", index=False)

