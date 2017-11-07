Install
*********
```
pip install json_transformer
```


Usage
*******************
```python
from json_transformer import JsonTransformer


class FieldMixin:

    @staticmethod
    def name(value, dict_key='name'):
        return 'new_name', 'johny'

    @staticmethod
    def id(value, dict_key='id'):
        return 'new_id', value

class RandomTransformer(JsonTransformer, FieldMixin):
    _keep_undeclared_methods = True




payload = {'name': 'John', 'id': '1', 'email': 'john@ueni.com'}
print(payload)
print('\n\n')
print(RandomTransormer(**payload)._new_json)

```
>
> o/p
>

```
payload: {'email': john@ueni.com, 'name': 'John', 'id': '1'}

transform: {'email', 'john@ueni.com', 'new_name': 'johny', 'new_id': '1'}
```

Other Utils:
************

```python
from json_transformer import print_object

print_object({'email': 'john@ueni.com', 'new_name': 'johny', 'new_id': '1'})

```

>
> o/p
>

```
class FieldMixin(object):

    @staticmethod
    def new_name(value, dict_key='new_name'):
        return dict_key, value

    @staticmethod
    def new_id(value, dict_key='new_id'):
        return dict_key, value

    @staticmethod
    def email(value, dict_key='email'):
        return dict_key, value

```
