CREATE TABLE songs(
    id TEXT PRIMARY KEY,
    name TEXT,
    release_date TEXT,
    mood TEXT,
    url TEXT
);

CREATE TABLE artists(
    artist_id TEXT PRIMARY KEY,
    artist_name TEXT
);

CREATE TABLE popity(
    id TEXT PRIMARY KEY,
    popularity REAL,
    FOREIGN KEY (id) REFERENCES songs (id)
);

CREATE TABLE song_artist(
    id TEXT,
    artist_id TEXT,
    FOREIGN KEY (id) REFERENCES songs (id),
    FOREIGN KEY (artist_id) REFERENCES artists( artist_id)
);