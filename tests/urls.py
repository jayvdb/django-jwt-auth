try:
    from django.conf.urls import patterns
except ImportError:
    def patterns(*args): return args

from tests.views import MockView


urlpatterns = patterns(
    '',
    (r'^jwt/$', MockView.as_view()),
    (r'^auth-token/$', 'jwt_auth.views.obtain_jwt_token'),
)
