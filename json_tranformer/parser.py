class DataTranformer:

    def __init__(self, **fields):
        self._new_json = dict(
            getattr(self, field)(value)
            for field, value in fields.items()
            if getattr(self, field, None)
        )


def print_object(json, space='    '):
    obj_str = 'class FieldMixin:\n\n'
    for method in json:
        obj_str += '{}@staticmethod\n'.format(space)
        obj_str += '{s}def {method}(value, dict_key=\'{method}\'):\n'.format(s=space, method=method)
        obj_str += '{s}{s}return dict_key, value\n\n'.format(s=space)

    print(obj_str)

