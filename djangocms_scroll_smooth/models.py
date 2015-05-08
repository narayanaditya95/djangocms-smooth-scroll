from django.db import models
from cms.models import CMSPlugin
from .utils import EASING_CHOICES


class SmoothScrollPluginModel(CMSPlugin):

    easing = models.CharField(
        max_length=25,
        choices=EASING_CHOICES,
        default=EASING_CHOICES[0][0],
        blank=False,
    )

    display_text = models.CharField(
        'Text of the Link',
        blank=False,
        default='',
        help_text=u'Please supply the text to be displayed by the link',
        max_length=32,
    )

    scrollto_id = models.CharField(
        'Scroll To ID',
        blank=False,
        default='',
        help_text=u'Please supply the id of the element to which it should scroll',
        max_length=32,
    )

    speed = models.PositiveIntegerField(
        help_text=u'Speed of the scroll',
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return u'%s:%s:%s' % (self.gist_user, self.gist_id, self.filename)