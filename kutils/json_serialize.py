from __future__ import unicode_literals
import json
import importlib
import codecs


PRINTABLE = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~ '


class JsonSerializable(object):
    def to_json_dict(self):
        return {k:self.__dict__[k] for k in self.__dict__ if not k.startswith('_')}


class JsonSerializeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JsonSerializable):
            # m = obj.__class__.__module__
            # c = obj.__class__.__name__
            json_dict = obj.to_json_dict()
            json_dict['_module'] = obj.__class__.__module__
            json_dict['_class'] = obj.__class__.__name__
            # return {
            #     "_module": m,
            #     "_class": c,
            #     "_value": obj.to_json_dict()
            # }
            return json_dict
        if isinstance(obj, bytes):
            json_dict = {'_class': 'bytes', '_module':None}
            try:
                json_dict['utf8'] = obj.decode('utf8')
            except:
                json_dict['repr'] = repr_encode(obj)
            return json_dict
        return json.JSONEncoder.default(self, obj)

# print json.dumps(data, cls=RoundTripEncoder, indent=2)

class JsonSerializeDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        # if '_value' not in obj or '_module' not in obj or '_class' not in obj:
        if '_module' not in obj or '_class' not in obj:
            return obj
        if obj['_module'] is None and obj['_class'] == 'bytes':
            if 'utf8' in obj:
                return obj['utf8'].decode()
            else:
                return repr_decode(obj['repr']) # security risk
        module_ = importlib.import_module(obj['_module'])
        class_ = module_.__dict__[obj['_class']]
        obj_deser = JsonSerializable()
        obj_deser.__module__ = obj['_module']
        obj_deser.__class__ = class_
        obj_deser.__dict__ = obj
        # return class_.from_json_dict(obj)
        return obj_deser


def load(*args, **kwargs):
    if not 'cls' in kwargs:
        kwargs['cls'] = JsonSerializeDecoder
    return json.load(*args, **kwargs)


def loads(*args, **kwargs):
    if not 'cls' in kwargs:
        kwargs['cls'] = JsonSerializeDecoder
    return json.loads(*args, **kwargs)


def dump(*args, **kwargs):
    if not 'cls' in kwargs:
        kwargs['cls'] = JsonSerializeEncoder
    return json.dump(*args, **kwargs)


def dumps(*args, **kwargs):
    if not 'cls' in kwargs:
        kwargs['cls'] = JsonSerializeEncoder
    return json.dumps(*args, **kwargs)

def repr_encode(bin):
    res = u''
    for ci in bin:
        if isinstance(ci, int):
            c = bytes([ci])
        else:
            c = ci
        if c in PRINTABLE:
            res += c.decode('utf8')
        else:
            # hex_ = hex(c)[2:]
            # if len(c) == 1:
            #     res += u'\\0'+ hex_
            # else:
            #     res += u'\\'+ hex_
            res += u'\\' + codecs.encode(c, "hex_codec").decode('utf8')
    return res

def repr_decode(repr_):
    res = b''
    i = 0
    while i < len(repr_):
        if repr_[i] != u'\\':
            res += repr_[i].encode('utf8')
            i += 1
        else:
            res += codecs.decode(repr_[i+1:i+3], "hex_codec")
            i += 3
    return res
