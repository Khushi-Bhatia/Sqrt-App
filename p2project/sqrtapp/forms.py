from django import forms
class SqrtForm(forms.Form):
	num=forms.FloatField(label="",widget=forms.NumberInput(attrs={'placeholder':'enter a number',"min":0.0}))