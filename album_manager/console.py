# print('hello')
import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


# artist1=Artist('Taylor','Swift')
# artist2=Artist('1975','band')
# artist3=Artist('Greg','Goyo',28)

artist1=artist_repository.select(26)
artist2=artist_repository.select(27)
artist3=artist_repository.select(28)


album1=Album('Lover',2020,artist1)
album2=Album('22',2015,artist1)
album3=Album('Speak Now',2012,artist1)
album4=Album('Chocolate',2013,artist2)
album5=Album('TOOMANY',2023,artist2)


# --->test save artist func
# artist_repository.save(artist1)
# artist_repository.save(artist2)
# artist_repository.save(artist3)


# --->test select all func
# result=artist_repository.select_all()
# for artist in result:
#     print(artist.__dict__)

#--->test select by id func
# result=artist_repository.select(3)
# print(result.__dict__)

# --->test delete func
# result=artist_repository.delete(3)
# result=artist_repository.select_all()
# for artist in result:
#     print(artist.__dict__)

# -->test delete all
# artist_repository.delete_all()

# -->test update/edit artist
# result=artist_repository.update(artist3)
# print(artist3.__dict__)


# -->test save album
result=album_repository.save(album1)
print(result)