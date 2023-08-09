from qgis import processing
import csv
import os

LakeDataIDPath = '/Users/dannyhagenlocker/Desktop/ICESat_Automation/LakeCrop.csv'
nameIndex = 0
lakeIDIndex = 1
xMinIndex = 2
xMaxIndex = 3
yMinIndex = 4
yMaxIndex = 5

with open(LakeDataIDPath, 'r') as file:
    LakeDataID = list(csv.reader(file, delimiter=','))
    LakeDataID = LakeDataID[1:47]
    for raster in LakeDataID:
        input = '/Users/dannyhagenlocker/Desktop/ICESat_Automation/CaliforniaTIF/CaliforniaWaterOccurrence.tif'
        output = '/Users/dannyhagenlocker/Desktop/ICESat_Automation/LakeTIFs/', raster[nameIndex], '_', raster[lakeIDIndex], '.tif'
        output = ''.join(output)
        outputVector = '/Users/dannyhagenlocker/Desktop/ICESat_Automation/LakeVectors/', raster[nameIndex], '_', raster[lakeIDIndex], '_Vectorized', '.shp'
        outputVector = ''.join(outputVector)
        boundingBox = raster[xMinIndex],',',raster[xMaxIndex],',',raster[yMinIndex],',',raster[yMaxIndex], ' [EPSG:4326]'
        boundingBox = ''.join(boundingBox)
        processing.run("gdal:cliprasterbyextent", {'INPUT': input,'PROJWIN': boundingBox, 'OVERCRS':False,'NODATA':None,'OPTIONS':'','DATA_TYPE':0,'EXTRA':'','OUTPUT': output})
        processing.run("gdal:polygonize", {'INPUT': output,'BAND':1,'FIELD':'DN','EIGHT_CONNECTEDNESS':False,'EXTRA':'','OUTPUT': outputVector})
        #print(output)
        #print(outputVector)
    
    #layer = iface.addVectorLayer(outputVector, '', 'ogr')
    #features = layer.getFeatures()
    #caps = layer.dataProvider.capabilities()
    #if caps & QgsVectorDataProvider.DeleteAttributes:
        #res = layer.dataProvider().deleteAttributes([0])
        #layer.updateFields()
    #if caps & QgsVectorDataProvider.AddAttributes:
    
    #km_area = QgsExpression('$area')
    #context = QgsExpressionContext()
    #context.appendScopes(\
    #QgsExpressionContextUtils.globalProjectLayerScopes(layer))
    
    #with edit(layer):
        #for f in layer.getFeatures():
            #context.setFeature(f)
            #f['area_KM2'] = km_area.evaluate(context)
            #layer.updateFeature(f)
        