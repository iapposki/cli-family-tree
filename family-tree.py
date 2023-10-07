import typer
import json
from logic import Member

app = typer.Typer()

@app.command()
def init_db():
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
    Member(name)


@app.command()
def add_relation(relation: str):
    Member.add_relation(relation)

@app.command()
def connect(sentence: str):
    Member.connect(sentence)

@app.command()
def count(sentence: str):
    Member.count(sentence)


if __name__ == "__main__":
    app()


