from django import forms

from .models import Comment , Category



class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment 

        fields = ( 'name' ,'email' , 'content')

            
        widgets  = {


            "name": forms.TextInput(attrs={'class': 'col-sm-12' ,
                                           'placeholder' :'Enter your name'}),
            "email": forms.TextInput(attrs={'class': 'col-sm-12' , 
                                            'placeholder' :'Enter your email'}),
            "content": forms.Textarea(attrs={'class': 'form-control'  , 
                                             'placeholder' :'Enter your comment'}),
        }
        
        
class FormSearch(forms.Form):
    
     
        q = forms.CharField()
        c = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'))
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['c'].label = ''
            self.fields['c'].required = False
            self.fields['c'].label = 'Category'
            self.fields['q'].label = 'search for'
            self.fields['q'].widget.attrs.update(
                {'class':'form-control'}) 
            
            
            