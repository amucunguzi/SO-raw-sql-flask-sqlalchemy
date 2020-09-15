class SomeService(object):
    def __init__(self, db):
        self.db = db

    def get_some_db_data(self):
        print('.... Calling db')
        result = self.db.engine.execute("select * from <table-name>; ")
        return [row for row in result]
