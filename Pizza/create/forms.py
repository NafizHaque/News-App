from django import forms
from .models import Pizza, Toppings

class PizzaModelForm(forms.ModelForm):
    class Meta:
        model = Pizza



        fields = ("title", "size", "toppings", "price") 

        widgets = {
            
            'title': forms.TextInput(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Pizza Name',
                                            
                                            
                                            }),

            'size': forms.Select(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Pizza Size',
                                            
                                            
                                            }),
                                            
            'toppings': forms.SelectMultiple(attrs={
                                                'class': 'form-control',

                                                
                                                
                                            }),

            'price': forms.TextInput(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Price',
                                            
                                            
                                            }),


        }


class ToppingsModelForm(forms.ModelForm):
    class Meta:
        model = Toppings



        fields = ("title", "Spice", "Veg",) 
