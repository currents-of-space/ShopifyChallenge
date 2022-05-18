from django.template.defaultfilters import register

@register.filter
def getSetFromManyToOneRelationship(_object, setName):
    """
    Returns the object's set with the specified name.
    """
    _set = getattr(_object, setName)
    return _set.all()

@register.filter
def calculateTotalOrderPrice(order):
    """
    Calculates the total order price.
    """
    orderElements = order.orderelement_set.all()
    sum = 0
    for orderElement in orderElements:
        sum = sum + (orderElement.product.Price * orderElement.quantity)

    return sum
    
    