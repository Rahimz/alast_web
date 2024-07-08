from io import BytesIO
from django.core.files import File
from PIL import Image as IMG

def make_thumbnail(image, size=(150, 150)):
    """Makes thumbnails of given size from given image"""
    thumbnail = None
    # im = IMG.open(image)
    try:
        with IMG.open(image) as im:
            im.convert('RGB') # convert mode

            extension = image.name.split('.')[-1]

            im.thumbnail(size) # resize image

            thumb_io = BytesIO() # create a BytesIO object
            # we have problem with gif image so if the save method doesnot work we do not 
            # make any thumbnail
            try:
                im.save(thumb_io, 'JPEG', quality=85) #, quality=85 save image to BytesIO object
            except:
                return 
            image_name = image.name.split('/')[-1]
            thumbnail = File(thumb_io, name=image_name) # create a django friendly File object
    except:
        pass    
    return thumbnail