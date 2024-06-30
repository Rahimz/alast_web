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

Models in the app:
    1 Publication category:
        -name

    2 Publication Author:
        -name

    3 Publication Lists:
        - title
        -category: related with foreignkey to "publication category model"

    4 Publication Articles: 
        -title 
        -content
        -PDF: upload to "pdf/"
        -summary
        -authors: related with foreignkey to "publication Author model"
        -category: related with foreignkey to "publication category model"

    5 Contact: Attributes: (Is it necessary?)
        -static data
        -map
        -contact form
        -social links