from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """Calculating the subtotal for individual item in the cart """
    return price * quantity
