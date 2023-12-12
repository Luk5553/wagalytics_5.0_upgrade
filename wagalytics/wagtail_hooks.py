from django.utils.translation import gettext as _

from wagtail import hooks
from wagtail.admin.menu import MenuItem

from django.urls import re_path, include
from django.urls import reverse


from . import urls
from . import views


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^analytics/', include(urls)),
    ]

@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Analytics'),
        reverse('wagalytics_dashboard'),
        classnames='icon icon-fa-bar-chart',
        order=1000
    )
