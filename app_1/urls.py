from django.urls import path
from app_1 import views
from final_pro import settings
from django.conf.urls.static import static
my_app = "app_1"

urlpatterns = [
    path('createh/',views.createhorror,name="createh"),
    path('readh/',views.readhorror,name="readh"),
    path('modifyh/<id>',views.modifyhorror,name="modifyh"),
    path('deleteh/<id>',views.deletehorror,name="deleteh"),
    path('createc/',views.createcomic,name="createc"),
    path('readc/',views.readcomic,name="readc"),
    path('modifyc/<id>',views.modifycomic,name="modifyc"),
    path('deletec/<id>',views.deletecomic,name="deletec"),
    path('createhis/',views.createhistory,name="createhis"),
    path('readhis/',views.readhistory,name="readhis"),
    path('modifyhis/<id>',views.modifyhistory,name="modifyhis"),
    path('deletehis/<id>',views.deletehistory,name="deletehis"),
    path('createad/',views.createadventure,name="createad"),
    path('readad/',views.readadventure,name="readad"),
    path('modifyad/<id>',views.modifyadventure,name="modifyad"),
    path('deletead/<id>',views.deleteadventure,name="deletead"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
