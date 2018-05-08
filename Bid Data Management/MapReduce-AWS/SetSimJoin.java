package comp9313.ass4;

import java.io.IOException;
import java.util.*;
//import java.util.Arrays;
//import java.util.List;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class SetSimJoin {

	public static class PairMapper extends Mapper<Object, Text, Text, Text> {
		
		
		private Text context_key = new Text();
		private Text context_value = new Text();
//		private Double tao = 0.85;
		
		/* utilize mapper to partition the prefix, by using the prefix filtering to decrease the running time;
		 */
		public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
			Configuration conf = context.getConfiguration();
			double tao = Double.parseDouble(conf.get("threshold"));
			
			
			String context_value_content = "";
	    	String value_string = value.toString();
			
//			System.out.println("value_string: " + value_string);
//			System.out.println("value_string_length: " + value_string.length());
			
			List<String> value_list = Arrays.asList(value_string.split(" "));
			
			System.out.println("value_list: " + value_list);
//			System.out.println("value_list_length: " + value_list.size());
//			System.out.println("rid: " + value_list.get(0));
//			System.out.println("");
//			List<String> value_list = Arrays.asList(value_string.split(" "));
			
			int length = value_list.size() - 1;
			List<String> element_List = value_list.subList(1, length + 1);
//			System.out.println("what: " + value_list.subList(1, length + 1).toString());
			
			/*
			 * prefix length caculation, also known as the prefix filtering;
			 */
			int prefix_length = length - ((int)Math.ceil(length * tao)) + 1;
			for (int i = 0; i < length; i++){
				context_value_content = context_value_content + "," + element_List.get(i);
			}
//			System.out.println("context_value_content: " + context_value_content);
			
			for(int j = 0; j < prefix_length; j++){
				context_key.set(element_List.get(j));
				String context_value_rid = value_list.get(0);
				String context_value_string = context_value_rid + context_value_content;
				context_value.set(context_value_string);
				context.write(context_key, context_value);
			}
		}		
	}


	public static class PairReducer extends Reducer<Text, Text, Text, DoubleWritable> {
//		 private Double tao = 0.85;
		 private Text output_key = new Text();
	     private DoubleWritable output_value = new DoubleWritable();
	     
//	     private Text output_temp = new Text();
	     
	     public void reduce(Text key, Iterable<Text> values,Context context) throws IOException, InterruptedException {
	    	 Configuration conf = context.getConfiguration();
			 double tao = Double.parseDouble(conf.get("threshold"));
//	    	 StringTokenizer itr1 = new StringTokenizer(values.toString());
//	    	 while (itr1.hasMoreTokens()) {
//	                String temp1 = itr1.nextToken();
//	                System.out.println("temp1: " + temp1.toString());
//	    	 }
	    	 List<String> storage_box = new ArrayList<String>();
	    	 
	    	 for (Text val:values) {
	    		 
	    		 storage_box.add(val.toString());
	    		 
//	    		 output.set(val);
	    		 System.out.println(val);
//	    		 context.write(key, output);
	    		 
	    		 System.out.println("storage_box: " + storage_box);
	    	 }
	    	 System.out.println("--------------------");
	    	 int length = storage_box.size();
	    	 /*
	    	  * use two for loop to loop around the whole storage_box;
	    	  */
	    	 for (int i=0; i<length; i++) {
	    	      String[] r1 = storage_box.get(i).split(",");
	    	      // System.out.ptintln("r1: " + r1.toString());
	    	      for (int j=1; j<length; j++){
	    	    	  if (i != j){
	    	        List<String> temp = new ArrayList<String>();
	    	        int count = 0;
	    	        String[] r2 = storage_box.get(j).split(",");
	    	        // System.out.ptintln("r2: " + r2.toString());
	    	        // if (r1 == r2) {
	    	        //   continue;
	    	        // }
	    	        for (int m = 1; m < r1.length; m++){
	    	          temp.add(r1[m]);
	    	        }
	    	        for (int n = 1; n < r2.length; n++){
	    	          if (temp.contains(r2[n])){
	    	            count ++;
	    	          }else{
	    	            temp.add(r2[n]);
	    	          }
	    	        }
	    	        /*
	    	         * sort the rid in ascending order, make sure left rid is smaller than the right one;
	    	         * if the similarity is smaller than the threshold, never keep the key value 
	    	         * pairs, which means they are not part of the candidate pairs.
	    	         */
	    	        if (Integer.parseInt(r1[0]) < Integer.parseInt(r2[0])){
	    	        	output_key.set("(" + r1[0] + "," + r2[0] + ")");
	    	        	if ((double)count/(double)temp.size() >= tao){
	    	        		output_value.set((double)count/(double)temp.size());
	    	    	        context.write(output_key, output_value);
	    	        	}
	    	        }else if (Integer.parseInt(r1[0]) > Integer.parseInt(r2[0])){
	    	        	output_key.set("(" + r2[0] + "," + r1[0] + ")");
	    	        	if ((double)count/(double)temp.size() >= tao){
	    	        		output_value.set((double)count/(double)temp.size());
	    	    	        context.write(output_key, output_value);
	    	        	}
	    	        }
//	    	        output_value.set((double)count/(double)temp.size());
//	    	        context.write(output_key, output_value);
//	    	    	}
//	    	        System.out.println("shit: " + r1[0] + " " + r2[0] + " " + (double)count/(double)temp.size());
	    	      }
	    	    }
	     }
	}
	}

	public static void main(String[] args) throws Exception {
		
		String input = args[0];
		String output = args[1];
		String threshold = args[2];
		int num = Integer.parseInt(args[3]);
		
		Configuration conf = new Configuration();
		conf.set("threshold", threshold);

		
		Job job = Job.getInstance(conf, "SetSimJoin");
		job.setNumReduceTasks(num);

		job.setJarByClass(SetSimJoin.class);
		job.setMapperClass(PairMapper.class);
		job.setReducerClass(PairReducer.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		FileInputFormat.addInputPath(job, new Path(input));
		FileOutputFormat.setOutputPath(job, new Path(output));
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
  }

