from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repo


def save(album):
    sql='INSERT INTO albums (title,year,artist_id) VALUES(%s,%s,%s) RETURNING *'
    values=[album.title, album.year,album.artist.id]
    results=run_sql(sql, values)
    id=results[0]['id']
    album.id=id
    return album


# method1
# def select_all():
#     albums=[]
#     sql='SELECT * FROM albums'
#     results=run_sql(sql)

#     for row in results:
#         if row != None:
#             albums.append(results)

#     return albums


def select_all():
    albums=[]
    sql='SELECT * FROM albums'
    results=run_sql(sql)

    for row in results:
            artist=artist_repo.select(row['artist_id'])
            print(artist)
        # instance of Artist 
            album=Album(row['title'],row['year'],artist,row['id'])
            albums.append(album)

    return albums


def select(id):
     album=None
     sql='SELECTE * FROM albums WHERE id=%?'
     values=[id]
     result=run_sql(sql,values)
     print('please print this out')
     if result:
          result=result[0]
          artist=artist_repo.select(result['artist_id'])
          album=Album(result['id'],result['title'],result['year'],artist)

     return album

def delete_all():
    sql = "DELETE  FROM tasks"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(album):
    sql = "UPDATE tasks SET (title, year, artist_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [album.title, album.year, album.artist.id,album.id]
    run_sql(sql, values)


