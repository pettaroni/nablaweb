# -*- coding: utf-8 -*-


from django.db import models
from content.models import Content


class News(Content):

    # Tekstinnhold
    headline = models.CharField(verbose_name="tittel", max_length=100, blank=False)
    lead_paragraph = models.TextField(verbose_name="ingress", blank=True, help_text="Vises på forsiden og i artikkelen")
    body = models.TextField(verbose_name="brødtekst", blank=True, help_text="Vises kun i artikkelen")

    PRIORITY_NUMBERS = ( 
        (0 , '0 - Dukker ikke opp'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10 - Er på forsida hele tiden')
        )
    priority = models.IntegerField(verbose_name="Prioritering", choices = PRIORITY_NUMBERS, default=5,
                                blank=False, null= False, help_text="Prioritering av saken på forsiden. Dette fungerer for øyeblikket ikke. Bortsett fra at prioritering=0 fjerner saken fra forsiden.") 



    def correct_picture(self): return self.picture
    def correct_cropping(self): return self.cropping

    class Meta:
        verbose_name = "nyhet"
        verbose_name_plural = "nyheter"
    
    @property
    def as_child_class(self):
        if hasattr(self, 'advert'):
            return self.advert
        elif hasattr(self, 'bedpres'):
            return self.bedpres
        else:
            return self

    def __unicode__(self):
        return self.headline
