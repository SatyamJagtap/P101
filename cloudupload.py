
import dropbox

class TransferData:

    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_file(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(filefrom,'rb')
        dbx.files_upload(f.read(),fileto)
    
def main():
    access_token = "sl.BFkb14lcGIt6aaXXDwPWXNw8dkDIxSPZal2AAfQegFRVQ-BNMcM7VX1QX_EvXRuo5a9y-Nma4NbeDPePNsKbC-yWqGlcQMkacMVK-8kETjWY80gMvSyy1eklOiYUgA5SUg_rY9zeN9KN"
    transferData = TransferData(access_token)
    filefrom = input("enter the file path to transfer:")
    fileto = input("enter the file path to upload to dropbox:")
    transferData.upload_file(filefrom,fileto)
    print("File has been moved.")

main()