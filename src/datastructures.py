from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []
        
        # Añadir familia
        self.add_member({
            "first_name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })
        
        self.add_member({
            "first_name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })
        
        self.add_member({
            "first_name": "Jimmy",
            "age": 5,
            "lucky_numbers": [1]
        })

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["last_name"] = self.last_name
        if "id" not in member:
            member["id"] = self._generateId()
        self._members.append(member)
        
        return member

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(i)
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None
    def get_all_members(self):
        return self._members