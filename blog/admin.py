from django.contrib import admin
from django.db import models
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as
from ckeditor.widgets import CKEditorWidget

from .models import Post
admin.site.register(Post)

class FlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget':CKEditorWidget}
    }
# Register your models here.
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
