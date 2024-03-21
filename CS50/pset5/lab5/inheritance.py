import sys
import random


class Person():
    def __init__(self, parent0, parent1, alleles, generation):
        self.parent0 = parent0
        self.parent1 = parent1
        self.alleles = alleles
        self.generation = generation


GENERATIONS = 4
persons = []


def main():
    create_family(GENERATIONS)
    print_family(persons)


def create_family(generations):

    def random_allele(options=["A", "B", "0"]):
        return random.choice(options)
    
    if generations > 1:
        parent0 = create_family(generations-1)
        parent1 = create_family(generations-1)

    if generations == 1:
        person = Person(None, None, 
                        [random_allele(), random_allele()], 
                        GENERATIONS-generations)
    else:
        person = Person(parent0, parent1, 
                        [random_allele(parent0.alleles), random_allele(parent1.alleles)], 
                        GENERATIONS-generations)

    persons.append(person)
    #print(f"{generations}: {person.alleles} \t {person.generation}")
    return person


def print_family(persons):
    indent_lenght = 4
    titles = ["Child", "Parent", "Grandparent", "Greatparent"]  # , "5th", "sixth"
    persons.reverse()
    for person in persons:
        title = titles[person.generation]
        print(f"{' '*indent_lenght*person.generation}{title} (Generation {person.generation}): blood type {''.join(person.alleles)}")
    

if __name__ == "__main__":
    main()
    del(persons)
    print()
    sys.exit(0)
