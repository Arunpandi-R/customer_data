import json
import sys

from flask import request


def get_meta_data_json() -> dict:
    if 'json' in request.form:
        json_of_metadata = request.form.to_dict(flat=False)
        try:
            meta_data_from_json = json_of_metadata['json']
            meta_data_from_json_0 = meta_data_from_json[0]
            str_meta_data_from_json_0 = str(meta_data_from_json_0)
            meta_data_dict = json.loads(str_meta_data_from_json_0)
        except Exception as e:
            print(str(e))
    else:
        if request.data is not None:
            try:
                my_json = request.data.decode('utf8').replace("'", '"')
                meta_data_dict = json.loads(my_json)
            except:
               pass
        else:
            pass
    return meta_data_dict

def get_meta_data_json_replace_quotes() -> dict:
    if 'json' in request.form:
        json_of_metadata = request.form.to_dict(flat=False)
        try:
            meta_data_from_json = json_of_metadata['json']
            meta_data_from_json_0 = meta_data_from_json[0]
            str_meta_data_from_json_0 = str(meta_data_from_json_0)
            meta_data_dict = json.loads(str_meta_data_from_json_0)
        except Exception as e:
            pass
    else:
        if request.data is not None:
            try:
                my_json = request.data.decode('utf8').replace("'", '\'')
                meta_data_dict = json.loads(my_json)
            except:
               pass
        else:
            pass

    return meta_data_dict


def get_meta_update_data_json() -> dict:
    if 'json' in request.form:
        json_of_metadata = request.form.to_dict(flat=False)
        try:
            meta_data_from_json = json_of_metadata['json']
            meta_data_from_json_0 = meta_data_from_json[0]
            str_meta_data_from_json_0 = str(meta_data_from_json_0)
            meta_data_dict = json.loads(str_meta_data_from_json_0)
        except Exception as e:
            tb = sys.exc_info()[2]

    else:
        if request.data is not None:
            try:
                my_json = request.data.decode('utf8').replace("'", '"')
                meta_data_dict = json.loads(my_json)
            except:
                meta_data_dict = {}
        else:
            meta_data_dict = {}
    return meta_data_dict


def get_request_files() -> dict:
    files = {'thumbnail': '', 'gallery': [], 'image': ''}
    if 'image' in request.files:
        files.update({'image': request.files['image']})
    else:
        del files['image']
    if 'gallery' in request.files:
        print('gallery exists')
        files.update({'gallery': request.files.getlist('gallery')})
    else:
        del files['gallery']
    if 'thumbnail' in request.files:
        files.update({'thumbnail': request.files['thumbnail']})
    else:
        del files['thumbnail']
    return files


def get_request_binary_data() -> str:
    try:
        data = request.get_data()
    except:
        data = ''
    return data


def get_special_characters_encoding_meta_json() -> dict:
    if request.data is not None:
        try:
            my_json = request.data.decode('utf8')
            meta_data_dict = json.loads(my_json)
            return meta_data_dict
        except Exception as p:
            print(p)
            pass
    else:
        pass
