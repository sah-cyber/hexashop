from django.db import models
from django import forms


#
#
# class EmailForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     slug = forms.SlugField(max_length=25)
#     email = forms.EmailField()
#     text = forms.TextInput(attrs={'placeholder':'Mesajiniz', 'rows': 5})
#     creted_at = models.DateTimeField(auto_now_add=True, verbose_name='Qeyd_tarixi')
#     creted_up = models.DateTimeField(auto_now=True, verbose_name='Yenilenme_tarixi')
#
#     def __str__(self):
#         return self.name,self.text
#
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.text =
#


class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad")
    slug = models.SlugField(max_length=100,unique=True,null=True)
    email = models.EmailField(verbose_name="Email")
    text = models.TextField(verbose_name='Etrafli')
    creted_at = models.DateTimeField(auto_now_add=True,verbose_name='Qeyd_tarixi')
    creted_up = models.DateTimeField(auto_now=True,verbose_name='Yenilenme_tarixi')
    #public = models.BooleanField(default=True, verbose_name="Derc_edilib")




    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = 'Contact'
    #     verbose_name_plural = 'Contact'

    # def get_absalute_url_shop_page_one(self):
    #     return reverse_lazy('shop_page_one', kwargs={'shop_slug': self.slug})



class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email','text']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': 'Adiniz','id' :'name'}),
            'text': forms.Textarea(attrs={'placeholder':'Mesajiniz', 'rows': 5,'id':'email'}),
            'email': forms.TextInput(attrs={'placeholder':'Email','id' :'message'}),

        }

