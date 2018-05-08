package comp9313.lab7

// the first step is to explicitly import the required spark classes into the my spark program

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
object Problem1 {

// creat a spark context object with the desired spark configuration that tells Apache Spark on how to access a cluster
  def main(args: Array[String]) {
  val inputFile = args(0)
  val outputFolder = args(1)
  val k = args(2).toInt

  val conf = new SparkConf().setAppName("Problem1").setMaster("local")
  val sc = new SparkContext(conf)
  val input = sc.textFile(inputFile)
  
  val words = input.map(_.toString().toLowerCase())
  val map_words = words.map(_.split("[\\s*$&#/\"'\\,.:;?!\\[\\](){}<>~\\-_]+"))

//  filter the x with the conditions: length >= 1 and x(0) is letter not digit
  val word_pairs = map_words.map( _.filter( x => x.length >=1 && x(0).isLetter))
  val distinct_pairs = word_pairs.map(_.distinct).flatMap (x => x).map(word=>(word,1))

//  map reduce process through sortBy and use map function to change the representation
  val word_reduce = distinct_pairs.reduceByKey(_+_)
  val word_top_k = word_reduce.sortBy(x=>(x._1)).take(k)
 
  val word_final = word_top_k.map(x=>x._1 + "\t" + x._2.toString())
  
  val rdd = sc.parallelize(word_final)

rdd.saveAsTextFile(outputFolder)
}
}
