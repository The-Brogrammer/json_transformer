from parser import DataTranformer

if __name__ == '__main__':

    class FieldMixin:

        @staticmethod
        def name(value, dict_key='name'):
            return 'new_name', 'Peter'

        @staticmethod
        def id(value, dict_key='id'):
            return 'new_id', value

    class RandomTransormer(DataTranformer, FieldMixin):
        pass


    payload = {'name': 'John', 'id': '1', 'email': None}
    print(payload)
    print('\n\n')
    print(RandomTransormer(**payload)._new_json)
