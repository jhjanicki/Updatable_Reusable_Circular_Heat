import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#enter and read file
filename = raw_input('Enter a filename: ')
data = pd.read_csv(filename)

#get useful fields
useful_fields = data[['FILENAME','LEFT_CHANNEL','RIGHT_CHANNEL']];

#get time and date from file string
useful_fields['date'], useful_fields['time'] = useful_fields['FILENAME'].str.split('_', 1).str

# strip .wav from filename
useful_fields['time'] = useful_fields['time'].map(lambda x: x.rstrip('.wav'))

# convert date string to datetime object
useful_fields['date'] = pd.to_datetime(useful_fields['date'])

# reformat time
useful_fields['time'] = useful_fields.time.str[:2]+ ':'+useful_fields.time.str[2:4] +':'+useful_fields.time.str[4:]

# convert time string to datetime object
useful_fields["time"] = pd.to_datetime(useful_fields["time"] , format='%H:%M:%S').dt.time

# create "average" column from "left_channel" and "right_channel"
useful_fields['average'] = useful_fields[['LEFT_CHANNEL', 'RIGHT_CHANNEL']].mean(axis=1)

# drop unwanted columns
useful_fields.drop(['FILENAME','LEFT_CHANNEL', 'RIGHT_CHANNEL'], axis=1, inplace=True)

# prepare output file name
newfilename = filename.split('.')
#outputfilename=newfilename[0]+'_cleaned.csv'
outputfilename=newfilename[0]+'_cleaned.json'

# print outputfilename
#useful_fields.to_csv('./'+outputfilename, sep=',', encoding='utf-8')
useful_fields.to_json('./'+outputfilename, orient='records')

