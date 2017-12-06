# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, ignore_case=False):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        # self.len_items = len(items)
        # assert self.len_items > 0
        self.items = items
        self.new_items = []
        self.index = -1
        self.ignore_case = ignore_case

        if ignore_case:
            for item in self.items:
                if item not in self.new_items:
                    self.new_items.append(item)
        else:
            for item in self.items:
                if isinstance(item, str):
                    if item.lower() not in [x.lower() for x in self.new_items]:
                        self.new_items.append(item)
                else:
                    if item not in self.new_items:
                        self.new_items.append(item)

    def __next__(self):
        # Нужно реализовать __next__    
        if self.index == len(self.new_items)-1:
            raise StopIteration
        self.index += 1
        return self.new_items[self.index]

    def __iter__(self):
        return self
