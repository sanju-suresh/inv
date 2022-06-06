from django import forms
from .models import Issue, Item
from .models import Csv

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields =('file_name',)

class Itemlist(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'item_name', 'quantity']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['numberofitems']


class StockCreateForm(forms.Form):
        category = forms.CharField(max_length=100)
        itnumber = forms.IntegerField()
        nameit = forms.CharField(max_length=100)


class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'item_name']


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'item_name', 'quantity']

class returnnumberForm(forms.Form):
    itnumber = forms.IntegerField()