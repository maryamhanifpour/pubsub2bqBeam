# pubsub2bqBeam


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
