from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Word count")
sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")
text = sc.textFile("/data/books/*txt") \
       .flatMap(lambda line: line.split())
counts = text.map(lambda word: (word.lower(), 1)) \
         .groupByKey() \
         .map(lambda p: (p[0], sum(p[1])))
counts.saveAsTextFile('/user/group18/wordcount_spark')
