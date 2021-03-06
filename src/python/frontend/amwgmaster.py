# This should probably move to packages/amwg but it is not actually used there; it is used by metadiags.py and the "classic" viewer
# This was generated from the NCAR-generated HTML pages for a full diags run
# It basically maps obssets to diags sets to vars. 

### TODO: Find NCEP link, copy ocean basin map

### This dictionary is used to create the classic view front page. The format is:
### preamble - any description before the plot links. Typically a summary/header of what the set is.
### desc: The description of the set, used by the front end web generator
### seasons: Which seasons are applicable to the page. Mostly used to determine how many "plot" columns need made
### NOTE: If you add a set, there is some code in core.js that needs updated to clear the page when switching between diagnostic sets. Grep for topten to find it.

amwgsets = {}
amwgsets['topten']={'preamble':'', 'desc':'Tier 1A Diagnostics', 'seasons':'NA'}
amwgsets['so']={'preamble':'', 'desc':'Tier 1B Diagnostics: Southern Ocean', 'seasons':'NA', 'regions':'Southern Ocean'}
amwgsets['testing']={'preamble':'', 'desc':'Testing region functionality', 'seasons':'NA', 'regions':'Southern Ocean'}
amwgsets['1'] ={'preamble': '', 'desc': 'Tables of ANN, DJF, JJA, global and regional means and RMSE.', 'seasons':'NA'}
amwgsets['2'] ={'preamble': '<p>The computation of the implied northward transports follows the conventions described in the paper by <a href="http://www.cgd.ucar.edu/cas/papers/jclim2001a/transpts.html">Trenberth and Caron (2001)</a>. Their corrections applied to the southern oceans poleward of 30S are not used in the calculations, and the NCEP derived values plotted here are their unadjusted values. Webpage about the NCEP derived data. A plot of the ocean basins used in the calculations.', 'desc': 'Line plots of annual implied northward transports.', 'seasons':'NA'}
amwgsets['3'] ={'preamble': '', 'desc': 'Line plots of DJF, JJA and ANN zonal means', 'seasons':['DJF', 'JJA', 'ANN']}
amwgsets['4'] ={'preamble': '', 'desc': 'Vertical contour plots of DJF, JJA and ANN zonal means', 'seasons':['DJF', 'JJA', 'ANN']}
amwgsets['4a']={'preamble': '', 'desc': 'Vertical (XZ) contour plots of DJF, JJA and ANN meridional means', 'seasons':['DJF', 'JJA', 'ANN']}
amwgsets['5'] ={'preamble': '', 'desc': 'Horizontal contour plots of DJF, JJA and ANN means', 'seasons':['DJF', 'JJA', 'ANN'] }
amwgsets['6'] ={'preamble': '', 'desc': 'Horizontal vector plots of DJF, JJA and ANN means', 'seasons':['DJF', 'JJA', 'ANN']} 
amwgsets['7'] ={'preamble': '', 'desc': 'Polar contour and vector plots of DJF, JJA and ANN means', 'seasons':['DJF', 'JJA', 'ANN']}
amwgsets['8'] ={'preamble': '', 'desc': 'Annual cycle contour plots of zonal means', 'seasons':['ANN']}
amwgsets['9'] ={'preamble': '', 'desc': 'Horizontal contour plots of DJF-JJA differences', 'seasons':'NA'}
amwgsets['10']={'preamble': '', 'desc': 'Annual cycle line plots of global means', 'seasons':['ANN']}
amwgsets['11']={'preamble': '', 'desc': 'Pacific annual cycle, Scatter plot plots', 'seasons':['ANN']}
amwgsets['12']={'preamble': '', 'desc': 'Vertical profile plots from 17 selected stations', 'seasons':'NA'}
amwgsets['13']={'preamble': '', 'desc': 'ISCCP cloud simulator plots ', 'seasons':'NA'} 
amwgsets['14']={'preamble': '<p>Taylor Diagrams were developed by Karl Taylor at PCMDI (<a href="http://www.agu.org/pubs/crossref/2001/2000JD900719.shtml">paper</a>|<a href="http://www-pcmdi.llnl.gov/publications/pdf/55.pdf">tech note</a>) and aim to condense information about variance and RMSE characteristics of a particular model run when compared with observations in a single diagram. The tables summarize the individual metrics for each variable considered including: <ul><br> <li>bias, as absolute percentage difference from observations <li>variance, as a ratio of the observed variance <li>correlation, correlation coefficient with observations </ul><p>', 'desc': 'Taylor Diagram plots ', 'seasons':'NA'}
amwgsets['15']={'preamble': '', 'desc': 'Annual Cycle at Select Stations plots', 'seasons':['ANN']}

