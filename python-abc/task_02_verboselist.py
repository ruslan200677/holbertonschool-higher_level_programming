#!/usr/bin/python3


class VerboseList(list):
    """verbo class"""
    def append(self, item):
        """ list append"""
        super().append(item)
        print(f"Added {item} to the list")

    def extend(self, iterable):
        """extenden def"""
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items")
