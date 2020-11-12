class Glue_Map_function:
    def __init__(self, fn, **kwargs):
        self.fn = fn
        self.kwargs = kwargs

    def __call__(self, rec):
        return self.fn(rec, **self.kwargs)


if __name__ == '__main__':
    import json
    def reuseable_fn(rec, rec_key, desired_dict, key, value):
        item_list = json.loads(rec[rec_key])
        
        filtered_dict = {item[key]: item[value] for item in item_list if item[key]in desired_dict.keys()} 

        for key in filtered_dict:
            rec[desired_dict[key]] = filtered_dict[key]

        return rec

    rec_key = 'data'
    desired_dict = {
        "a" : "data_a",
        "c" : "data_c",
        'f': 'data_f',
        'z' : 'data_z'
    }

    reuseable_mapping_fn = Glue_Map_function(
        fn=reuseable_fn,
        rec_key=rec_key, 
        desired_dict=desired_dict,
        key='UniKey',
        value='UniVal')

    rec = {'data':'''[{"UniKey": "a", "UniVal": "1"}, {"UniKey": "b", "UniVal": "2"}, {"UniKey": "c", "UniVal": "3"}, {"UniKey": "d", "UniVal": "4"}, {"UniKey": "e", "UniVal": "5"}, {"UniKey": "f", "UniVal": "6"}, {"UniKey": "g", "UniVal": "7"}, {"UniKey": "h", "UniVal": "8"}, {"UniKey": "i", "UniVal": "9"}, {"UniKey": "j", "UniVal": "10"}]'''}
    rec = reuseable_mapping_fn(rec)
    # print(rec)
    print(json.dumps(rec,indent=4))