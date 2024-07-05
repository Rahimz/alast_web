# multimedias app

This app handle all images and videos we need for each part

## models



```python

class Gallery(TimeStampedModel):
    solution = models.Foreignkey(Solution)
    publication = models.Foreignkey(Publication)    
    zone = models.CharField()
    title
    slug
    uuid

class Image(TimeStampedModel):
    gallery = models.ForeignKey(Gallery)
    title = models.CharField()
    file = models.ImageField()
    thumbnail = models.ImageField()
    image_alt = models.charField()
```
