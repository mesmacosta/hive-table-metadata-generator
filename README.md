# hive-table-metadata-generator

To test some Hive capabilities, it’s good to have a good number of tables with different complex column types inside the Hive metastore. This script generates random metadata for the Hive metastore.

## Activate your virtualenv if it’s not up
`source ./env/bin/activate`

## Install the requirements for the metadata generator
`pip install -r requirements.txt`

If you receive an error when installing the requirements, run:

`sudo apt-get install python-dev libsasl2-dev gcc`

`sudo apt-get install sasl2-bin libsasl2-2 libsasl2-dev libsasl2-modules`

Then run the install requirements again

## Run the script
`python hive_metastore_metadata_generator.py`
