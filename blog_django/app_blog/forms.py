from django import forms

class  TextCommentForm(forms.Form):

    nombre = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'placeholder':'Ingrese nombre'}))
    creador = forms.CharField(max_length=100)
    post = forms.CharField(max_length = 200)
    date_creacion = forms.DateField()
    
    PENGUIN = 'PNG'
    ATLAS = 'ATL'
    ATHENEO = 'ATH'
    
    editorial_options = [
        (PENGUIN, 'Penguin'),
        (ATLAS, 'Atlas'),
        (ATHENEO, 'Atheneo')]

    editorial = forms.ChoiceField(
        
        choices = editorial_options,
        
    )

    image_view = forms.ImageField()