import json

if __name__ == "__main__":
    with open('db.json', 'r') as cnf:
        dbconf = json.load(cnf)
        print(dbconf)
        print(dbconf['host'])
    pass
