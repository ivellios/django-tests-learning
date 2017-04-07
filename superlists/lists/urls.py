from django.conf.urls import url
from lists.views import view_list, new_list, add_item

urlpatterns = [
    url(r'^new', new_list, name = 'new-list'),
    url(r'^(\d+)/$', view_list, name='view-list'),
    url(r'^(\d+)/add_item$', add_item, name='add-item'),
]
