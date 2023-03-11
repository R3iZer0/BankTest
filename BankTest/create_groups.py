from django.contrib.auth.models import Group

group_name = 'Client'
new_group, created = Group.objects.get_or_create(name=group_name)
