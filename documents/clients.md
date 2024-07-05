# clients app

## Models

```python
class Client(TimeStampedModel):
    name = models.CharField()
    uuid 
    logo = models.ImageField()
    user = mdoels.ForeignKey(User)


class TimeLine(TimeStampedModel):
    client = models.ForeignKey(Client)
    title = models.CharField()

class TimeLineEvent(TimeStampedModel):
    timeline = models.ForeignKey(TimeLine)
    title = models.CharField()
    image = models.ImageField()
    file = models.FileField()
    text = models.TextField()
    link = models.URLField()
```
