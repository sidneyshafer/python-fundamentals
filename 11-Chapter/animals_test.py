# -------------------------------------
# This program tests the animals module
# -------------------------------------

import animals

mammal = animals.Mammal('regular mammal')
mammal.show_species()
mammal.make_sound()

dog = animals.Dog()
dog.show_species()
dog.make_sound()

cat = animals.Cat()
cat.show_species()
cat.make_sound()
