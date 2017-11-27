from django import forms

CATEGORY = (('Clothing','Clothing'),
            ('Shoes','Shoes'),
            ('Bags','Bags'),
            ('Accessoires','Accessoires'),
            ('Gifts','Gifts'),
            ('Jewelry_and_Watches','Jewelry_and_Watches'),
            ('Lingerie','Lingerie'),
            ('Beauty','Beauty')
            )
SPIDERS = (('Net-a-porter spider','Net-a-porter spider'),)

class SimpleForm(forms.Form):
    spider = forms.CharField(widget=forms.Select(choices=SPIDERS))
    category = forms.CharField(widget=forms.Select(choices=CATEGORY))

