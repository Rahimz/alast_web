# Tools app

We put some extra tools in tools app like:

- abstract models
- convertor for Gregory to Hijri calendar
- pdf or excel makers

## Tools models

We use a TimeStampedModel as an abstract model to add created and updated datetime to each model we make.
Abstract model (that defines in class Meta) is not a real model and don't have any table in the database, they are a predefined model to use in other model.
When we put inherit from them in a model class, all fields in them will add to our model

```python
class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    class Meta: 
        abstract = True 
    
    
    # def get_fa_created(self):
    #     return hij_strf_date(greg_to_hij_date(self.created.date()), '%-d %B %Y')
    # def get_fa_updated(self):
    #     return hij_strf_date(greg_to_hij_date(self.updated.date()), '%-d %B %Y')

    def save(self, *args, **kwargs):
        """
        Overriding the save method in order to make sure that
        modified field is updated even if it is not given as
        a parameter to the update field argument.
        """
        update_fields = kwargs.get('update_fields', None)
        if update_fields:
            kwargs['update_fields'] = set(update_fields).union({'updated'})

        super().save(*args, **kwargs)
```

And we make a new model like this:

```python
class Solution(TimeStampedModel):
   ...
```


```python
class GregoryToHijriConverter(models.Model):
    conversion_date = models.DateField()
    gregorian_date = models.DateField()
    hijri_date = models.DateField()
```

```python
class PdfExcelMaker(models.Model):
    file_type = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')

    def __str__(self):
```