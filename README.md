# Mood based music recommendation
Amateur thing I did for a college project. I got 10/10 marks though so not complaining

Extract the contents of csv_files.zip into flaskApp/csv_files


Works like:\
Upload image of your face.\
It analyses your mood from it, and gives you a playlist of songs matching your mood.\
The face-to-mood bit is done with [FER](https://pypi.org/project/fer/)\
The song-to-mood bit was done with tensorflow. I used this dataset at [Kaggle](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=tracks.csv)  


Uses SQLite3 and Flask

