# Module E7.
## Subject: MongoDB & Redis
Instruction:
1) Clone the repository
2) Install redis, django, djongo, pymongo, django-redis to your PC
3) Make sure the precreated **Redis** and **MongoDB** are working for you (if not, then replace the DATABASES>CLIENT>host & CACHES>default>LOCATION with your MongoDB & Redis IP.)
4) Run the server using command: **_python manage.py runserver_** (if you've added your databases, then run **_python manage.py makemigrations_** firstly, and **_python manage.py migrate_** fte.)
```
URLS:
    path("", views.AdView.as_view(), name="ad-list"), # - index.html page (ListView)
    path("ad", views.AddAd.as_view(), name='ad-create'), # - add.html page (CreateView)
    path("addetail/<int:pk>", views.AdDetail.as_view(), name='ad-detail'), # - detail.html (DetailView)
    path("addetail/<int:pk>/comment", views.AddComment.as_view(), name='comment-create'), # - add_comment.html (CreateView)
    path("addetail/<int:pk>/tag", views.AddTag.as_view(), name='tag-create'), # - add_tag.html (CreateView)
    path("<int:pk>", views.get_ad, name='get-ad') # - get.html (function, allows to find ad by ID)
```
**note. Statistics with a number of comments and tags are available in DetailView**
