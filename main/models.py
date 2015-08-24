from django.db import models
#from cartridge.shop.models import Product
#from mezzanine.generic.fields import CommentsField, KeywordsField

class Profile(models.Model):

    user = models.OneToOneField("auth.User")
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return "%s" % (self.user)


#class Good(Product, Ownable):


#class Good(Product, Ownable):
    
#    comments = CommentsField()
#    keywords = KeywordsField()
    
#   class Meta:
#        verbose_name = _("Good")
 #       verbose_name_plural = _("Goods")

#    @models.permalink
  #  def get_absolute_url(self):
    #    return ("good_detail", (), {"slug": self.slug})

