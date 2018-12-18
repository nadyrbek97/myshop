from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # We use a TypedChoiceField field with coerce=int to convert the input into an integer
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    # This allows you to indicate whether the quantity has to
    # be added to any existing quantity in the cart for this product(False)
    # or whether the existing quantity has to be updated with the given quantity(True).
    # We use a HiddenInput widget for this field since we don't want to display it to the user
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
