from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _

class Video(models.Model):
    caption = models.CharField(_("caption"), max_length=260)
    video = models.FileField(_("video"), upload_to='video/%y')

    

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.caption
