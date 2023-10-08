# cli-family-tree

To setup the project: 

```
python -m venv .venv
python -m pip install -r requirements.txt
```

Commands:


Cleans and initializes the database with the proper structure for storing data.
```
python -m family-tree init-db
```
Adds a person as a member with an optional field of gender(recommended).                                       
```
python -m family-tree "KK Dhakad male"
```
Adds relation.                                                                                    
```
python -m family-tree add-relation "son"
```
Adds relation between two members. Example : `python -m family-tree connect `                                                     
```
python -m family-tree connect "Amit Dhakad as son of KK Dhakad"
```        
Counts and states the members with the same relation as given.
```
python -m family-tree count sons of "KK Dhakad"
```          

Notes: 
-  DB is stored in root directory in json format.
-  Code does not support multiple people with same name.
-  Code provides gender based on relationship using the `connect` command but since only one gender can be determined in this way, it is recommended to give gender while adding as member
-  A premade (with first order relations) family tree is already present in the db with its copy, reference is saved in the root folder.
