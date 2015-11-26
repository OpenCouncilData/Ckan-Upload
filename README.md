## Ckan-Upload

This simple command-line tool automates the process of updating an existing resource (file) in a CKAN based repository such as data.gov.au or data.vic.gov.au. It is intended to allow councils to automate the regular updating of data.

Developed by Steve Bennett, as part of the OpenCouncilData toolkit funded by MAV Technology, and released under the MIT License.

Pre-requisites: Python, Pip, Git

### Installation:

```
git clone https://github.com/OpenCouncilData/Ckan-Upload
cd Ckan-Upload
pip install ckanapi argparse
```

### Usage:

1. Get your API key by going to your user account page in data.gov.au. It is a string of numbers and letters with hyphens.
2. Go to the page of the resource (file within a dataset) that you wish to update, and copy the whole URL. *For instance: http://data.gov.au/dataset/geelong-drain-pipes/resource/970d4dfd-4313-45ee-be9a-6b69b47483f1*
3. Export the file that you want to upload to somewhere on disk.
4. Now run:

```
python ckan-upload.py --key YOURAPIKEYHERE  --resource http://YOURRESOURCEURLHERE /path/to/MYFILE.csv
```