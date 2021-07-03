from flask import (
    Blueprint, g, render_template,
    request,url_for
)
from flaskApp.db import get_db
from flaskApp.face_to_mood import give_result
import pandas as pd
from flaskApp.helpers import implode_df,get_playlist

bp = Blueprint('mood', __name__,url_prefix='/suggest')

@bp.route('/')
def index():
    return render_template('mood.html')

@bp.route('/upload')
def upload():
    return render_template('upload.html')

@bp.route('/result',methods = ['GET', 'POST'])
def result():
    image_save_point = 'user_faces/image.jpg'
    if request.method == 'POST':
        f = request.files['file']       
        f.save(image_save_point)
        moods = give_result(image_save_point)
        playlist = get_playlist(get_db(), moods)
        df = pd.DataFrame(playlist)
        df = implode_df(df, 'url', 'artist_name')
        return df.to_html()

