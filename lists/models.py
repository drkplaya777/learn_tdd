from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    
    shared_with = models.ManyToManyField(
    
        settings.AUTH_USER_MODEL, related_name='sharee'
    
    )
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])
        
    @classmethod 
    def create_new(cls, first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)
        
        Item.objects.create(text=first_item_text, list=list_)
    
        return list_
        
    @classmethod
    def find_list(cls, list_id):
        try:
            list_ = List.objects.get(id=list_id)
        except List.DoesNotExist:
            return None
        else:        
            return list_
    
    def share(self, user_email):
        User = get_user_model()
        user = User.objects.get(email=user_email)
        
        self.shared_with.add(user)
        
        return True
    
    @property
    def name(self):
        return self.item_set.first().text
        
        
class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
    
    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')
        
    def __str__(self):
        return self.text
