import datetime

from django import forms
from django.template.defaultfilters import slugify

from comics.core.models import Comic
from comics.sets.models import Set

class NewSetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ('name',)

    def save(self, commit=True):
        set = super(NewSetForm, self).save(commit=False)
        set.name = slugify(set.name)
        set.last_modified = datetime.datetime.now()
        set.last_loaded = datetime.datetime.now()
        if commit:
            set.save()
        return set

class EditSetForm(forms.ModelForm):
    comics = forms.ModelMultipleChoiceField(
        Comic.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple)
    add_new_comics = forms.BooleanField(
        label='Automatically add new comics to the set', required=False)
    hide_empty_strips = forms.BooleanField(
        label='Hide comic from set view if no strips for the interval exists', required=False)

    class Meta:
        model = Set
        fields = ('add_new_comics', 'comics',)

    def save(self, commit=True):
        comics_set = super(EditSetForm, self).save(commit=False)
        comics_set.last_modified = datetime.datetime.now()
        if commit:
            comics_set.save()
            self.save_m2m()
        return comics_set
