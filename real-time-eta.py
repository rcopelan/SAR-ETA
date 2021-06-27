from sartopo_python import SartopoSession
import time

sts2=SartopoSession(
    "sartopo.com",
    "27CC",
    configpath="eta.cfg",
    account="robert@atsar.org")
    
fid2=sts2.addFolder("MyOnlineFolder")
sts2.addMarker(39,-120,"onlineStuff")
sts2.addMarker(39.01,-119.99,"onlineStuff2",folderId=fid2)
r2=sts2.getFeatures("Marker")
print("return value from getFeatures('Marker'):")
print(json.dumps(r2,indent=3))
time.sleep(15)
print("moving online after a pause:"+r2[0]['id'])
sts2.addMarker(39.02,-119.98,r2[0]['properties']['title'],existingId=r2[0]['id']) 
