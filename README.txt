<--A simple Tweet Parser-->
===============================================================================
To run the program, use the following syntax:
  python3 main.py <input_file>

For example:
  python3 main.py tweets.json
===============================================================================
The input files must pe placed in the src/resources/input/ folder.
However, when running the program, only the name file must be specified
(the program will look for the input file in the src/resources/input/ folder).

The program accepts input files that uses .json of .txt formats. The input file
can contain either a tweet per line, if it is a .txt file, or tweets stored in
JSON format (it does no matter whether it is a .txt or a .json file, it sees
that the content is JSON styled).

If the input file contains tweets, stored line by line, it is recommended that
the first tweet should not start with the character '{'. The program uses this
character to check if the content is JSON styled in a .txt file.

For tweets stored in JSON format, the standard tweet style is the one found at:
https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview
===============================================================================
The output is presented in bot TXT and JSON format. The output contains two
files, one that contains each of the words found in the input file, with its
number of appearances in its origin tweet and its number of appearances in the
whole input file (It searches all the tweets).
  For example: Created 1 2
The second file contains the median amount of unique words for all tweets,
where a word is unique if it appeared only once in its home tweet, and also the
median amount of unique words for all tweets, where a word is unique if it
appeared only once in the whole input file.
  For example:  The median amount of unique words (for words unique in their
                own tweet): 4.5
                The median amount of unique words (for words unique among all
                the tweets): 1.0
Then, the output is also presented in JSON format, for simpler further
utilisation.
===============================================================================
Implemented By Claudiu Mihai Jechel
