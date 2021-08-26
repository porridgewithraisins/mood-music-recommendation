# Mood based music recommendation

### Written in python, with SQLite3, Flask and Tensorflow

#### Install
Extract the contents of csv_files.zip into flaskApp/csv_files.

Then, from the folder where the flaskApp directory lies, start a virtual environment (recommended as machine learning packages are thicc)
```bash
python3 -m venv venv
sh venv/bin/activate
```
Then install dependencies,

```bash
pip install -r requirements.txt
```
Then start the app on a local server,
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
Works like:\
Upload image of your face.\
It analyses your mood from it, and gives you a playlist of songs matching your mood.\
The face-to-mood bit is done with [FER](https://pypi.org/project/fer/)\
The song-to-mood bit was done with tensorflow. I used this dataset at [Kaggle](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=tracks.csv)  


Demo:
![26th-21 17](https://user-images.githubusercontent.com/72668511/130995162-e06b052c-f62c-4c3b-9026-1b8705d23db3.gif)

You can also perform a fuzzy search of the entire database
![26th-21 19](https://user-images.githubusercontent.com/72668511/130996179-bb3e5aba-81ce-4d66-8cea-cbb5112c3c0f.gif)

