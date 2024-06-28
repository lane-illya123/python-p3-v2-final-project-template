
from models.__init__ import CURSOR, CONN

class Book:

    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of category instances """
        
        
        sql = """
            CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists category instances """
        sql = """
            DROP TABLE IF EXISTS category;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name values of the current category instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO category (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new category instance and save the object to the database """
        category = cls(name)
        category.save()
        return category

    def update(self):
        """Update the table row corresponding to the current category instance."""
        sql = """
            UPDATE category
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current category instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM category
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Book object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        book = cls.all.get(row[0])
        if book:
            # ensure attributes match row values in case local instance was modified
            book.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            book = cls(row[1])
            book.id = row[0]
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        """Return a list containing a category object per row in the table"""
        sql = """
            SELECT *
            FROM category
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return a Book object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM category
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a category object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM category
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def recipes(self):
        """Return list of recipes associated with current category"""
        from models.recipe import Recipes
        sql = """
            SELECT * FROM recipes
            WHERE category_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Recipes.instance_from_db(row) for row in rows
        ]                    