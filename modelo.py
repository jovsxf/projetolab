from bson.objectid import ObjectId

class Maquinario:
    def __init__(self, db):
        self.db = db

    def create_maq(self, marca, modelo, ano, status):
        try:
            res = self.db.collection.insert_one({"marca": marca, "modelo": modelo, "ano": ano, "status": status})
            print(f"Maquinário criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Erro ao criar maquinário: {e}")
            return None

    def read_maq_by_id(self, id):
        try:
            maq = self.db.collection.find_one({"_id": ObjectId(id)})
            if maq:
                print(f"Maquinário encontrado: {maq}")
            return maq
        except Exception as e:
            print(f"Erro ao buscar maquinário: {e}")
            return None

    def update_maq(self, id, marca, modelo, ano, status):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"marca": marca, "modelo": modelo, "ano": ano, "status": status}}
            )
            print(f"Maquinário atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Erro ao atualizar maquinário: {e}")
            return None

    def delete_maq(self, id):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Maquinário deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Erro ao deletar maquinário: {e}")
            return None
    
    def add_operator(self, maq_id, op_id):
        try:
            maq = self.read_maq_by_id(maq_id)
            if maq and maq["operator_id"] is None:
                res = self.db.collection.update_one(
                    {"_id": ObjectId(maq_id)},
                    {"$set": {"operator_id": ObjectId(op_id), "status": "unavailable"}}
                )
                print(f"Operador {op_id} adicionado ao maquinário {maq_id}")
                return res.modified_count
            else:
                print("Maquinário já possui um operador.")
                return 0
        except Exception as e:
            print(f"Erro ao adicionar operador ao maquinário: {e}")
            return None

    def remove_operator(self, maq_id):
        try:
            maq = self.read_maq_by_id(maq_id)
            if maq and maq["operator_id"] is not None:
                res = self.db.collection.update_one(
                    {"_id": ObjectId(maq_id)},
                    {"$set": {"operator_id": None, "status": "available"}}
                )
                print(f"Operador removido do maquinário {maq_id}")
                return res.modified_count
            else:
                print("Maquinário não possui operador.")
                return 0
        except Exception as e:
            print(f"Erro ao remover operador do maquinário: {e}")
            return None    


class Operador:
    def __init__(self, db):
        self.db = db

    def create_op(self, name):
        try:
            res = self.db.collection.insert_one({"name": name, "maq": None})
            print(f"Operador criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Erro ao criar operador: {e}")
            return None

    def read_op(self, name):
        try:
            op = self.db.collection.find_one({"name": name})
            if op:
                print(f"Operador encontrado: {op}")
            return op
        except Exception as e:
            print(f"Erro ao buscar operador: {e}")
            return None

    def update_op(self, name, new_maq):
        try:
            res = self.db.collection.update_one(
                {"name": name},
                {"$set": {"maq": new_maq}}
            )
            print(f"Operador atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Erro ao atualizar operador: {e}")
            return None

    def delete_op(self, name):
        try:
            res = self.db.collection.delete_one({"name": name})
            print(f"Operador deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Erro ao deletar operador: {e}")
            return None
