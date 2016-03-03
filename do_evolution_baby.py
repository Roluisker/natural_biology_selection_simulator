import random
import sys

print "GOAL:"
CHALLENGE     = sys.stdin.readline()
DNA_SIZE    = len(CHALLENGE)
print "GENERATIONS:"
GENERATIONS = int(sys.stdin.readline())

RAN_SIZE    = 20


def new_population(individual):
    adaptation_val = adaptation_calculation(individual)

    if adaptation_val == 0:
        final = (individual, 1.0)
    else:
        final = (individual, 1.0/adaptation_val)

    return final   

def make_couples(all_population):    
    ind_love_1 = semi_ran_get_in_love(all_population)
    ind_love_2 = semi_ran_get_in_love(all_population) 

    return (ind_love_1,ind_love_2)

def semi_ran_get_in_love(items):
  weight_total = sum((item[1] for item in items))
  ran = random.uniform(0, weight_total)
  for item, weight in items:
    if ran < weight:
      return item
    ran = ran - weight
  return item


def adaptation_calculation(dna):
  adaptation = []
  [ adaptation.append( abs(ord(dna[c]) - ord(CHALLENGE[c])) )  for c in xrange(DNA_SIZE) ] 
  return sum(adaptation)


def random_dna():
  final_dna = []
  for a in xrange(RAN_SIZE):
    dna = ""
    for b in xrange(DNA_SIZE):
      dna += chr(int(random.randrange(32, 126, 1)))
    final_dna.append(dna)
  return final_dna


def mutate(dna):
  dna_out = ""
  mutation_chance = 100
  for c in xrange(DNA_SIZE):
    if int(random.random()*mutation_chance) == 1:
      dna_out += chr(int(random.randrange(32, 126, 1)))
    else:
      dna_out += dna[c]
  return dna_out

def reproduction(dna1, dna2):
  pos = int(random.random()*DNA_SIZE)
  return (dna1[:pos]+dna2[pos:], dna2[:pos]+dna1[pos:])


if __name__ == "__main__":
  
  population = random_dna()
  
  for generation in xrange(GENERATIONS):
    print "Do evolution %s Baby!: '%s'" % (generation, population[0])
    all_population = []

    for individual in population:
      
      all_population.append(new_population(individual))

    population = []

    for a in xrange(RAN_SIZE/2):

      ind_love_1, ind_love_2 = make_couples(all_population)

      ind_love_1, ind_love_2 = reproduction(ind_love_1, ind_love_2)

      population.append(mutate(ind_love_1))
      population.append(mutate(ind_love_2))

  final_string = population[0]

  print "FINAL: %s" % final_string
  print "GOAL: %s" % CHALLENGE

  exit(0)