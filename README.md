                                                                Blogs Django Assignment 2023-v2
                              The goal is to create a Web application using Django where users can create and publish blogs.
             Must have:
             
              # DONE - User Authentication - You can use Django’s default 
              # DONE - Post table - Create a table with following fields (id, title, author, content, creation_date,published_date)
              # DONE - Create Forms that allows authenticated users to create and update Posts
              # DONE ONLY BY CLICKING CHECKBOX Only published posts can be seen by everyone 
                    # uncompleted  draft work - Posts can be saved as draft or can be published. Only published posts can be seen by everyone
                     
             Good to have:
                    - Dynamic Fields for Post author should be allowed to add dynamic fields
              # DONE - Support for images in the Post
              
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
 # RUN THE APP AND SCREEN SHOTS
 
  ![image](https://github.com/shaileshpawar821/blog/assets/135419941/d27d4583-ecb9-41c0-9460-ae377c635dab)
  
 step 1: run the app
       Command -- python manage.py runserver
                  after running it, you can go to localhost:8000 or 127.0.0.1:8000.
                  
display home page of the app

- in this app a top of header section create a boostrap navbar inside 4 tabs 1.Home 2.Create blog 3.Login/Regi 4.Logout
- If the user wants to create a blog or post, he has to login first. redirect to login page not a user

Login Page:
        ![image](https://github.com/shaileshpawar821/blog/assets/135419941/0b0630a4-1e11-4f81-a592-9cb76667814c)
-If the user is not registered then he can register from here also.

Register page:
        ![image](https://github.com/shaileshpawar821/blog/assets/135419941/65be2e6d-9761-4ae8-b4ea-5743f9ea0138)

Create Post Page with Form:
        ![image](https://github.com/shaileshpawar821/blog/assets/135419941/1aee50ff-1700-4038-bc7c-283fa61f64b1)
        
- when submit the post then display in home page list of post seen everyone 
#Only published posts can be seen by everyone when in form check box clicking 

         ![image](https://github.com/shaileshpawar821/blog/assets/135419941/23771c7a-9005-429c-b0c7-343eac8ab5b5)
         
Edit post with edit post form 

# Edit post button display on the post image top-left side Click
 
 edit post form
   ![image](https://github.com/shaileshpawar821/blog/assets/135419941/0bfd512b-3922-409b-9ab3-f1ff4effca3e)

Last Logout Link in Navbar last 
    when click Logout link redirect to home page 
    

--------------

Model/table 

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title




                    
                    
