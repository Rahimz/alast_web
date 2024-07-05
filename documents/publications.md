# Publications app

## Pages

Page 1: Publications
    - List of publications

Page 2: Contact Us
    -static data 
    -map 
    -contact form 
    -social links

Page 3: Publications Article:
    -content 
    -pdf 
    -summary
    -title
    -authors
    -category

## Models

### PublicationCategory

    ```python
    class PublicationCategory(models.Model):
        name = models.CharField(max_length=255)
    ```

### PublicationAuthor

    ```python
    class PublicationAuthor(models.Model):
        name = models.CharField(max_length=255)
    ```
    
### PublicationList
    ```python
    class PublicationList(models.Model):
        title = models.CharField(max_length=255)
        category = models.ForeignKey(PublicationCategory, on_delete=models.CASCADE)
    ```

### PublicationArticle

    ```python
    class PublicationArticle(GregoryToHijriConverter):
        title = models.CharField(max_length=255)
        content = models.TextField()
        pdf = models.FileField(upload_to='pdf/')
        summary = models.TextField()
        authors = models.ForeignKey(PublicationAuthor, on_delete=models.CASCADE)
        category = models.ForeignKey(PublicationCategory, on_delete=models.CASCADE)
    ```
    
### Contact
    ```python
    class Contact(PdfExcelMaker):
        static_data = models.TextField()
        maps = models.CharField(max_length=255)
        contact_form = models.TextField()
        social_links = models.URLField()
    ```
    