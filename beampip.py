from __future__ import absolute_import

import argparse
import logging

from past.builtins import unicode
import apache_beam as beam
import apache_beam.transforms.window as window
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.combiners import ToListCombineFn


from apache_beam.io.gcp.internal.clients import bigquery

def find_msg(element):
        import re
        dictmsg = [eval(element)]
        return(dictmsg)
class FormDoFn(beam.DoFn):
      def process(self, element, window=beam.DoFn.WindowParam):
          return(element)

def run(argv=None):
  """Build and run the pipeline."""

  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--input_subscription', required=True,
      help='Input PubSub subscription of the form "projects/<project>/subscriptions/<subscription_name>".')
  parser.add_argument(
      '--output_table', required=True,
      help=
      ('Output BigQuery table for results specified as: PROJECT:DATASET.TABLE '
       'or DATASET.TABLE.'))
  known_args, pipeline_args = parser.parse_known_args(argv)

  with beam.Pipeline(argv=pipeline_args) as p:

    # Read the text from PubSub messages.
    lines = p | beam.io.ReadFromPubSub(subscription=known_args.input_subscription)
    transformed = (lines
                   | 'Split' >> (beam.FlatMap(find_msg))
                   | 'window' >> beam.WindowInto(window.FixedWindows(60))
                   | 'append' >> beam.CombineGlobally(ToListCombineFn()).without_defaults()
                   | 'Format' >> beam.ParDo(FormDoFn()))

    transformed | 'Write' >> beam.io.WriteToBigQuery(known_args.output_table)


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()

