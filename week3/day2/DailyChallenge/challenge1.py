import math


class Pagination:

    def __init__(self, items=None, page_size=10):
        if items is None:
            self.items = []
        self.items = items
        self.page_size = int(page_size)
        self.current_idx = 0
        if not self.items:
            self.total_pages = 1
        else:
            self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        first_item = self.page_size * self.current_idx
        last_item = first_item + self.page_size
        return self.items[first_item:last_item]

    def go_to_page(self, page_num):
        target_idx = page_num - 1
        if target_idx < 0 or target_idx >= self.total_pages:
            raise ValueError(f"Error!")
        self.current_idx = target_idx
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        items_to_print = self.get_visible_items()
        print(items_to_print)
        item = '\n'.join(items_to_print)
        return item


# item=Pagination('abcdefghi', 3)
# print(item.get_visible_items())
# print(item.current_idx)
# print(str(item))

# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabetList, 4)
# print(str(p))

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
print("la ok")
# ['a', 'b', 'c', 'd']

p.next_page()
print("ok ici")
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

try:
    p.go_to_page(10)
    print(p.current_idx + 1)
except ValueError as e:
    print(e)
    
try:
    p.go_to_page(0)
except ValueError as e:
    print(e)


