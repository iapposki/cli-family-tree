import typer
import json
from logic import Member

app = typer.Typer()

@app.command()
def init_db():
    """Cleans and initializes the database with the proper structure for storing data.
        Example : python -m family-tree init-db
    """
    # setup db file
    with open('db.json', 'w+') as file:
        data = {}
        data['members'] = {}
        # data['relations'] = {'daughter': 'parent', 'son' : 'parent', 'father': 'offspring', 'mother' : 'offspring', 'husband': 'wife', 'wife': 'husband', 'brother': 'sibling', 'sister': 'sibling', }
        data['relations'] = {}

        json.dump(data,file,indent=4)

    print('initialized db')

@app.command()
def add_person(name: str) : 
    """Adds a person as a member.
        Example : python -m family-tree "KK Dhakad"
    """
    Member(name)


@app.command()
def add_relation(relation: str):
    """Adds relation. Example : python -m family-tree add-relation "son" """
    Member.add_relation(relation)

@app.command()
def connect(sentence: str):
    """Adds relation between two members. Example : python -m family-tree connect "Amit Dhakad as son of KK Dhakad" """
    Member.connect(sentence)

@app.command()
def count(sentence: str):
    """Counts the members with the same relation as given. Example : python -m family-tree count "sons of KK Dhakad" """
    Member.count(sentence)


if __name__ == "__main__":
    app()


