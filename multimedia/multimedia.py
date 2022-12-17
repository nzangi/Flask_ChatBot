import re
import pydot
from binarytree import build
import itertools
import string

sentence = ''
letter_frequency = {}
global probabilities
probabilities = []

print("Question 1")

with open("input_frequency_file.txt", 'r') as file:
    my_text = file.read().lower()

print("---------------------------------------------------------")
# print('input file contents are:')
# print(my_text)
# print("---------------------------------------------------------")

# reading word by word and ignoring special characters
words = re.findall(r'\w+', my_text)
# appending all words to one sentence
for word in words:
    sentence = sentence + word

# reading alphabet by alphabet
for alphabet in sentence:
    if alphabet not  in string.ascii_lowercase:
        # remove numbers
        continue
    if alphabet in letter_frequency:
        # add length of the alphabet by 1
        letter_frequency[alphabet] += 1
    else:
        # it's the first time alphabet appears
        # so set it's frequency to 1
        letter_frequency[alphabet] = 1

# sort our alphabets ascending
sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=False)
# convert sorted myList back to dictionary
sorted_dictionary = dict(sorted_frequency)

# wring frequency outputs to a file
# and printing our alphabets with respective frequencies
open('output_frequency_file.txt', 'w').close()  # this opens file and removes any existing contents first

for key, value in sorted_frequency:
    # print to standard output
    print(f"{key}\t{value}")
    # print to file
    print(f"{key}\t{value}", file=open('output_frequency_file.txt', 'a'))

print('alphabets and frequencies are also available in output_frequencies_file.txt\n\n\n')




print("**********************************************************")
print("Question 2")
print("**********************************************************")


class HuffmanCoding:
    def __init__(self, probability):
        self.probability = probability

    def position(self, value, index):
        for j in range(len(self.probability)):
            if value >= self.probability[j]:
                return j
        return index - 1

    def compute_code(self):
        num = len(self.probability)
        huffman_coding = [''] * num

        for k in range(num - 2):
            val = self.probability[num - k - 1] + self.probability[num - k - 2]
            if huffman_coding[num - k - 1] != '' and huffman_coding[num - k - 2] != '':
                huffman_coding[-1] = ['1' + symbol for symbol in huffman_coding[-1]]
                huffman_coding[-2] = ['0' + symbol for symbol in huffman_coding[-2]]
            elif huffman_coding[num - k - 1] != '':
                huffman_coding[num - k - 2] = '0'
                huffman_coding[-1] = ['1' + symbol for symbol in huffman_coding[-1]]
            elif huffman_coding[num - k - 2] != '':
                huffman_coding[num - k - 1] = '1'
                huffman_coding[-2] = ['0' + symbol for symbol in huffman_coding[-2]]
            else:
                huffman_coding[num - k - 1] = '1'
                huffman_coding[num - k - 2] = '0'

            position = self.position(val, k)
            probability = self.probability[0:(len(self.probability) - 2)]
            probability.insert(position, val)
            if isinstance(huffman_coding[num - k - 2], list) and isinstance(huffman_coding[num - k - 1], list):
                complete_code = huffman_coding[num - k - 1] + huffman_coding[num - k - 2]
            elif isinstance(huffman_coding[num - k - 2], list):
                complete_code = huffman_coding[num - k - 2] + [huffman_coding[num - k - 1]]
            elif isinstance(huffman_coding[num - k - 1], list):
                complete_code = huffman_coding[num - k - 1] + [huffman_coding[num - k - 2]]
            else:
                complete_code = [huffman_coding[num - k - 2], huffman_coding[num - k - 1]]

            huffman_coding = huffman_coding[0:(len(huffman_coding) - 2)]
            huffman_coding.insert(position, complete_code)

        huffman_coding[0] = ['0' + symbol for symbol in huffman_coding[0]]
        huffman_coding[1] = ['1' + symbol for symbol in huffman_coding[1]]

        if len(huffman_coding[1]) == 0:
            huffman_coding[1] = '1'

        count = 0
        final_code = [''] * num

        for k in range(2):
            for j in range(len(huffman_coding[k])):
                final_code[count] = huffman_coding[k][j]
                count += 1

        final_code = sorted(final_code, key=len)
        return final_code


probabilities = [float("{:.2f}".format(frequency[1] / len(sentence))) for frequency in sorted_frequency]
probabilities = sorted(probabilities)
huffmanClassObject = HuffmanCoding(probabilities)
P = probabilities

huffman_code = huffmanClassObject.compute_code()
print(' Alphabet | Huffman code ')
print('--------------------------')

for key, alphabet in enumerate(sorted_dictionary):
    if huffman_code[key] == '':
        print(' %-4r |%12s' % (alphabet[0], 1))
        continue
    print(' %-4r |%12s' % (alphabet[0], huffman_code[key]))


# calculate huffman code




tree_level = 0

for code in huffman_code:
    if len(code) > tree_level:
        tree_level = len(code)

tree_depth = tree_level + 1

values = []


def get_node_alphabet(code):
    if code in huffman_code:
        # return (int(sorted_frequency[huffman_code.index(code)][1]))/len(sentence)
        return huffman_code.index(code) +1
    else:
        return 0


binary_codes = []

for i in range(tree_depth):
    for code in ["".join(seq) for seq in itertools.product("01", repeat=i)]:
        binary_codes.append(code)

for binary_code in binary_codes:
    values.append(get_node_alphabet(binary_code))

tree = build(values)
tree = str(tree).replace(' 0 ', '   ')


for alphabet in sorted_frequency:
    space_length = len(str(sorted_frequency.index(alphabet)+1))
    if space_length > 1:
        tree = tree.replace(' ' + str(sorted_frequency.index(alphabet) + 1) + ' ', ' ' + alphabet[0] + ' '*space_length)
        tree = tree.replace(' ' + str(sorted_frequency.index(alphabet) + 1) + '\n', ' ' + alphabet[0] + ' '*space_length+'\n')
        tree = tree.replace('\n' + str(sorted_frequency.index(alphabet) + 1) + ' ', '\n' + alphabet[0] + ' '*space_length)
    else:
        tree = tree.replace(' ' + str(sorted_frequency.index(alphabet) + 1) + ' ', ' ' + alphabet[0] + ' ')
        tree = tree.replace(' ' + str(sorted_frequency.index(alphabet) + 1) + '\n', ' ' + alphabet[0] + '\n')
        tree = tree.replace('\n' + str(sorted_frequency.index(alphabet) + 1) + ' ', '\n' + alphabet[0] + ' ')


print("-----------------------------------------------------------------")
print('huffman tree graphical representation')
print('***We attemptend to draw the tree graphically too*** ')
print("-----------------------------------------------------------------")
print(tree)
