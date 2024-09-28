from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('userapp.urls', namespace='userapp')),
                  path('course/', include('courseapp.urls', namespace='courseapp')),
                  path('trainer/', include('trainers.urls', namespace='trainers')),
                  path('batch/', include('batchapp.urls', namespace='batchapp')),
                  path('student/', include('studentapp.urls',namespace='studentapp')),
                  path('admins/', include('adminapp.urls',namespace='adminapp')),
                  path('topic/', include('topicapp.urls', namespace='topicapp')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
