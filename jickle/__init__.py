import json


class Jickle(object):
    def __init__(self, ori_json):
        self.key_list = list()
        self.output_dict = dict()
        self.output_str = None
        # load json
        try:
            self.ori_dict = json.loads(ori_json)
        except:
            raise Exception("Error parsing json document!")

        for k, v in self.ori_dict.items():
            self.key_list.append(k)
            if isinstance(v, dict):
                v1 = json.dumps(v)
                x = Jickle(v1)
                setattr(self, k, x)
            else:
                setattr(self, k, v)

    def update(self, output_dict={}):

        for each in self.key_list:
            x = getattr(self, each)
            if isinstance(x, Jickle):
                output_dict[each] = dict()
                x.update(output_dict[each])
            else:
                output_dict[each] = x

        self.output_dict = output_dict
        self.output_str = json.dumps(output_dict)

    def substitute(self, ptn, repl):
        properties_list = list(dir(self))
        for each in dir(self):
            if each in self.key_list:
                properties_list.append(each)

        for each in properties_list:
            x = getattr(self, each)
            if isinstance(x, Jickle):
                x.substitute(ptn, repl)
            else:
                if type(ptn) == type(x) and hasattr(ptn, '__iter__') and ptn in x:
                    setattr(self, each, repl)
                elif type(ptn) == type(x) and ptn == x:
                    setattr(self, each, repl)
