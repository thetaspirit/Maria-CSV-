import csv
import os

HEADER = [
  "id",
  "week",
  "center_id",
  "meal_id",
  "checkout_price",
  "base_price",
  "emailer_for_promotion",
  "homepage_featured",
  "num_orders"
  ]

def write_to_file(row):
    """
    Writes one row to a file, depending on its center_id.
    The row parameter should be a dictionary, with keys that match HEADER.
    """

    filename = str(row["center_id"]) + '.csv'

    # CREATING FILES AND WRITING HEADERS IF THEY DON'T ALREADY EXIST

    # Writing header to individual csv file
    if not os.path.exists(filename):
        with open(filename) as file:
            csv.DictWriter(file, fieldnames=HEADER, quoting=csv.QUOTE_NONNUMERIC).writeheader()
            file.close()

    # WRITING THE DATA

    with open(filename) as file:
        csv.DictWriter(file, fieldnames=HEADER, quoting=csv.QUOTE_NONNUMERIC).writerow(row)
        file.close()