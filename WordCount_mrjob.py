from mrjob.job import MRJob
import re
pattern = re.compile(r"[\w']+")

class wordCount(MRJob):    
    def mapper(self, _, line):
        for word in pattern.findall(line):
            yield word.lower(), 1

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    wordCount.run()
