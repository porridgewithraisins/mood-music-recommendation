def implode_df(df,key_col, implode_col):
    agg_dict = {x : 'first' for x in df}
    agg_dict[implode_col] = ', '.join
    return(
        df.groupby([key_col],as_index=False)
        .agg(agg_dict)
        )


def get_playlist(db, moods, row_count = 100):
    sql =(
        "SELECT name,artists.artist_name,release_date,mood,"
        "popity.popularity,url "
        "FROM songs JOIN song_artist "
        "on songs.id = song_artist.id "
        "JOIN artists "
        "on song_artist.artist_id = artists.artist_id "
        "JOIN popity "
        "on songs.id = popity.id "
        "WHERE mood IN "
        f"({','.join('?'*len(moods))}) "
        "ORDER by popity.popularity DESC "
        f"LIMIT {row_count};"
        )
    params = tuple(moods)
    pl = db.execute(sql,params).fetchall()
    return [dict(row) for row in pl]


def query_db(db, fields, row_count=200): 
    # fields_to_col_names = {
    #     "song" : "name",
    #     "artist" : "artist_name",
    #     "year" : "strftime('%Y', release_date)",
    #     "mood" : "mood"
    # }
    sql =(
            "SELECT name,artists.artist_name,release_date,mood,"
            "popity.popularity,url "
            "FROM songs JOIN song_artist "
            "on songs.id = song_artist.id "
            "JOIN artists "
            "on song_artist.artist_id = artists.artist_id "
            "JOIN popity "
            "on songs.id = popity.id "
            "WHERE "
            "(name like ? OR ? is NULL) AND "
            "(artist_name like ? OR ? is NULL) AND "
            "(strftime('%Y', release_date) = ? OR ? is NULL) AND "
            "(mood = ? or ? is NULL) "
            "ORDER by popity.popularity DESC "
            f"LIMIT {row_count}"
            )
    
    params = [
         ( ('%'+fields['song']+'%') if fields['song'] else fields['song'] ),
         ( ('%'+fields['artist']+'%') if fields['artist'] else fields['artist'] ),
          fields['year'], fields['mood']]

    params = [x for x in params for i in range(2)]
    
    result = db.execute(sql,tuple(params))
    return [dict(row) for row in result]    


# def query_db_test(fields):
#     db = get_db()
#     sql = (
#         "SELECT name,release_date,mood,url "
#         "FROM test WHERE "
#         "(name = ? or ? is NULL) AND "
#         "(strftime('%Y', release_date) = ? or ? is NULL) AND "
#         "(mood = ? or ? is NULL)"
#     )
#     params = [fields['song'], fields['year'], fields['mood']]
#     params = [x for x in params for i in range(2)]
#     result = db.execute(sql,tuple(params))
#     return [dict(row) for row in result]
