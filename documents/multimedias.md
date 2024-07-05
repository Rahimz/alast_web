# multimedias app

This app handle all images and videos we need for each part

## models

```python
class Image(TimeStampedModel):
    soulution = models.Foreignkey(Solution)
    publication = models.Foreignkey(Publication)
    member = models.Foreignkey(TeamMemebr)
    zone = models.CharField()
    title = models.CharField()
    file = models.ImageField()
    thumbnail = models.ImageField()
    image_alt = models.charField()
```
