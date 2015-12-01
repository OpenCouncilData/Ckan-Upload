import argparse, ckanapi

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        self.exit(2)

parser = MyParser(description='Uploads a file to update an existing resource in data.gov.au or other CKAN portal.',
    epilog="Source code and issues: https://github.com/OpenCouncilData/Ckan-Upload")
parser.add_argument('--apikey', required=True, help='Your API key for the portal. Find this on your data.gov.au user page.')
parser.add_argument('--resource', required=True, help='URL of the resource to update (eg http://data.gov.au/dataset/geelong-drain-pipes/resource/970d4dfd-4313-45ee-be9a-6b69b47483f1)')
parser.add_argument('filename', help='The file that will be uploaded in place of the existing resource.')

try:
    args = parser.parse_args()
except:
    parser.print_help()
    raise SystemExit

server = args.resource.split('/dataset')[0]
resourceid = args.resource.split('/')[-1]

print "Connecting to %s to update resource ID %s" % (server, resourceid)
ckan = ckanapi.RemoteCKAN(server, apikey=args.apikey,user_agent='opencouncildata testing')

resourceinfo = ckan.action.resource_show(id=resourceid)
print "Uploading %s to \"%s\". (Previously modified at %s)" % (args.filename, resourceinfo["name"], resourceinfo["last_modified"])
ckan.action.resource_update(id=resourceid,upload=open(args.filename), format=resourceinfo["format"])