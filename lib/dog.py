#!/usr/bin/env python3

class Dog:
    def __init__(self, name , breed = "Mutt"):
        self.breed = breed
        self.name = name
fido = Dog("Fido")
fido.breed = "Golden Retriever"
print(fido.breed)
print(fido.name)
