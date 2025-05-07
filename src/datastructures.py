
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 0  # Inicialización del ID automático

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "Pepon",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [5, 6, 7,]
            }

        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        self._next_id += 1
        return self._next_id

    def add_member(self, member):
        # fill this method and update the return
        member['id'] = self._generateId()
        member['last_name'] = self.last_name
        self._members.append(member)
        return member['first_name']

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"success": True, "message": f"El miembro con ID {id} se ha eliminado"}, 200
    
        return {"success": False, "message": f"No existe el miembro con ID {id}"}, 400

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == id:
                return member

        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
