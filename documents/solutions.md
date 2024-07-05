# Solution app

## Pages

Solutions List:
    - title
    - image
    - short description
    - link to details
  
    Categories:
    - tangible: (products, packaging, furniture, graphics)
    - non-tangible: (PSS, service, brand, research - UCID)
    - Reasearch is also a kind of category and there is no need to add another model for it

Solutions Details:
    - images of solutions
    - video
    - text
    - clien name
    - client logo

## Models

### SolutionCategory

    - Categories should have parent to make a tree structure. each category could have a parent or not.
    - We dont make the category chioces, the admin will make it (tangible: (products, packaging, furniture, graphics) non-tangible: (PSS, service, brand, research - UCID))

    ```python
    class SolutionCategory(TimeStampedModel):
        parent = models.ForeignKey(self, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Parent"))
        name = models.CharField()
        slug = models.SlugField(allow_unicode=True)
    ```

### Solution

    ```python
    class Solution(TimeStampedModel):
        title = models.CharField(max_length=255)
        slug = models.SlugFiels(allow_unicode=True)
        description = models.TextField()
        cover_image = models.ImageField(uploud_to = 'images/')
        client = mdoels.CharField(null=True, blank=True)
        client_logo = models.ImageField(null=True, blank=True)
        category = models.ForeignKey(SolutionCategory, null=True, blank=True, on_delete=models.SET_NULL) # related with foreignkey to " Solution Category model"
    ```