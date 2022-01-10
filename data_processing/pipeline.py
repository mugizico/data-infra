import apache_beam as beam
import argparse
import logging
from typing import List


def parse_lines(row: str) -> List:
    return row.split(",")


class FmtInflationPct(beam.DoFn):
    """Beam Function to change the inflation
    from a float to a string formatted to 2 decimal points with %"""

    def process(self, element):
        inflation = float(element[9])
        country = element[2]
        crisis_status = element[-1]
        yield country, "{:.2f}".format(inflation) + "%", crisis_status


def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--output")
    args, pipeline_args = parser.parse_known_args(argv)
    table_spec = "africa_data.africa_crises"

    with beam.Pipeline(argv=pipeline_args) as p:
        lines = (
            p
            | "ReadCSVFile" >> beam.io.ReadFromText(args.input, skip_header_lines=1)
            | "ParseCSV" >> beam.Map(parse_lines)
        )

        fmt_inflation_lines = lines | "FormatInflationPct" >> beam.ParDo(
            FmtInflationPct()
        )
        # Write output to local file with a DirectRunner
        """
        fmt_inflation_lines | "WriteOutput" >> beam.io.WriteToText(
            args.output, file_name_suffix=".csv"
        )
        """

        # Write output to BigQuery with a DataflowRunner
        fmt_inflation_lines | "WriteOutput" >> beam.io.Write(
            beam.io.WriteToBigQuery(
                table_spec,
                schema="country:STRING,inflation_pct:STRING,crisis_status:STRING",
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
            )
        )


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    run()
