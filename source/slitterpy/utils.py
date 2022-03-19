import inspect
from typing import Any

def mapClass(class_obj, options:dict ={}):
    option_defaults = {
        'ignore-attributes': False,
        'ignore-classes': False,
        'ignore-methods': False,
        'ignore-dunder': False,
        'ignore-type': False
    }

    options = option_defaults | options

    attribute_list = []
    
    def addAttribute(attr_type, attr):
        if options['ignore-type']:
            attribute_list.append(attr)
        else:
            attribute_list.append([attr_type, attr])

    for attribute in dir(class_obj):
        if options['ignore-dunder'] == False and attribute.startswith('__'):
            if options['ignore-attributes'] == False and not callable(getattr(class_obj, attribute)):
                addAttribute("dunder-attributes", attribute)
            if options['ignore-methods'] == False and inspect.isfunction(getattr(class_obj, attribute)):
                addAttribute("duncder-function", attribute)
            if options['ignore-classes'] == False and inspect.isclass(getattr(class_obj, attribute)):
                addAttribute("dunder-class", attribute)
            continue
        if options['ignore-dunder'] == True and attribute.startswith('__'):
            continue
        if options['ignore-attributes'] == False and not callable(getattr(class_obj, attribute)):
            addAttribute("attributes", attribute)
        if options['ignore-methods'] == False and inspect.isfunction(getattr(class_obj, attribute)):
            addAttribute("function", attribute)
        if options['ignore-classes'] == False and inspect.isclass(getattr(class_obj, attribute)):
            addAttribute("class", attribute)

    return attribute_list

def methodExists(cls: object, method: str):
    return hasattr(cls, method) and callable(getattr(cls, method))

def callMethodFromString(cls: object, method: str, *args, **kwargs) -> Any:
    if methodExists(cls, method):
        method = getattr(cls, method)
        return method(*args, **kwargs)