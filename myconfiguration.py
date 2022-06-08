import configparser
config = configparser.RawConfigParser()
config.read(filenames="../config.properties")

MOVIE_DB_API_KEY = config.get("themoviedb.org", "mvdb_api_key")