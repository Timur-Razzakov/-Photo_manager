from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    # для вывода документации о API (swagger)
    path('Photo_manager', get_schema_view(title="Photo Manager",
                                       description='Документация к тестовому API сервису '
                                       ), name='Photo_manager'),
    path('docs/', TemplateView.as_view(
        template_name='index.html',
        extra_context={'schema_url': 'Photo_manager'}
    ), name='docs'),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    # авторизация и регистрация
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
