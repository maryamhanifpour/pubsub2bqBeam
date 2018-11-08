# pubsub2bqBeam

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
