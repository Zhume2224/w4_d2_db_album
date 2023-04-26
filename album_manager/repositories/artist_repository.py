from db.run_sql import run_sql
from models.artist import Artist


def save(artist):
    sql='INSERT INTO artists (first_name,last_name) VALUES(%s,%s) RETURNING *'
    values=[artist.first_name, artist.last_name]
    results=run_sql(sql, values)
    id=results[0]['id']
    artist.id=id
    return artist



def select_all():
    artists=[]
    sql='SELECT * FROM artists'
    results=run_sql(sql)

    for row in results:
        artist=Artist(row['first_name'],row['last_name'],row['id'])
        # translate to python
        artists.append(artist)

    return artists


def select(id):
    artist=None
    sql='SELECT * FROM artists WHERE id=%s'
    values=[id]
    result=run_sql(sql,values)[0]
    # translate to python
  
    if result is not None:
        artist=Artist(result['first_name'],result['last_name'],result['id'] )

    return artist

def delete(id):
    sql='DELETE FROM artists WHERE id=%s'
    values=[id]
    run_sql(sql,values)

def delete_all():
    sql='DELETE  FROM artists'
    run_sql(sql)
    # no need to put *

def update(artist):
    sql='UPDATE artists SET (first_name,last_name)=(%s,%s)WHERE id=%s'
    values=[artist.first_name,artist.last_name,artist.id]
    run_sql(sql,values)

