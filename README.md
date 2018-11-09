Apache Beam pipeline to deliver messages accumulated in pubsub to bigquery.

publish.py: Use it to publish test data to a pubsub topic.

beampip.py: Use it to to deliver messages accumalted in pubsub to a bigquery table by mnaking a dataflow template.

To make a Dataflow template:

python beampip.py \
   --runner DataflowRunner \
   --staging_location gs://<> \
   --temp_location gs://<> \
   --template_location gs://<> \
   --project <> \
   --input_subscription <> \
   --output_table <> \
   --streaming
   
   
   
![alt text](https://github.com/maryamhanifpour/pubsub2bqBeam/blob/master/beampip.PNG)


Cons: 
1. The safest way to close the running pipeline is via another API to Drain the specific pipeline.
2. Still streaming inserts to Bigquery unless using Java SDK.
3. Python SDK does not support  dynamic destinations, this is useful if some inputs are bad and cannot be processed, bad input should be written to another destination as dead letter.
