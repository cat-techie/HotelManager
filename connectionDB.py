import psycopg2


def connectionDB():
    try:
        con = psycopg2.connect(
            database="HotelDB",
            user="cat-techie",
            password="31657101hd",
            host="",
            port="5432")
        return con
    except psycopg2.OperationalError:
        return None
