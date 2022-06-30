# Project Report

## Introduction
This project has successfully develops 2 maps of the user's choice of ocean, one  each of the month of April of the years 1922 and 2021 respectively. The dataset used for this purpose is from the Marine datasets EN4 of the Met Office Hadley Observation Center. EN.4.2.2 data were obtained from https://www.metoffice.gov.uk/hadobs/en4/ and are © British Crown Copyright, Met Office, [year of first publication], provided under a Non-Commercial Government Licence http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/. These basic maps display the sea surface salinity of the oceans for the two years, which can either used for the purpose of studying, or can be modified and catered to the needs of further research.

## List of Dependencies
This project makes use of Python as the only programming language and Jupyter as the sole platform. As a result, the project uses pre-loaded python modules/dependencies to facilitate the code-writing process. The dependencies used are as follows:-


- Iris :  This package is used for analyzing and visualising the earth science data that is used in this project, specifically since the data is in a NetCDF format. The datasets were called, loaded, and extracted using this module.
- Maplotlib : This is the module that is used to visualise the data that is extracted and stored. This module is specifically used to plot the data visually and works in tandem with the Cartopy module, and presenting the extracted data as they are on the map.
- Cartopy : This module aids in visualizing the data into geospatial forms and produce desired maps. Cartopy was used to finally produce the maps, by specifying the projections and and making the map presentable by demarcating the land and other features.

## Instruction
This project contains 4 functions, all of which are easy to read through and understand.
- The ` proj_documentation()` returns the documentation markdown file of the project, giving a brief about the entire project.

- The `load_datasets(dataset1, dataset2)` function loads the marine dataset onto the program, extracts the required data and assigns it to appropriate variables and returns a list of all the items that will be needed to progress through the code.

- The `ocean_selector()` function lets the user to input the name of the ocean that they wish to have their maps centered about, and stores it into a list. This element is then called upon and returned as a string at the end of the function.

- The `central_lon(x)` function assigns the ocean input with the longitude that it needs to be centered about. This is only possible if the dictionary specified identifies the inout from the user as an element of its list. 

## Testing
Just two tests have been defined for this project, although there were 4 functions that could be potentially tested. This is because the last two functions required inputs from the user upon running the notebook, and defining tests for them without doing the same needed additional steps that I am not yet aware of.

**test_documentation()** to assert whether the documentation is of the type string.

**test_datasets()** to assert if the number of variables collected and the type they are variable the data is extracted and stored in.

## Limitations and Further Development
This notebook is a simple beginner's guide to creating sea surface salinity maps. One of the main limitation is that the changes in projections that needs to be incorporated to view the Polar oceans (Arctic and Antarctic oceans) have not been done. If the user desires to do the same, then they must make changes to the projection, and change it to orthographic and specify further changes to it, which I do not completely understand. This notebook can further be developed into so many different ways, where in the datasets can be used to create correlation plots/regression plots (haloclines, thermoclines, etc.), and even make the maps in such a way that it shows only the particular ocean/sea of interest with a higher resolution and quality.


## References
Dataset - Data version - EN.4.2.2, bias correction - .c14, downloaded on 24/06/2022 - "Good, S. A., M. J. Martin and N. A. Rayner, 2013. EN4: quality controlled ocean temperature and salinity profiles and monthly objective analyses with uncertainty estimates, Journal of Geophysical Research: Oceans, doi:10.1002/2013JC009067"
Du, Y., Zhang, Y. & Shi, J. Relationship between sea surface salinity and ocean circulation and climate change. Sci. China Earth Sci. 62, 771–782 (2019). https://doi.org/10.1007/s11430-018-9276-6