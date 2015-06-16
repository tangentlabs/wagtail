# This will attempt to include a permission decorator from the
# settings. If the decorator does not exist, the normal django
# permissions decorator will be used.
# This allows users to override the django-centric behaviours.
import importlib

from django.conf import settings
from django.contrib.auth.decorators import permission_required as django_permission_required


try:
    module = importlib.import_module(settings.WAGTAIL_PERMISSIONS_DECORATOR[0])
    permission_required = getattr(module, settings.WAGTAIL_PERMISSIONS_DECORATOR[1])
except (IndexError, ImportError, AttributeError) as err:
    permission_required = django_permission_required

# A simple example of an overridden decorator would be
#
#def _cms_permission_test(test_func, login_url=None, **kwargs):
#    def decorator(view_func):
#        @wraps(view_func)
#        def _wrapped_view(request, *args, **kwargs):
#            return view_func(request, *args, **kwargs)
#        return _wrapped_view
#    return decorator
#
#
#def cms_permissions(perm, login_url=None, raise_exception=False):
#    def _test_func(request, *args, **kwargs):
#        return True
#    return _cms_permission_test(_test_func, login_url=login_url)
