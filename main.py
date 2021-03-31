import sys
import json
import statistics
from colorama import Fore, Style


def validateArguments(args):
    print('Validating request ...\n')
    # checks if the number of arguments is equal to 2
    # if not, the program exits
    if len(args) != 2:
        print("Invalid operation!")
        print("Try: python3 main.py <input file>")
        sys.exit()


def removePunctuation(arr):
    # removes punctuation from all the strings stored in an array
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

    for i in range(len(arr)):
        for c in arr[i]:
            if c in punc:
                arr[i] = arr[i].replace(c, "")


def splitLinesIntoWords(arr):
    # takes an array of strings,
    # separates each string into words,
    # appends them into a new array of strings
    # appends all the new arrays into one big array of arrays, and returns it
    tweets = []

    for a in arr:
        if a != '\n':
            ws = a.split()
            tweets.append(ws)

    return tweets

###############################################################################

# Validate command line arguments
validateArguments(sys.argv)

# paths to input/output folders
input_path_folder = 'resources/input/'
output_path_folder = 'resources/output/'

# path to the input file
input_file = input_path_folder + sys.argv[1]
print('Input file: ' + input_file + '\n')

# paths to the output files
output_file_words_txt = output_path_folder + 'words.txt'
output_file_median_txt = output_path_folder + 'median.txt'
output_file_words_json = output_path_folder + 'words.json'
output_file_median_json = output_path_folder + 'median.json'
print(
    'Output file (words in simple text format): ' +
    Fore.YELLOW +
    output_file_words_txt +
    Style.RESET_ALL)
print(
    'Output file (median in simple text format): ' +
    Fore.YELLOW +
    output_file_median_txt +
    Style.RESET_ALL)
print(
    'Output file (words in json format): ' +
    Fore.YELLOW +
    output_file_words_json +
    Style.RESET_ALL)
print(
    'Output file (median in json format): ' +
    Fore.YELLOW +
    output_file_median_json +
    Style.RESET_ALL + '\n')

# reading the file content line by line
file1 = open(input_file, 'r')
lines = file1.readlines()
file1.close()

print('Converting tweets into words ...\n')

# used for storing tweets
tweets = []

# if { is found at the first position in the first line,
# than the input is JSON format
if lines[0][0] == '{':
    # reading the input in JSON format
    with open(input_file) as json_file:
        # read input file
        data = json.load(json_file)
        # closing input file
        json_file.close()

    lines = []
    # getting only the text from each tweet
    for p in data['tweets']:
        lines.append(p['text'])

    # split each tweet into words
    tweets = splitLinesIntoWords(lines)
else:
    lines = []
    # read input file
    file1 = open(input_file, 'r')
    lines = file1.readlines()

    # split each tweet into words
    tweets = splitLinesIntoWords(lines)

print('Removing punctuation ...\n')

# remove punctuation
for tweet in tweets:
    removePunctuation(tweet)

print('Counting words ...\n')

# stores the number of appeareances of each word in its own tweet
words_count_per_tweet = []
# stores the number of appeareances of each word in the whole input file
words_count_overall = []

for tweet in tweets:
    app = []
    app_overall = []

    for word in tweet:
        # count the number of appeareances of each word in its own tweet
        app.append(tweet.count(word))

        # count the number of appeareances of each word in the whole input file
        count_s = 0
        for t in tweets:
            count_s += t.count(word)

        app_overall.append(count_s)

    words_count_per_tweet.append(app)
    words_count_overall.append(app_overall)

print('Counting unique words ...\n')

# stores the number of unique values for each tweet
# where a word is unique if it appears only once in its tweet
unique_count = []
# stores the number of unique values for each tweet,
# where a word is unique if it appears only once in the whole document
unique_count_overall = []

for i in range(len(tweets)):
    unique_count.append(words_count_per_tweet[i].count(1))
    unique_count_overall.append(words_count_overall[i].count(1))

# sorting both arrays for calculating the median
unique_count.sort()
unique_count_overall.sort()

print('Calculating the median ...\n')

# calculating the median
median = statistics.median(unique_count)
median_overall = statistics.median(unique_count_overall)

print(
    'Writing in ' +
    Fore.YELLOW +
    output_file_words_txt +
    Style.RESET_ALL +
    '...\n')

# opens the output file
f = open(output_file_words_txt, "w")

# this is the way the words are printed
f.write(
    'Word || ' +
    'No. of appearances in the same tweet || ' +
    'No. of appearances in all tweets' +
    '\n')

for i in range(len(tweets)):
    for j in range(len(tweets[i])):
        f.write(
            tweets[i][j] +
            ' ' +
            str(words_count_per_tweet[i][j]) +
            ' ' +
            str(words_count_overall[i][j]) +
            '\n')

# closing the output file
f.close()

print(
    'Writing in ' +
    Fore.YELLOW +
    output_file_median_txt +
    Style.RESET_ALL +
    '...\n')

# opens the output file
f = open(output_file_median_txt, "w")

f.write(
    'The median amount of unique words ' +
    '(for words unique in their own tweet): ' +
    str(median) + '\n')
f.write(
    'The median amount of unique words ' +
    '(for words unique among all the tweets): ' +
    str(median_overall) +
    '\n')

# closing the output file
f.close()

print('Converting words into JSON format ...')

# converting the data into JSON format
data = {}
data['words'] = []

for i in range(len(tweets)):
    for j in range(len(tweets[i])):
        data['words'].append({
            'word': word,
            'app': words_count_per_tweet[i][j],
            'overallApp': words_count_overall[i][j]
        })

print(
    'Writing in ' +
    Fore.YELLOW +
    output_file_words_json +
    Style.RESET_ALL +
    '...\n')

# writing the data to a .json file
with open(output_file_words_json, 'w') as outfile:
    json.dump(data, outfile)

# closing the output file
outfile.close()

print('Converting median into JSON format ...')

# converting the data into JSON format
data = {}
data['medians'] = []
data['medians'].append({
    'median': median,
    'median_overall': median_overall,
})

print(
    'Writing in ' +
    Fore.YELLOW +
    output_file_median_json +
    Style.RESET_ALL +
    '...\n')

# writing the data to a .json file
with open(output_file_median_json, 'w') as outfile:
    json.dump(data, outfile)

# closing the output file
outfile.close()

print(Fore.GREEN + 'Done.' + Style.RESET_ALL)
