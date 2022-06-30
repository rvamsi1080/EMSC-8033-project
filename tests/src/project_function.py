from .Dependencies import *

def proj_documentation():
    
    markdown_documentation = """
    
This markdown function returns a brief overview of the project and the obejective it tries to achieve.

This notebook is programmed to create a pair of maps for the month of April, for two years that are 100 years apart (1922 and 2022). It has been designed in such a way that the user can specify which ocean they would like the map to be centered about.

The notebook is fairly generalized and user friendly, with appropriate instructions and details provided prior to running the cells. The maps are plotted using inbuilt packages such as matplotlib and Cartopy, and the data is extracted using the iris module. The salinity data is obtained from the EN4 datasets of the Met Office - Hadley Center."""
    
    return markdown_documentation


def load_datasets(dataset1, dataset2):
        """ The data should be chosen from the objective analyses datasets (available as .zip files), and uploaded onto the workspace before beginning work on the same. Two of them to be selected to compare the difference in salinity.The code in this function cannot be customised since these are specific to the data that is dowloaded. The user, if need arises, may have to make considerable changes to this function depending on the dataset they plan to use if they decide to use completely different ones """
        
        import iris
        
        data_salinity = []
        
        sal_analysis1 = iris.load(dataset1)
        sal_analysis2 = iris.load(dataset2)
        sal1 = sal_analysis1.extract('sea_water_salinity')[0]
        sal2 = sal_analysis2.extract('sea_water_salinity')[0]
        gridlons1 = sal1.coord('longitude').contiguous_bounds()
        gridlons2 = sal2.coord('longitude').contiguous_bounds()
        gridlats1 = sal1.coord('latitude').contiguous_bounds()
        gridlats2 = sal2.coord('latitude').contiguous_bounds()
        seasal_2021 = sal1.data[0, 0, :, :]
        seasal_1922 = sal2.data[0, 0, :, :]
        
        data_salinity.append(seasal_2021)
        data_salinity.append(seasal_1922)
        
        return data_salinity, gridlons1, gridlons2, gridlats1, gridlats2


def ocean_selector():
    """ This function allows the user to type in the ocean that they wish the plot to be centred about"""
    oceans = []
   
    ocean_choice = input('choose your ocean:')
    
    oceans.append(ocean_choice)
    return oceans[0]


def central_lon(x):
    """ This function assigns the longitude value of the chosen ocean to the central longitude variable.  For simplicity's sake, only the Indian, Pacific and Atlantic oceans are used for this program, since to display the Polar oceans (Southern and Northern oceans), we need to make orthographic changes to the projection """   
   
    
    ocean_centre = {'Indian' : 81, 'Pacific' : 180, 'Atlantic' : -20}
    
    
    if x in ocean_centre:
        central_lon = (ocean_centre[x])
        return central_lon
    else:
        print ('Invalid Ocean choice')
               
    return central_lon



    

