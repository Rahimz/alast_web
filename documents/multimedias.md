# multimedias app

This app handle all images and videos we need for each part

## models

```python
class Image(TimeStampedModel):
    title = models.CharField()
    file = models.ImageField()
    thumbnail = models.ImageField()
    image_alt = models.charField()
```
