# Contacts app

## Models

    ```python
    class Contact(TimeStampedModel):
        name = models.TextField()
        phne = models.CharField()
        email = models.EmailField()
        messages = models.TextField()
    ```
