class ShoppingListDB:
    def __init__(self):
        self.items = {} 
        self.id_counter = 1

    def add_item(self, item):
        item_id = self.id_counter
        item_with_id = item.model_copy(update={"id": item_id}) if hasattr(item, 'model_copy') else item
        self.items[item_id] = item_with_id
        self.id_counter += 1
        return item_with_id

    def get_all(self, category=None):
        if category:
            return [item for item in self.items.values() if item.category == category]
        return list(self.items.values())

    def update_quantity(self, item_id: int, new_qty: int):
        if item_id not in self.items:
            raise KeyError(f"Item with ID {item_id} not found")
        self.items[item_id].quantity = new_qty
        return self.items[item_id]

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise KeyError(f"Cannot delete: ID {item_id} does not exist")
    
    def clear_all(self):
        self.items.clear()
        self.id_counter = 1

db = ShoppingListDB()