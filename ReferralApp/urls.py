from django.conf.urls.static import static
from django.urls import path
from ReferralApp import views
from VresMpes import settings

urlpatterns = [
    # other urls

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)