from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.showLog),
    path('main', views.showMain),
    path('requests', views.showReq),
    path('SignUp', views.Signing),
    path('Calculate', views.Calculate),
    path('showRequests', views.showRequests)

]+ static(settings.STATIC_URL, document_rootr=settings.STATIC_ROOT)