package comp9313.lab7

// the first step is to explicitly import the required spark classes into the my spark program
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object Problem2 {
  
// creat a spark context object with the desired spark configuration that tells Apache Spark on how to access a cluster  
  def main(args: Array[String]) {
  val inputFile = args(0)
  val outputFolder = args(1)
  val conf = new SparkConf().setAppName("Problem2").setMaster("local")
  val sc = new SparkContext(conf)
  val input = sc.textFile(inputFile)

// use map function to change the line representation to (key, value)
  val pair = input.map(line => line.split("\t")).map(x=>(x(1).toString().toInt,x(0).toString().toInt))

//  use mapValues method to change to string, filter and delete the spacing
  val group = pair.groupByKey().mapValues(x=>x.toList)
//  group.foreach(println)
//  use method toList, toString, toInt to with the partition function to change the value part to 
//  Int type, then use map function to convert the key type from string to Int type, for the future sorting.
//  group_change.foreach(println)
  val sort = group.mapValues(_.sorted).sortByKey()

  val sort_list = sort.mapValues(_.mkString(","))

  val rdd = sort_list.map(x=>x._1.toString() + "\t" + x._2)
rdd.saveAsTextFile(outputFolder)
}
}
