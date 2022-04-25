import pandas as pd
import bitarray
import mmh3


def bloom_hash(item, size, hash_count):
    bit_array = bitarray.bitarray(size)
    bit_array.setall(0)
    for ii in range(hash_count):
        index = mmh3.hash(item, ii) % size
        bit_array[index] = 1
    return bytes(bit_array)

# similarity coefficient
def sum_digits(bits):
    digits = [int(x) for x in list(bits)]
    return sum(digits)

def dice_coeff(bits1, bits2):
    bits = list(zip(bits1, bits2))
    commons = sum([x[0] == x[1] for x in bits])
    return (2 * commons) / (sum_digits(bits1) + sum_digits(bits2))


class BloomFilter(set):
    def __init__(self, size, hash_count):
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)
        self.size = size
        self.hash_count = hash_count

    def add(self, item):
        for ii in range(self.hash_count):
            index = mmh3.hash(item, ii) % self.size
            self.bit_array[index] = 1
        return self

    def __contains__(self, item):
        out = True
        for ii in range(self.hash_count):
            index = mmh3.hash(item, ii) % self.size
            ### If what I am expecting to be a 1 turns out to be a 0, then return False
            if self.bit_array[index] == 0:
                out = False
        return out
    
    def return_hash(self, item):
        bit_array = bitarray.bitarray(self.size)
        bit_array.setall(0)
        for ii in range(self.hash_count):
            index = mmh3.hash(item, ii) % self.size
            bit_array[index] = 1
        return bit_array

if __name__ == '__main__':   
    bloom = BloomFilter(size = 100, hash_count = 10)
    animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle',
               'bird', 'bison', 'boar', 'butterfly', 'ant', 'anaconda', 'bear',
               'chicken', 'dolphin', 'donkey', 'crow', 'crocodile']
    # First insertion of animals into the bloom filter
    for animal in animals:
        bloom.add(animal)
        print(bloom.return_hash(animal))

    # Membership existence for already inserted animals
    # There should not be any false negatives
    for animal in animals:
        if animal in bloom:
            print('{} is in bloom filter as expected'.format(animal))
        else:
            print('Something is terribly went wrong for {}'.format(animal))
            print('FALSE NEGATIVE!')

    # Membership existence for not inserted animals
    # There could be false positives
    other_animals = ['badger', 'cow', 'pig', 'sheep', 'bee', 'wolf', 'fox',
                     'whale', 'shark', 'fish', 'turkey', 'duck', 'dove',
                     'deer', 'elephant', 'frog', 'falcon', 'goat', 'gorilla',
                     'hawk' ]
    for other_animal in other_animals:
        if other_animal in bloom:
            print('{} is not in the bloom, but a false positive'.format(other_animal))
        else:
            print('{} is not in the bloom filter as expected'.format(other_animal))
        
        
##Using bloomfilter library:
# from bloom_filter2 import BloomFilter
# instantiate BloomFilter with custom settings,
# max_elements is how many elements you expect the filter to hold.
# error_rate defines accuracy; You can use defaults with
# `BloomFilter()` without any arguments. Following example
# is same as defaults:
# bloom = BloomFilter(max_elements=10000, error_rate=0.1)

# # Test whether the bloom-filter has seen a key:
# assert("test-key" in bloom) is False

# # Mark the key as seen
# bloom.add("test-key")

# # Now check again
# assert("test-key" in bloom)