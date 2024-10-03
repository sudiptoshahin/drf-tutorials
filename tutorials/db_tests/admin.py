from django.contrib import admin
from db_tests.models import Person, Group, Membership


admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
# admin.site.register(Profile)
