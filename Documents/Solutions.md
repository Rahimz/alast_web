Page 1:Solutions List:
    -title 
    -image 
    -short description 
    -link to details
    Categories:
    -tangible: (products, packaging, furniture, graphics)
    -non-tangible: (PSS, service, brand, research - UCID)

Page 2:Solutions Details:
    -images of solutions
    -video 
    -text in repeatable boxes

Models in the app:
    1 Solution:
        -title 
        -image (uploud_to = 'images/')
        -description
        -link
        - category: related with foreignkey to " Solution Category model"
        - research: related with foreignkey to " Solution Research model"

    2 Solution Category: Categories:     
        -tangible: (products, packaging, furniture, graphics)
        -non-tangible: (PSS, service, brand, research - UCID)
        - category choices: tangible, non tangible (not sure?)
        - category type: related with category choices 

    3 Solution Research: research categories: 
        -UCID  
        -UX
        -research choices: (ucid, ux) (not sure?)
        -research category: related with research choices