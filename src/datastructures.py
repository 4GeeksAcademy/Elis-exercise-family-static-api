from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # Lista de miembros inicial vacía
        self._members = []

        # Inicializa el ID de la próxima persona
        self._next_id = 1

    # Método para generar un ID aleatorio para los miembros
    def _generateId(self):
        return randint(0, 99999999)

    # Método para generar un ID incremental
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    # Método para añadir un miembro a la familia
    def add_member(self, member):
        # Asegura que el miembro tenga un apellido y un ID
        member["last_name"] = self.last_name
        member["id"] = self._generate_id()
        
        # Asegura que el campo "lucky_numbers" sea una lista (con valores por defecto si es None)
        member["lucky_numbers"] = list(member.get("lucky_numbers", []))

        # Añadir el miembro a la lista de miembros
        self._members.append(member)
        return member

    # Método para eliminar un miembro de la familia por ID
    def delete_member(self, id):
        # Busca el miembro con el ID proporcionado
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                # Elimina el miembro de la lista
                removed_member = self._members.pop(position)
                return removed_member
        
        # Si no se encuentra el miembro, devuelve None
        return None

    # Método para obtener un miembro por su ID
    def get_member(self, id):
        # Busca al miembro en la lista de miembros
        for member in self._members:
            if member["id"] == int(id):
                return member
        
        # Si no se encuentra el miembro, devuelve None
        return None

    # Método para obtener todos los miembros de la familia
    def get_all_members(self):
        return self._members
