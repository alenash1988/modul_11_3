
def introspection_info(obj):
        _type = type(obj).__name__
        attributes = dir(obj)
        for method in attributes:
            if callable(getattr(obj, method)):
                module = obj.__class__.__module__
                info = {'type': _type, 'attributes': attributes, 'methods': method, 'modul': module}
                return info




number_info = introspection_info(42)
print(number_info)