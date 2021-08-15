from django import forms
from ads.models import Ad, Tag, Comment


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})


class AddTagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(AddTagForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')

    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
