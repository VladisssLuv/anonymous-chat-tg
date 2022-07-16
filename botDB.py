import json

class DataBaseBot(object):
    def __init__(self):
        pass
    
    def add(self, id_, status, in_dialog, id_companion):
        try:
            data = json.load(open('data_b.json'))
        except:
            data = []
        data.append({'id': id_, 'status': status, 'in_dialog'  :in_dialog, 'id_companion': id_companion})
        with open('data_b.json', 'w') as wfile:
            json.dump(data, wfile, indent=2, ensure_ascii=False)

    def get_id_first(self, find_status = False):
        try:
            data = json.load(open('data_b.json'))
        except:
            return None
        for el in data:
            if el['status'] == find_status:
                return el['id']
        return None

    def get_status(self, find_id):
        try:
            data = json.load(open('data_b.json'))
        except:
            return None
        for el in data:
            if el['id'] == find_id:
                return el['status']
        return None

    def get_in_dialog(self, find_id):
        try:
            data = json.load(open('data_b.json'))
        except:
            return None
        for el in data:
            if el['id'] == find_id:
                return el['in_dialog']
        return None

    def get_id_companion(self, find_id):
        try:
            data = json.load(open('data_b.json'))
        except:
            return None
        for el in data:
            if el['id'] == find_id:
                return el['id_companion']
        return None

    def find_dialog(self):
        try:
            data = json.load(open('data_b.json'))
        except:
            return None
        for el in data:
            if el['status'] == True and el['in_dialog'] == False:
                return el['id']
        return None

    def set_status(self, find_id, new_status):
        try:
            data = json.load(open('data_b.json'))
        except:
            return None
        for el in data:
            if el['id'] == find_id:
                el['status'] = new_status
                break 
        with open('data_b.json', 'w') as wfile:
            json.dump(data, wfile, indent=2, ensure_ascii=False)

    def set_in_dialog(self, find_id, new_in_gialog):
        try:
            data = json.load(open('data_b.json'))
        except:
            return None
        for el in data:
            if el['id'] == find_id:
                el['in_dialog'] = new_in_gialog
                break
        with open('data_b.json', 'w') as wfile:
            json.dump(data, wfile, indent=2, ensure_ascii=False)

    def set_id_companion(self, find_id, new_id):
        try:
            data = json.load(open('data_b.json'))
        except:
            return None
        for el in data:
            if el['id'] == find_id:
                el['id_companion'] = new_id
                break
        with open('data_b.json', 'w') as wfile:
            json.dump(data, wfile, indent=2, ensure_ascii=False)
