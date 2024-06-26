import pandas as pd
import logging
import time
from sqlalchemy import create_engine  


df = pd.read_csv("./datasource/spotify_top_songs_audio_features.csv")

engine = create_engine('mysql://root:henshin@10.108.2.9/mysql')


logging.basicConfig(filename='./docs/song_recommended_api.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Loading output data to mysql table')
start_time = time.time()
try:
    df.to_sql('spotify_top_songs', con=engine, if_exists='replace', index=False)
    logging.info('Data successfully written to MySQL table')
    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f'Data from DataFrame written to MySQL table. {len(df)} rows processed. Time taken: {elapsed_time:.2f} seconds')

except Exception as e:
    logging.error(f'Step 1: Error writing data to MySQL table - {str(e)}')
    end_time = time.time()
