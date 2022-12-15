from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    # для вывода документации о API (swagger)
    path('API_schema', get_schema_view(title="API information's",
                                       description='Это документация к тестовому API '
                                       ), name='API_schema'),
    path('docs/', TemplateView.as_view(
        template_name='index.html',
        extra_context={'schema_url': 'API_schema'}
    ), name='docs'),
    path('admin/', admin.site.urls),
    path('v1/', include('app.urls')),
    # авторизация и регистрация
    # path('auth/', include('djoser.urls')),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/token', obtain_auth_token, name='token'),
    # path('auth/logout/', Logout.as_view()),

]
