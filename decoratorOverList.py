import random
import time
import memory_profiler as mem_profile

names = ['Aaba', 'Bbkw', 'Ccko', 'Ddaw', 'Eenm', 'Fflap']
majors = ['Er', 'Dr', 'Com', 'Acc', 'Er', 'Dr']

print("Memory before: {}Mbs".format(mem_profile.memory_usage()))


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
        return result


def people_Generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


t1 = time.process_time()
# people = people_list(9876543219876587987)
people = people_Generator(1000000)
#
# for i in range(len(names)):
#     print(people.__iter__().__next__())


t2 = time.process_time()
print("Memory after: {}Mbs".format(mem_profile.memory_usage()))
print("Took {} seconds".format(t2 - t1))

# time.perf_counter() or time.process_time()
