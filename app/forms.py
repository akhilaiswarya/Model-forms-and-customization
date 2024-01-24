from django import forms

from app.models import *


class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class WebPageForm(forms.ModelForm):
    class Meta():
        model=WebPage
        fields='__all__'
        #fields=['topic_name','name','gmail']
        #exclude=['url','name']
        labels={'topic_name':'TN','gmail':'g'}
        widgets={'name':forms.Textarea(),'gmail':forms.PasswordInput}


class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'
        