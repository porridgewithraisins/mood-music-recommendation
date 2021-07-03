from flask import (
    Blueprint, g, redirect, render_template,
    request, url_for
)
import pandas as pd
from flaskApp.db import get_db
from flaskApp.helpers import implode_df,query_db

bp = Blueprint('search', __name__, url_prefix = '/search')

@bp.route('/', methods = ['GET'])
def get_user_query():
    return render_template('search.html')

@bp.route('/result', methods =['GET', 'POST'])
def result():
    fields = {
        'song': None,
        'artist': None,
        'year': None,
        'mood' : None
    }
    if request.method == 'POST':
        for field in fields:
            x = request.form.get(field)
            if not x: continue
            fields[field] = x.strip().title()
        res = query_db(get_db(), fields)
        df = pd.DataFrame(res)
        df = implode_df(df,'url', 'artist_name')
        return df.to_html()
    # else get request
    return 'search something first you bozo'