### This dictionary is used to convert a full descriptive name of an obs set into the more minimal chunk of filename used for the obs set and for resultant PNGS
### These were taken from NCAR code
### Format is "long name":"short name" 
obsprefix={'GPCP 1979-2003 - Tropics': 'GPCP_TROP',
 'SMMR and SSM/I 1979-1999': 'SSMI',
 'NCEP Reanalysis 1979-98 - Tropics': 'NCEP_TROP',
 'NVAP 1988-1999': 'NVAP',
 'NVAP 1988-1999 - Tropics': 'NVAP_TROP',
 'North Slope of Alaska (NSA)': 'NSA',
 'ISCCP D2 1983-2001': 'ISCCP',
 'NA': 'N/A',
 'Tropical Western Pacific--Region 2 (TWP2)': 'TWP2',
 'CMAP (Xie-Arkin) 1979-98 - Tropics': 'XA_TROP',
 'ERA40 Reanalysis 1980-2001': 'ERA40',
 'PREC/L (CMAP) 1948-2001': 'PRECL',
 'ECMWF Reanalysis 1979-93': 'ECMWF',
 'SSM/I (Wentz) 1987-2000': 'SSMI',
 'CMAP (Xie-Arkin) 1979-98': 'XA',
 'Southern Great Plains (SGP)': 'SGP',
 'Legates and Willmott 1920-80': 'LEGATES',
 'HadISST/OI.v2 (Pre-Indust) 1870-1900': 'HADISST_PI',
 'CERES2 March 2000-October 2005': 'CERES2',
 'JRA25 Reanalysis 1979-04': 'JRA25',
 'ISCCP FD Jul1983-Dec2000': 'ISCCP',
 'ERBE Feb1985-Apr1989 - Tropics': 'ERBE_TROP',
 'MODIS Mar2000-Aug2004 - Tropics': 'MODIS_TROP',
 'SSM/I (Wentz) 1987-2000 - Tropics': 'SSMI_TROP',
 'TRMM (3B43) 1998-Feb2004 - Tropics': 'TRMM_TROP',
 'GPCP 1979-2003': 'GPCP',
 'Legates and Willmott 1920-80 - Tropics': 'LEGATES_TROP',
 'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': 'CLOUDSAT',
 'ERA40 Reanalysis 1980-2001 - Tropics': 'ERA40_TROP',
 'CERES 2000-2003': 'CERES',
 'IPCC/CRU Climatology 1961-90': 'CRU',
 'ERS Scatterometer 1992-2000': 'ERS',
 'Tropical Western Pacific--Region 3 (TWP3)': 'TWP3',
 'ISCCP D1 Daytime Jul1983-Sep2001': 'ISCCP',
 'Large-Yeager 1984-2004 - Tropics': 'LARYEA_TROP',
 'ERS Scatterometer 1992-2000 - Tropics': 'ERS_TROP',
 'JRA25 Reanalysis 1979-04 - Tropics': 'JRA25_TROP',
 'Large-Yeager 1984-2004': 'LARYEA',
 'Surface Heat Budget of the Arctic Ocean (SHEBA)': 'SHEBA',
 'NCEP Reanalysis 1979-98': 'NCEP',
 'CERES2 March 2000-October 2005 - Tropics': 'CERES2_TROP',
 'HadISST/OI.v2 (Present Day) 1999-2008': 'HADISST_PD',
 'TRMM (3B43) 1998-Feb2004': 'TRMM',
 'ERBE Feb1985-Apr1989': 'ERBE',
 'ECMWF Reanalysis 1979-93 - Tropics': 'ECMWF_TROP',
 'Willmott and Matsuura 1950-99': 'WILLMOTT',
 'Woods Hole OAFLUX 1958-2006': 'WHOI',
 'MODIS Mar2000-Aug2004': 'MODIS',
 'Tropical Western Pacific--Region 1 (TWP1)': 'TWP1',
 'HadISST/OI.v2 (Climatology) 1982-2001': 'HADISST',
 'AIRS IR Sounder 2002-06': 'AIRS',
 'Warren Cloud Surface OBS': 'WARREN',
 'CERES 2000-2003 - Tropics': 'CERES_TROP',
 'ERA Interim Reanalysis' : 'ERAI',
 'CERES-EBAF':'CERES-EBAF',
 'AOD Data': 'AOD_550'}


varinfo = {}

### This dictionary controls which variables belong in which diagnostics sets and which observation sets make sense for each variable. 
### The format is:
### 'desc': A description of the variable name. Used for generating row text in the plot set web pages
### 'obssets' A dictionary
###       The format is a long name (identical to one in obsprefix) and then a filekey and list of sets that variable is used in. 
###       Multiple entries are supported
### 'sets': A list of stringified sets this variable is used in. 
### Example:
### varinfo['PSL_SOUTH']={'desc': 'Sea-level pressure (Southern)', 'obssets': {'NCEP Reanalysis 1979-98': {'filekey': 'NCEP', 'usedin': ['7']}, 'JRA25 Reanalysis 1979-04': {'filekey': 'JRA25', 'usedin': ['7']}}, 'sets': ['7']}
### PSL_SOUTH is used in sets 7. In set 7, the NCEP Reanalysis 1979-98 set is used and has the shortname "NCEP" for the files. It is used in set 7. PSL_SOUTH is also used with the JRA25 Reanalysis 1979-84 obs set which is
### named JRA25 on disk

