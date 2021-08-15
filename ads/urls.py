from django.urls import path

from . import views

app_name = "ads"

urlpatterns = [
    path("", views.AdView.as_view(), name="ad-list"),
    path("ad", views.AddAd.as_view(), name='ad-create'),
    path("addetail/<int:pk>", views.AdDetail.as_view(), name='ad-detail'),
    path("addetail/<int:pk>/comment", views.AddComment.as_view(), name='comment-create'),
    path("addetail/<int:pk>/tag", views.AddTag.as_view(), name='tag-create'),
    path("<int:pk>", views.get_ad, name='get-ad')
]
