# syntax-project-with-SpaCy

The idea is to write a program in Python 3 that can be executed with the command :
  ```
    python program.py text_file
  ```
   
(where text_file is a pure text file in French, encoded in utf-8), and which parses the text with spaCy and produces a file named "verbs" which contains one line for each verbal lemma observed in the text file, with the following information :
1. The number of occurrences of the verbal lemma in the text file (raw frequency)
2. The verbal lemma itself (the infinitive form of the verb)
3. Rounded percentages of the types of verb complements. The following UD v2 dependency types are considered: "obj", "iobj", "obl", "ccomp", and "xcomp". Example: if the verb "to say" is observed 20 times in the corpus, and has a complement type "obj" 12 times, then the percentage of the dependency type "obj" for this verb is 60.
Use the fr_sequoia-ud-dev.txt file included in the directory as an example input file. In the output file, the verbs should be sorted in descending order of frequency. The display format is given by the following sample extract :
![example]()
which indicates for example that the verb "to follow" has a direct object complement (obj) in 64% of the 16 cases found. Note that it is possible to get "percentages" higher than 100 due to spaCy analysis errors, which can produce several complements of the same type for the same verb. Also, some of the verbal lemmas found by spaCy may be incorrect.