varinfo['PSL_SOUTH']={'desc':'Sea-level pressure (Southern)', 'sets': ['7'], 'obssets': {
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['7']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['7']}
}}
varinfo['TREFHT_NORTH']={'desc':'2-meter temperature (land) (Northern)', 'sets': ['7'], 'obssets': {
	'Willmott and Matsuura 1950-99': {
		'filekey': 'WILLMOTT', 'usedin': ['7']},
	'IPCC/CRU Climatology 1961-90': {
		'filekey': 'CRU', 'usedin': ['7']}
}}
varinfo['TS']={'desc':'Surface temperature', 'sets': ['5', '3', '10'], 'obssets': {
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['5', '3', '10']}
}}
varinfo['SHFLX_SOUTH']={'desc':'Surface sensible heat flux (Southern)', 'sets': ['7'], 'obssets': {
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['7']}
}}
varinfo['FSNTOAC']={'desc':'TOA clearsky new SW flux', 'sets': ['5', '3', '10'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['5', '3', '10']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['5', '3', '10']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['5', '3', '10']}
}}
varinfo['QFLX_SOUTH']={'desc':'Surface water flux (Southern)', 'sets': ['7'], 'obssets': {
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['7']}
}}
varinfo['CLDHGH_NORTH']={'desc':'High cloud amount (IR clouds) (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['7']}
}}
varinfo['FSNTOA_SOUTH']={'desc':'TOA net SW flux (Southern)', 'sets': ['7'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['7']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['TTRP']={'desc':'Tropopause temperature', 'sets': ['5'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['5']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['5']}
}}
varinfo['Z3_500_NORTH']={'desc':'500 mb geopotential height (Northern)', 'sets': ['7'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['7']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['7']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['7']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['7']}
}}
varinfo['FSNS']={'desc':'Surf Net SW flux', 'sets': ['5', '3', '10','so','testing'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10']},
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['5', '3', '10', 'so', 'testing']}
}}
varinfo['FLDS_SOUTH']={'desc':'Surf LW downwelling flux (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['CLDLOW_NORTH']={'desc':'Low cloud amount (IR clouds) (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'Warren Cloud Surface OBS': {
		'filekey': 'WARREN', 'usedin': ['7']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['7']}
}}
varinfo['ALBEDOC_SOUTH']={'desc':'TOA clearsky albedo (Southern)', 'sets': ['7'], 'obssets': {
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['TS_NORTH']={'desc':'Surface temperature (Northern)', 'sets': ['7'], 'obssets': {
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['7']}
}}
varinfo['TCLDAREA']={'desc':'Total cloud area (Day)', 'sets': ['5'], 'obssets': {
	'ISCCP D1 Daytime Jul1983-Sep2001': {
		'filekey': 'ISCCP', 'usedin': ['5']},
	'MODIS Mar2000-Aug2004': {
		'filekey': 'MODIS', 'usedin': ['5']}
}}
varinfo['T']={'desc':'Temperature', 'sets': ['4a', '4', '15', 'topten','so','testing'], 'obssets': {
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['4a', '4']},
	'ERAI Interim Reanalysis': {
		'filekey': 'ERAI', 'usedin': ['topten','so','testing']},
	'North Slope of Alaska (NSA)': {
		'filekey': 'NSA', 'usedin': ['15']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['4a', '4', 'testing']},
	'Tropical Western Pacific--Region 2 (TWP2)': {
		'filekey': 'TWP2', 'usedin': ['15']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['4a', '4']},
	'Tropical Western Pacific--Region 1 (TWP1)': {
		'filekey': 'TWP1', 'usedin': ['15']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']},
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['4a', '4']},
	'AIRS IR Sounder 2002-06': {
		'filekey': 'AIRS', 'usedin': ['4a', '4']},
	'Tropical Western Pacific--Region 3 (TWP3)': {
		'filekey': 'TWP3', 'usedin': ['15']}
}}
varinfo['PRECT_NORTH']={'desc':'Precipitation rate (Northern)', 'sets': ['7'], 'obssets': {
	'GPCP 1979-2003': {
		'filekey': 'GPCP', 'usedin': ['7']}
}}
varinfo['TGCLDLWP']={'desc':'Cloud liquid water', 'sets': ['5', '3', '10', '15'], 'obssets': {
	'Tropical Western Pacific--Region 1 (TWP1)': {
		'filekey': 'TWP1', 'usedin': ['15']},
	'Tropical Western Pacific--Region 3 (TWP3)': {
		'filekey': 'TWP3', 'usedin': ['15']},
	'North Slope of Alaska (NSA)': {
		'filekey': 'NSA', 'usedin': ['15']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']},
	'SSM/I (Wentz) 1987-2000 - Tropics': {
		'filekey': 'SSMI_TROP', 'usedin': ['5']},
	'Tropical Western Pacific--Region 2 (TWP2)': {
		'filekey': 'TWP2', 'usedin': ['15']},
	'NVAP 1988-1999 - Tropics': {
		'filekey': 'NVAP_TROP', 'usedin': ['5']},
	'SSM/I (Wentz) 1987-2000': {
		'filekey': 'SSMI', 'usedin': ['5', '3', '10']},
	'NVAP 1988-1999': {
		'filekey': 'NVAP', 'usedin': ['5', '3', '10']},
	'MODIS Mar2000-Aug2004': {
		'filekey': 'MODIS', 'usedin': ['5', '3']}
}}
varinfo['PS_NORTH']={'desc':'Surface pressure (Northern)', 'sets': ['7'], 'obssets': {
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['7']}
}}
varinfo['SURF_STRESS_TROP']={'desc':'Surface wind stress (ocean)', 'sets': ['6'], 'obssets': {
	'JRA25 Reanalysis 1979-04 - Tropics': {
		'filekey': 'JRA25_TROP', 'usedin': ['6']},
	'ERS Scatterometer 1992-2000 - Tropics': {
		'filekey': 'ERS_TROP', 'usedin': ['6']},
	'NCEP Reanalysis 1979-98 - Tropics': {
		'filekey': 'NCEP_TROP', 'usedin': ['6']},
	'Large-Yeager 1984-2004 - Tropics': {
		'filekey': 'LARYEA_TROP', 'usedin': ['6']}
}}
varinfo['CLDMED']={'desc':'Mid cloud amount (IR clouds)', 'sets': ['5', '3', '10'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['5', '3']}
}}
varinfo['FSDS']={'desc':'Surf SW downwelling flux', 'sets': ['5', '3', '10', '15'], 'obssets': {
	'Surface Heat Budget of the Arctic Ocean (SHEBA)': {
		'filekey': 'SHEBA', 'usedin': ['15']},
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10']},
	'Tropical Western Pacific--Region 2 (TWP2)': {
		'filekey': 'TWP2', 'usedin': ['15']},
	'Tropical Western Pacific--Region 1 (TWP1)': {
		'filekey': 'TWP1', 'usedin': ['15']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']},
	'Tropical Western Pacific--Region 3 (TWP3)': {
		'filekey': 'TWP3', 'usedin': ['15']},
	'North Slope of Alaska (NSA)': {
		'filekey': 'NSA', 'usedin': ['15']}
}}
varinfo['FSNTOA']={'desc':'TOA new SW flux', 'sets': ['5', '3', '10'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['5', '3', '10']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['5', '3', '10']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['5', '3', '10']}
}}
varinfo['CLDLOW']={'desc':'Low cloud amount (IR clouds)', 'sets': ['5', '3', '10'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10']},
	'Warren Cloud Surface OBS': {
		'filekey': 'WARREN', 'usedin': ['5', '3']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['5', '3']}
}}
varinfo['Z3_500_SOUTH']={'desc':'500 mb geopotential height (Southern)', 'sets': ['7'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['7']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['7']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['7']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['7']}
}}
varinfo['LHFLX']={'desc':'Surface latent heat flux', 'sets': ['5', '3', '10', '15','so'], 'obssets': {
	'Woods Hole OAFLUX 1958-2006': {
		'filekey': 'WHOI', 'usedin': ['5', '3', '10']},
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['5', '3', '10','so']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['5', '3']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['5', '3', '10']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']}
}}
varinfo['CLDMED_VISIR_NORTH']={'desc':'Mid cloud amount (VIS/IR/NIR) clouds) (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['MEANTAU']={'desc':'Mean cloud optical thickness (Day)', 'sets': ['5'], 'obssets': {
	'ISCCP D1 Daytime Jul1983-Sep2001': {
		'filekey': 'ISCCP', 'usedin': ['5']},
	'MODIS Mar2000-Aug2004': {
		'filekey': 'MODIS', 'usedin': ['5']}
}}
varinfo['SWCF']={'desc':'TOA shortwave cloud forcing', 'sets': ['5', '3', '9', '10', 'topten','so','testing'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['5', '3', '9', '10']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['5', '3', '9', '10']},
	'CERES_EBAF': {
		'filekey': 'CERES-EBAF', 'usedin': ['topten','so','testing']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['5', '3', '9', '10']}
}}
varinfo['ALBEDO']={'desc':'TOA Albedo', 'sets': ['5', '10'], 'obssets': {
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['5', '10']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['5', '10']}
}}
varinfo['SWCF_TROP']={'desc':'TOA shortwave cloud forcing', 'sets': ['5'], 'obssets': {
	'ERBE Feb1985-Apr1989 - Tropics': {
		'filekey': 'ERBE_TROP', 'usedin': ['5']},
	'CERES2 March 2000-October 2005 - Tropics': {
		'filekey': 'CERES2_TROP', 'usedin': ['5']},
	'CERES 2000-2003 - Tropics': {
		'filekey': 'CERES_TROP', 'usedin': ['5']}
}}
varinfo['FLDSC_SOUTH']={'desc':'Clearsky Surf LW downwelling flux (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['MEANTTOP']={'desc':'Mean cloud top temperature (Day)', 'sets': ['5'], 'obssets': {
	'ISCCP D1 Daytime Jul1983-Sep2001': {
		'filekey': 'ISCCP', 'usedin': ['5']},
	'MODIS Mar2000-Aug2004': {
		'filekey': 'MODIS', 'usedin': ['5']}
}}
varinfo['PRECT_TROP']={'desc':'Tropical Precipitation rate', 'sets': ['5'], 'obssets': {
	'TRMM (3B43) 1998-Feb2004': {
		'filekey': 'TRMM_TROP', 'usedin': ['5']},
	'Legates and Willmott 1920-80 - Tropics': {
		'filekey': 'LEGATES_TROP', 'usedin': ['5']},
	'CMAP (Xie-Arkin) 1979-98 - Tropics': {
		'filekey': 'XA_TROP', 'usedin': ['5']},
	'GPCP 1979-2003 - Tropics': {
		'filekey': 'GPCP_TROP', 'usedin': ['5']},
	'SSM/I (Wentz) 1987-2000 - Tropics': {
		'filekey': 'SSMI_TROP', 'usedin': ['5']}
}}
varinfo['FSDSC_SOUTH']={'desc':'Clearsky Surf SW downwelling flux (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['FLDS_NORTH']={'desc':'Surf LW downwelling flux (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['FSNSC_NORTH']={'desc':'Clearsky Surf Net SW flux (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['FSDS_SOUTH']={'desc':'Surf SW downwelling flux (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['RESTOA']={'desc':'TOA residual energy flux', 'sets': ['10'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['10']}
}}
varinfo['SHFLX_NORTH']={'desc':'Surface sensible heat flux (Northern)', 'sets': ['7'], 'obssets': {
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['7']}
}}
varinfo['CLDHGH']={'desc':'High cloud amount (IR clouds)', 'sets': ['5', '3', '10'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['5', '3']}
}}
varinfo['SHFLX']={'desc':'Surface sensible heat flux', 'sets': ['5', '3', '10', '15', 'so', 'testing'], 'obssets': {
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['5', '3', '10']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['5', '3', '10']},
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['5', '3', '10', 'so', 'testing']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']}
}}
varinfo['PS_SOUTH']={'desc':'Surface pressure (Southern)', 'sets': ['7'], 'obssets': {
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['7']}
}}
varinfo['FLNSC']={'desc':'Clearsky Surf Net LW Flux', 'sets': ['5', '3'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['5', '3']}
}}
varinfo['CLDHGH_SOUTH']={'desc':'High cloud amount (IR clouds) (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['7']}
}}
varinfo['FSNSC_SOUTH']={'desc':'Clearsky Surf Net SW flux (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['ALBEDOC_NORTH']={'desc':'TOA clearsky albedo (Northern)', 'sets': ['7'], 'obssets': {
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['ALBEDOC']={'desc':'TOA clearsky albedo', 'sets': ['5', '10'], 'obssets': {
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['5', '10']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['5', '10']}
}}
varinfo['ICEFRAC_SOUTH']={'desc':'Sea-ice area (Southern)', 'sets': ['10', '7'], 'obssets': {
	'SMMR and SSM/I 1979-1999': {
		'filekey': 'SSMI', 'usedin': ['10', '7']},
	'HadISST/OI.v2 (Climatology) 1982-2001': {
		'filekey': 'HADISST', 'usedin': ['10', '7']}
}}
varinfo['RELHUM']={'desc':'Relative humidity', 'sets': ['4a', '4', 'topten', 'testing'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['4a', '4']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['4a', '4']},
	'AIRS IR Sounder 2002-06': {
		'filekey': 'AIRS', 'usedin': ['4a', '4']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['4a', '4', 'testing']},
	'ERAI Interim Reanalysis': {
		'filekey': 'ERAI', 'usedin': ['topten']}
}}
varinfo['EP']={'desc':'Evaporation - precipitation', 'sets': ['5', '10'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['5', '10']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['10']}
}}
varinfo['QFLX']={'desc':'Surface water flux', 'sets': ['5', '3', '10', 'so','testing'], 'obssets': {
	'Woods Hole OAFLUX 1958-2006': {
		'filekey': 'WHOI', 'usedin': ['5', '3', '10']},
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['5', '3', '10']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['10']},
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['5', '3', '10', 'so','testing']}
}}
varinfo['PSL']={'desc':'Sea-level pressure', 'sets': ['5', '3', '9', '10', 'topten'], 'obssets': {
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['5', '3', '10']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['5', '3', '9', '10']},
	'ERAI Interim Reanalysis': {
		'filekey': 'ERAI', 'usedin': ['topten']}
}}
varinfo['CLDTOT_VISIR_NORTH']={'desc':'Total cloud amount (VIS/IR/NIR) clouds) (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['SST']={'desc':'Sea surface temperature', 'sets': ['5', '10'], 'obssets': {
	'HadISST/OI.v2 (Present Day) 1999-2008': {
		'filekey': 'HADISST_PD', 'usedin': ['5']},
	'HadISST/OI.v2 (Pre-Indust) 1870-1900': {
		'filekey': 'HADISST_PI', 'usedin': ['5']},
	'HadISST/OI.v2 (Climatology) 1982-2001': {
		'filekey': 'HADISST', 'usedin': ['5', '10']}
}}
varinfo['FLNS']={'desc':'Surf Net LW flux', 'sets': ['5', '3', '10'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10']},
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['5', '3', '10']}
}}
varinfo['ICEFRAC_NORTH']={'desc':'Sea-ice area (Northern)', 'sets': ['10', '7'], 'obssets': {
	'SMMR and SSM/I 1979-1999': {
		'filekey': 'SSMI', 'usedin': ['10', '7']},
	'HadISST/OI.v2 (Climatology) 1982-2001': {
		'filekey': 'HADISST', 'usedin': ['10', '7']}
}}
varinfo['CLDLOW_VISIR']={'desc':'Low cloud amount (VIS/IR/NIR clouds)', 'sets': ['5', '3', '10'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10']}
}}
varinfo['PRECT']={'desc':'Precipitation rate', 'sets': ['5', '3', '8', '9', '10', '15', 'topten', 'so', 'testing'], 'obssets': {
	'CMAP (Xie-Arkin) 1979-98': {
		'filekey': 'XA', 'usedin': ['5', '3', '8', '9', '10']},
	'GPCP 1979-2003': {
		'filekey': 'GPCP', 'usedin': ['5', '3', '8', '9', '10', 'topten', 'so', 'testing']},
	'Legates and Willmott 1920-80': {
		'filekey': 'LEGATES', 'usedin': ['5', '3', '10']},
	'TRMM (3B43) 1998-Feb2004': {
		'filekey': 'TRMM', 'usedin': ['3', '10']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']},
	'SSM/I (Wentz) 1987-2000': {
		'filekey': 'SSMI', 'usedin': ['5', '3', '10']}
}}
varinfo['PRECT_LAND']={'desc':'Precipitation rate (land)', 'sets': ['5'], 'obssets': {
	'PREC/L (CMAP) 1948-2001': {
		'filekey': 'PRECL', 'usedin': ['5']}
}}
varinfo['PRECIP']={'desc':'Cumulative precipitation (land)', 'sets': ['5'], 'obssets': {
	'Willmott and Matsuura 1950-99': {
		'filekey': 'WILLMOTT', 'usedin': ['5']}
}}
varinfo['TMQ']={'desc':'Precipitable Water', 'sets': ['15'], 'obssets': {
	'North Slope of Alaska (NSA)': {
		'filekey': 'NSA', 'usedin': ['15']},
	'Tropical Western Pacific--Region 1 (TWP1)': {
		'filekey': 'TWP1', 'usedin': ['15']},
	'Tropical Western Pacific--Region 2 (TWP2)': {
		'filekey': 'TWP2', 'usedin': ['15']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']},
	'Tropical Western Pacific--Region 3 (TWP3)': {
		'filekey': 'TWP3', 'usedin': ['15']}
}}
varinfo['LWCF']={'desc':'TOA longwave cloud forcing', 'sets': ['5', '3', '9', '10', 'topten', 'so'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['5', '3', '9', '10']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['5', '3', '9', '10']},
	'CERES_EBAF': {
		'filekey': 'CERES-EBAF', 'usedin': ['topten', 'so']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['5', '3', '9', '10']}
}}
varinfo['FLDS']={'desc':'Surf LW downwelling flux', 'sets': ['5', '3', '10', '15', 'so'], 'obssets': {
	'Surface Heat Budget of the Arctic Ocean (SHEBA)': {
		'filekey': 'SHEBA', 'usedin': ['15']},
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10', 'so']},
	'Tropical Western Pacific--Region 2 (TWP2)': {
		'filekey': 'TWP2', 'usedin': ['15']},
	'Tropical Western Pacific--Region 1 (TWP1)': {
		'filekey': 'TWP1', 'usedin': ['15']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']},
	'Tropical Western Pacific--Region 3 (TWP3)': {
		'filekey': 'TWP3', 'usedin': ['15']},
	'North Slope of Alaska (NSA)': {
		'filekey': 'NSA', 'usedin': ['15']}
}}
varinfo['T_200']={'desc':'200 mb temperature', 'sets': ['5', '10'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['5', '10']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['5', '10']},
	'AIRS IR Sounder 2002-06': {
		'filekey': 'AIRS', 'usedin': ['5', '10']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['5', '10']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['5', '10']}
}}
varinfo['FLDSC_NORTH']={'desc':'Clearsky Surf LW downwelling flux (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['SWCFSRF']={'desc':'Surf SW Cloud Forcing', 'sets': ['5', '3'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['5', '3']}
}}
varinfo['FLDSC']={'desc':'Clearsky Surf LW downwelling flux', 'sets': ['5', '3'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['5', '3']}
}}
varinfo['CLDLOW_SOUTH']={'desc':'Low cloud amount (IR clouds) (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'Warren Cloud Surface OBS': {
		'filekey': 'WARREN', 'usedin': ['7']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['7']}
}}
varinfo['TS_SOUTH']={'desc':'Surface temperature (Southern)', 'sets': ['7'], 'obssets': {
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['7']}
}}
varinfo['Z3_500']={'desc':'500 mb geopotential height', 'sets': ['5', '10'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['5', '10']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['5', '10']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['5', '10']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['5', '10']}
}}
varinfo['OMEGA']={'desc':'Pressure vertical velocity', 'sets': ['4a', '4', 'testing'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['4a', '4']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['4a', '4']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['4a', '4']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['4a', '4', 'testing']}
}}
varinfo['FLUT']={'desc':'TOA upward LW flux', 'sets': ['5', '3', '8', '10'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['5', '3', '8', '10']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['5', '3', '8', '10']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['5', '3', '8', '10']}
}}
varinfo['FLUT_NORTH']={'desc':'TOA upward LW flux (Northern)', 'sets': ['7'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['7']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['TREFHT_SOUTH']={'desc':'2-meter temperature (land) (Southern)', 'sets': ['7'], 'obssets': {
	'Willmott and Matsuura 1950-99': {
		'filekey': 'WILLMOTT', 'usedin': ['7']}
}}
varinfo['TREFHT']={'desc':'2-meter air temperature (land)', 'sets': ['5', '3', '9', '10', 'topten', 'testing'], 'obssets': {
	'Willmott and Matsuura 1950-99': {
		'filekey': 'WILLMOTT', 'usedin': ['5', '3', '10', 'topten', 'testing']},
	'Legates and Willmott 1920-80': {
		'filekey': 'LEGATES', 'usedin': ['5', '3', '9', '10']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['9']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['5', '3', '10']},
	'IPCC/CRU Climatology 1961-90': {
		'filekey': 'CRU', 'usedin': ['5', '3']}
}}
varinfo['AODVIS']={'desc':'Aerosol optical depth', 'sets': ['topten', 'so'], 'obssets': {
	'AOD_550': {
		'filekey': 'sat', 'usedin': ['topten', 'so']}
}}
varinfo['CLDLOW_VISIR_NORTH']={'desc':'Low cloud amount (VIS/IR/NIR) clouds) (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['Atmospheric_heat']={'desc':'Atmospheric Heat', 'sets': ['2'], 'obssets': {
	'N/A': {
		'filekey': 'NA', 'usedin': ['2']}
}}
varinfo['FSDSC']={'desc':'Clearsky Surf SW downwelling flux', 'sets': ['5', '3'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['5', '3']}
}}
varinfo['QFLX_NORTH']={'desc':'Surface water flux (Northern)', 'sets': ['7'], 'obssets': {
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['7']}
}}
varinfo['SURF_WIND_SOUTH']={'desc':'Near surface wind (Southern)', 'sets': ['7'], 'obssets': {
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['7']}
}}
varinfo['CLDHGH_VISIR']={'desc':'High cloud amount (VIS/IR/NIR clouds)', 'sets': ['5', '3', '10'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10']}
}}
varinfo['FLNS_SOUTH']={'desc':'Surf Net LW flux (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['7']}
}}
varinfo['FLUT_SOUTH']={'desc':'TOA upward LW flux (Southern)', 'sets': ['7'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['7']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['STRESS']={'desc':'Surface wind stress (ocean)', 'sets': ['6', 'topten', 'so','testing'], 'obssets': {
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['6']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['6']},
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['6', 'so','testing']},
	'ERS Scatterometer 1992-2000': {
		'filekey': 'ERS', 'usedin': ['6', 'topten', 'so','testing']}
}}
varinfo['CLDTOT_SOUTH']={'desc':'Total cloud amount (IR clouds) (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'Warren Cloud Surface OBS': {
		'filekey': 'WARREN', 'usedin': ['7']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['7']}
}}
varinfo['PREH2O']={'desc':'Total precipitable water', 'sets': ['5', '3', '8', '9', '10'], 'obssets': {
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['5', '3', '8', '9', '10']},
	'NCEP Reanalysis 1979-98 - Tropics': {
		'filekey': 'NCEP_TROP', 'usedin': ['5']},
	'NVAP 1988-1999': {
		'filekey': 'NVAP', 'usedin': ['5', '3', '8', '9', '10']},
	'NVAP 1988-1999 - Tropics': {
		'filekey': 'NVAP_TROP', 'usedin': ['5']},
	'SSM/I (Wentz) 1987-2000 - Tropics': {
		'filekey': 'SSMI_TROP', 'usedin': ['5']},
	'ECMWF Reanalysis 1979-93 - Tropics': {
		'filekey': 'ECMWF_TROP', 'usedin': ['5']},
	'ERA40 Reanalysis 1980-2001 - Tropics': {
		'filekey': 'ERA40_TROP', 'usedin': ['5']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['5', '3', '8', '9', '10', 'testing']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['5', '3', '8', '9', '10']},
	'MODIS Mar2000-Aug2004': {
		'filekey': 'MODIS', 'usedin': ['5', '3']},
	'MODIS Mar2000-Aug2004 - Tropics': {
		'filekey': 'MODIS_TROP', 'usedin': ['5']},
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['5', '3', '8', '9', '10']},
	'JRA25 Reanalysis 1979-04 - Tropics': {
		'filekey': 'JRA25_TROP', 'usedin': ['5']},
	'AIRS IR Sounder 2002-06': {
		'filekey': 'AIRS', 'usedin': ['3']},
	'SSM/I (Wentz) 1987-2000': {
		'filekey': 'SSMI', 'usedin': ['5', '3', '10']}
}}
varinfo['FSNS_NORTH']={'desc':'Surf Net SW flux (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['7']}
}}
varinfo['Ocean_Freshwater']={'desc':'Ocean Freshwater', 'sets': ['2'], 'obssets': {
	'N/A': {
		'filekey': 'NA', 'usedin': ['2']}
}}
varinfo['CLDTOT_NORTH']={'desc':'Total cloud amount (IR clouds) (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'Warren Cloud Surface OBS': {
		'filekey': 'WARREN', 'usedin': ['7']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['7']}
}}
varinfo['FLUTC_SOUTH']={'desc':'TOA clearsky upward LW flux (Southern)', 'sets': ['7'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['7']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['MSE']={'desc':'Moist Static Energy', 'sets': ['15'], 'obssets': {
	'North Slope of Alaska (NSA)': {
		'filekey': 'NSA', 'usedin': ['15']},
	'Tropical Western Pacific--Region 1 (TWP1)': {
		'filekey': 'TWP1', 'usedin': ['15']},
	'Tropical Western Pacific--Region 2 (TWP2)': {
		'filekey': 'TWP2', 'usedin': ['15']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']},
	'Tropical Western Pacific--Region 3 (TWP3)': {
		'filekey': 'TWP3', 'usedin': ['15']}
}}
varinfo['SHUM']={'desc':'Specific humidity', 'sets': ['4a', '4', 'testing'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['4a', '4']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['4a', '4']},
	'AIRS IR Sounder 2002-06': {
		'filekey': 'AIRS', 'usedin': ['4a', '4']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['4a', '4', 'testing']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['4a', '4']}
}}
varinfo['FLNS_NORTH']={'desc':'Surf Net LW flux (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['7']}
}}
varinfo['FSDSC_NORTH']={'desc':'Clearsky Surf SW downwelling flux (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['U_200']={'desc':'200 mb zonal wind', 'sets': ['5', '8', '10'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['5', '8', '10']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['5', '8', '10']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['5', '8', '10']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['5', '8', '10']}
}}
varinfo['ALBEDO_NORTH']={'desc':'TOA albedo (Northern)', 'sets': ['7'], 'obssets': {
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['FLUTC']={'desc':'TOA clearsky upward LW flux', 'sets': ['5', '3', '10'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['5', '3', '10']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['5', '3', '10']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['5', '3', '10']}
}}
varinfo['ALBEDO_SOUTH']={'desc':'TOA albedo (Southern)', 'sets': ['7'], 'obssets': {
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['FLNSC_SOUTH']={'desc':'Clearsky Surf Net LW flux (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['CLOUD']={'desc':'Cloud Fraction', 'sets': ['15'], 'obssets': {
	'North Slope of Alaska (NSA)': {
		'filekey': 'NSA', 'usedin': ['15']},
	'Tropical Western Pacific--Region 1 (TWP1)': {
		'filekey': 'TWP1', 'usedin': ['15']},
	'Tropical Western Pacific--Region 2 (TWP2)': {
		'filekey': 'TWP2', 'usedin': ['15']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']},
	'Tropical Western Pacific--Region 3 (TWP3)': {
		'filekey': 'TWP3', 'usedin': ['15']}
}}
varinfo['FSNS_SOUTH']={'desc':'Surf Net SW flux (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'Large-Yeager 1984-2004': {
		'filekey': 'LARYEA', 'usedin': ['7']}
}}
varinfo['FSNTOAC_SOUTH']={'desc':'TOA clearsky net SW flux (Southern)', 'sets': ['7'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['7']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['CLDTOT_VISIR']={'desc':'Total cloud amount (VIS/IR/NIR clouds)', 'sets': ['5', '3', '10'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10']}
}}
varinfo['FSNTOA_NORTH']={'desc':'TOA net SW flux (Northern)', 'sets': ['7'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['7']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['Z3_300']={'desc':'300 mb geopotential height', 'sets': ['5', '10'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['5', '10']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['5', '10']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['5', '10']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['5', '10']}
}}
varinfo['FLUTC_NORTH']={'desc':'TOA clearsky upward LW flux (Northern)', 'sets': ['7'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['7']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['CLDTOT']={'desc':'Mid cloud amount (IR clouds)', 'sets': ['5', '3', '9', '10', '15', 'so','testing'], 'obssets': {
	'Tropical Western Pacific--Region 1 (TWP1)': {
		'filekey': 'TWP1', 'usedin': ['15']},
	'Tropical Western Pacific--Region 3 (TWP3)': {
		'filekey': 'TWP3', 'usedin': ['15']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']},
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '9', '10', 'so','testing']},
	'Tropical Western Pacific--Region 2 (TWP2)': {
		'filekey': 'TWP2', 'usedin': ['15']},
	'Warren Cloud Surface OBS': {
		'filekey': 'WARREN', 'usedin': ['5', '3']},
	'North Slope of Alaska (NSA)': {
		'filekey': 'NSA', 'usedin': ['15']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['5', '9', 'so','testing']}
}}
varinfo['CLDMED_NORTH']={'desc':'Mid cloud amount (IR clouds) (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['7']}
}}
varinfo['Q']={'desc':'Specific Humidity', 'sets': ['15'], 'obssets': {
	'North Slope of Alaska (NSA)': {
		'filekey': 'NSA', 'usedin': ['15']},
	'Tropical Western Pacific--Region 1 (TWP1)': {
		'filekey': 'TWP1', 'usedin': ['15']},
	'Tropical Western Pacific--Region 2 (TWP2)': {
		'filekey': 'TWP2', 'usedin': ['15']},
	'Southern Great Plains (SGP)': {
		'filekey': 'SGP', 'usedin': ['15']},
	'Tropical Western Pacific--Region 3 (TWP3)': {
		'filekey': 'TWP3', 'usedin': ['15']}
}}
varinfo['PSL_NORTH']={'desc':'Sea-level pressure (Northern)', 'sets': ['7'], 'obssets': {
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['7']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['7']}
}}
varinfo['U']={'desc':'Zonal Wind', 'sets': ['4a', '4', 'topten'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['4a', '4']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['4a', '4']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['4a', '4']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['4a', '4']},
	'ERAI Interim Reanalysis': {
		'filekey': 'ERAI', 'usedin': ['topten']}
}}
varinfo['LWCFSRF']={'desc':'Surf LW Cloud Forcing', 'sets': ['5', '3'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['5', '3']}
}}
varinfo['FSNSC']={'desc':'Clearsky Surf Net SW Flux', 'sets': ['5', '3'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['5', '3']}
}}
varinfo['SURF_WIND_NORTH']={'desc':'Near surface wind (Northern)', 'sets': ['7'], 'obssets': {
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['7']}
}}
varinfo['CLDMED_VISIR']={'desc':'Mid cloud amount (VIS/IR/NIR clouds)', 'sets': ['5', '3', '10'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['5', '3', '10']}
}}
varinfo['MEANPTOP']={'desc':'Mean cloud top pressure (Day)', 'sets': ['5'], 'obssets': {
	'ISCCP D1 Daytime Jul1983-Sep2001': {
		'filekey': 'ISCCP', 'usedin': ['5']},
	'MODIS Mar2000-Aug2004': {
		'filekey': 'MODIS', 'usedin': ['5']}
}}
varinfo['T_850']={'desc':'850 mb temperature', 'sets': ['5', '9', '10'], 'obssets': {
	'ECMWF Reanalysis 1979-93': {
		'filekey': 'ECMWF', 'usedin': ['5', '9', '10']},
	'JRA25 Reanalysis 1979-04': {
		'filekey': 'JRA25', 'usedin': ['5', '9', '10']},
	'AIRS IR Sounder 2002-06': {
		'filekey': 'AIRS', 'usedin': ['5', '9', '10']},
	'ERA40 Reanalysis 1980-2001': {
		'filekey': 'ERA40', 'usedin': ['5', '9', '10']},
	'NCEP Reanalysis 1979-98': {
		'filekey': 'NCEP', 'usedin': ['5', '9', '10']}
}}
varinfo['PRECT_SOUTH']={'desc':'Precipitation rate (Southern)', 'sets': ['7'], 'obssets': {
	'GPCP 1979-2003': {
		'filekey': 'GPCP', 'usedin': ['7']}
}}
varinfo['CLDHGH_VISIR_NORTH']={'desc':'High cloud amount (VIS/IR/NIR) clouds) (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['FLNSC_NORTH']={'desc':'Clearsky Surf Net LW flux (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['FSDS_NORTH']={'desc':'Surf SW downwelling flux (Northern)', 'sets': ['7'], 'obssets': {
	'ISCCP FD Jul1983-Dec2000': {
		'filekey': 'ISCCP', 'usedin': ['7']}
}}
varinfo['Ocean_Heat']={'desc':'Ocean Heat', 'sets': ['2'], 'obssets': {
	'N/A': {
		'filekey': 'NA', 'usedin': ['2']}
}}
varinfo['FSNTOAC_NORTH']={'desc':'TOA clearsky net SW flux (Northern)', 'sets': ['7'], 'obssets': {
	'ERBE Feb1985-Apr1989': {
		'filekey': 'ERBE', 'usedin': ['7']},
	'CERES2 March 2000-October 2005': {
		'filekey': 'CERES2', 'usedin': ['7']},
	'CERES 2000-2003': {
		'filekey': 'CERES', 'usedin': ['7']}
}}
varinfo['CLDMED_SOUTH']={'desc':'Mid cloud amount (IR clouds) (Southern)', 'sets': ['7'], 'obssets': {
	'ISCCP D2 1983-2001': {
		'filekey': 'ISCCP', 'usedin': ['7']},
	'CLOUDSAT (Radar+Lidar) Sep2006-Nov2008': {
		'filekey': 'CLOUDSAT', 'usedin': ['7']}
}}
