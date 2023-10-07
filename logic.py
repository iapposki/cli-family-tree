import json


class Member: 
    def __init__(self, name, gender = None) :
        self.name = name
        self.gender = gender
        self.relation = {}
        new_member = {'name': self.name, 'gender': self.gender, 'relation': self.relation}
        data = self.load_data()
        if self.name in data['members']:
            res = 'Sorry...member with same name already present'
        else:
            with open('db.json', 'w') as file:
                data['members'][self.name.lower()] = new_member
                json.dump(data,file,indent=4)
                res = f'{self.name} successfully added as a member'
        print(res)

    @staticmethod
    def count(sentence):
        parts = sentence.split(" ")
        relation = parts[0].lower()
        if relation[-1] == 's':
            relation = relation[0:len(relation)-1]
        if relation == 'wive': 
            relation = 'wife'
        name = " ".join(parts[parts.index('of')+1:])
        data = Member.load_data()
        if relation in data['members'][name.lower()]['relation']:
            print(len(data['members'][name.lower()]['relation'][relation]))
        else:
            print(0)


    @staticmethod
    def connect(sentence):
        parts = sentence.split(" ")
        first_name = " ".join(parts[0:parts.index('as')])
        second_name = " ".join(parts[parts.index('of')+ 1:])
        relation = parts[parts.index('as')+1]
        data = Member.load_data()
        if relation in data['members'][second_name.lower()]['relation']:
            data['members'][second_name.lower()]['relation'][relation].append(first_name.lower())
        else: 
            data['members'][second_name.lower()]['relation'][relation] = [first_name.lower()]
        Member.dump_data(data)
        # print(first_name, second_name, relation)

    @staticmethod    
    def load_data():
        with open('db.json', 'r') as file:
                data = json.load(file)
        return data

    @staticmethod
    def dump_data(data):
         with open('db.json', 'w') as file:
              json.dump(data,file, indent=4)

    @staticmethod
    def add_relation(relation):
        data = Member.load_data()
        data['relation'][relation.lower()] = {}
        Member.dump_data(data)
    
        