import json


class Member: 
    def __init__(self, info) :
        parts = info.split(" ")
        if parts[-1] == 'female' or parts[-1] == 'male':
            self.name = " ".join(parts[0:len(parts)-1])
            self.gender = parts[-1]
        else:
            self.name = " ".join(parts)
            self.gender = None
            
        self.relation = {}
        new_member = {'name': self.name, 'gender': self.gender, 'relation': self.relation}
        data = self.load_data()
        if self.name.lower() in data['members']:
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
            print(f'{len(data['members'][name.lower()]['relation'][relation])} {relation} found : {data['members'][name.lower()]['relation'][relation]}')
        else:
            print(f'0 {relation} found.')


    @staticmethod
    def connect(sentence):
        relationship_dict = {
            "father": "son daughter",
            "mother": "son daughter",
            "brother": "brother sister",
            "sister": "brother sister",
            "grandmother": "grandson granddaughter",
            "grandfather": "grandson granddaughter",
            "grandson": "grandfather grandmother",
            "granddaughter": "grandfather grandmother",
            "uncle": "nephew niece",
            "aunt": "nephew niece",
            "nephew": "uncle aunt",
            "niece": "uncle aunt",
            "son": "father mother",
            "daughter": "father mother",
            "husband": "husband wife",
            "wife": "husband wife",
        }
        female_relationship_set = {'sister', 'mother', 'grandmother', 'aunt', 'niece', 'daughter', 'wife'}
        parts = sentence.split(" ")
        first_name = " ".join(parts[0:parts.index('as')])
        second_name = " ".join(parts[parts.index('of')+ 1:])
        relation = parts[parts.index('as')+1].lower()
        data = Member.load_data()
        if relation in data['members'][second_name.lower()]['relation']:
            data['members'][second_name.lower()]['relation'][relation].append(first_name.lower())
            data['members'][second_name.lower()]['relation'][relation] = list(set(data['members'][second_name.lower()]['relation'][relation]))
            if relation in female_relationship_set:
                data['members'][first_name.lower()]['gender'] = 'female'
            else:
                data['members'][first_name.lower()]['gender'] = 'male'
        else: 
            data['members'][second_name.lower()]['relation'][relation] = [first_name.lower()]
            if relation in female_relationship_set:
                data['members'][first_name.lower()]['gender'] = 'female'
            else:
                data['members'][first_name.lower()]['gender'] = 'male'

        if data['members'][second_name.lower()]['gender'] == 'female':
            if relationship_dict[relation].split(" ")[1] in data['members'][first_name.lower()]['relation']:
                data['members'][first_name.lower()]['relation'][relationship_dict[relation].split(" ")[1]].append(second_name.lower())
                data['members'][first_name.lower()]['relation'][relationship_dict[relation].split(" ")[1]] = list(set(data['members'][first_name.lower()]['relation'][relationship_dict[relation].split(" ")[1]]))
            else:
                data['members'][first_name.lower()]['relation'][relationship_dict[relation].split(" ")[1]] = [second_name.lower()]
        elif data['members'][second_name.lower()]['gender'] == 'male' :
            if relationship_dict[relation].split(" ")[0] in data['members'][first_name.lower()]['relation']:
                data['members'][first_name.lower()]['relation'][relationship_dict[relation].split(" ")[0]].append(second_name.lower())
                data['members'][first_name.lower()]['relation'][relationship_dict[relation].split(" ")[0]] = list(set(data['members'][first_name.lower()]['relation'][relationship_dict[relation].split(" ")[0]]))
            else:
                data['members'][first_name.lower()]['relation'][relationship_dict[relation].split(" ")[0]] = [second_name.lower()]
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
    
        