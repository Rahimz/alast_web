# generals app

## Models 

```python
class TeamMember(TimeStampedModel):
    first_name = models.CharField()
    last_name = models.CharField()    
    role = models.CharField()    
    linkedin = models.URLField()
    image = models.ImageField()

class Award(TimeStampedModel):
    title = models.CharField()
    slug = models.CharField()
    year = models.IntegerField()
    description = models.CharField()
    image = models.ImageField()
```
