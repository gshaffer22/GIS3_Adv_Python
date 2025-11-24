# importing arcpy toolkit 
import arcpy

from arcpy.sa import *

# setting the correct workspace 
arcpy.env.workspace = r"R:\GEOG491_16440_FALL2025\Student_Data\gshaffer\Lab4\Ex10"

# setting up the three different rasters for each condition
# degree raster
degree_raster = arcpy.Raster("elevation")
# aspect raster 
aspect_raster = arcpy.Raster("elevation") 
# landcover raster
landcover_raster = arcpy.Raster("lc_recl") 

arcpy.env.overwriteOutput = True

# setting the requirements for degree raster
slope = Slope(degree_raster)
moderate_slope = (slope > 5) & (slope < 20)
# saving the final slope 
moderate_slope.save(r"R:\GEOG491_16440_FALL2025\Student_Data\gshaffer\Lab4\Ex10\degree.tif")

# setting the requirements for the aspect raster 
aspect = Aspect(aspect_raster) 
southerly_aspect = (aspect > 150) & (aspect < 270)
# saving the final aspect raster
southerly_aspect.save(r"R:\GEOG491_16440_FALL2025\Student_Data\gshaffer\Lab4\Ex10\aspect.tif")

# setting the requiements for the landcover raster
land_types = (landcover_raster == 1) | (landcover_raster == 2) | (landcover_raster == 3)
land_types.save(r"R:\GEOG491_16440_FALL2025\Student_Data\gshaffer\Lab4\Ex10\land_reclass.tif")

# combining the three rasters 
final_raster = moderate_slope * southerly_aspect * land_types


