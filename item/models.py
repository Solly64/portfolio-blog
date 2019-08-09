from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

class Item(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    description2 = RichTextUploadingField(blank=True, null=True,
    config_name='special', external_plugin_resources = [('youtube',
    '/static/base/ckeditor_plugins/youtube/', 'plugin.js',
    )]
    )
    body = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    slug = models.SlugField(default='', blank=True)

    def save(self):
        self.slug= slugify(self.title)
        super(Item, self).save()

    def __str__(self):
        return '%s' % self.title
