# Project Title - Sea Surface Salinity - A notebook on making salinity maps

## Executive Summary - 
This Project is a tutorial notebook for marine and climate scientists wishing to study how the sea water salinity has changed over the years. The notebook produces two maps, centered appropriately based on the choice of ocean of the user, obtained as an input.

These maps can be used by students to understand the differences in salinity of the world oceans, and by scientists wishing to correlate and compare the salinity of a particular ocean across two periods in time. This project essentially serves as an ancillory tool for a larger, much more complex project focused on marine science or climate change, particularly for studying the effects of salinity changes and how it affects the global climate that is controlled by ocean circulation.

The notebook runs 4 functions, including the documentation, and then the Mapmaker codes. A brief about each function is available as docstrings above them.


## Goal - 
- To develop an easy to navigate and fairly generalizable python notebook to plot a surface seawater salinity map of the global oceans, that can be used for further research
- To make the code generalized and easy to navigate through the addition of docstrings and detailed documentation.
## Background - 
Climate research and Climate change analysis has become one of the growing fields of research in the recent days. A lot of debate regarding whether Climate Change is real, and the effects it is having on the current ecosystems is being conducted at interntaional forums. Furthermore, ocean salinity is an important indicator of climate change, as it affects the hydrological cycle and the thermohyaline circulation (Global Ocean Conveyor belt) significantly. 

The analysis of seawater salinity had been rather slow during the past 2 decades, but ever since the onset of the ARGO project (Array for Real-time Geostrophic Observations) began in the year 2000, various such salinity specific analysis measures were incorporated, making its study progress at much better rates. A vast number of programs and dedicated softwares are out there that achieves what this notebook does, in a much larger scale and in a much detailed manner. There are even some softwares that specifically display climate data on world maps, in the form of overlays and interactive maps.

This notebook achieves a simple task of creating two world maps centred as per the input of the user, focusing on the ocean of the user's choice. The maps are from two years, 1922 and 2021, and displays the salinity of the oceans and how they have changed in the 99 years separating them. This notebook is general in the sense that this can be adapted by anyone to use in presentations, or even adapt the entire notebook and make changes to it to suit their research

## Resources and Timeline - 
The inspiration for this project came from observing similar maps showing other kinds of data over the course of undergraduate studies. The datasets for this project were downloaded from the marine datasets (EN4) of Met Office Hadley Center for Climate Science and Services. The Met Office maintain a library of gridded datasets that are to be used in climate monitoring and research. The dataset consists of two products :- Observed surface temperatures and salinity profiles, and the objective analyses that are formed from the profile data. 

** Review of codes **:-
1. Cartopy:- Cartopy is the most common package that is used globally for geospatial data processing to produce maps and other geospatial analysis of data. This makes it an essential module to be imported into this notebook. This is a domain specific package that extends upon the Matplot module, which again is a data visualisation package.
2. Iris:- This package is used for analyzing and visualising earth science data. This module easily reads data is in the NetCDF format. This is also a built up package that uses Numpy as its base.
3. The user guide for the EN4 datasets helped me in getting started with writing the code, and on choosing which modules to use. The link to the user guide is as follows: https://www.metoffice.gov.uk/hadobs/hadiod/HadIOD.1.2.0.0_Product_User_Guide_[1.1].pdf

** Timeline **:-
1. Search for the appropriate datasets among all the available ones on open source platforms and satellite datas.
2. Make a raw draft of the code
3. Create separate python files for dependencies and the functions
4. Clean up the code and assign functions
5. Create and complete the notebook
6. developed and saved the maps.

## Testing
The functions that will be defined will further be tested using test functions and by running a notebook to do the same. `pytest` will be used to achieve this and the test functions will try and assert the type and length of the functions and the variables that they return

## References
Dataset - Data version - EN.4.2.2, bias correction - .c14, downloaded on 24/06/2022 - "Good, S. A., M. J. Martin and N. A. Rayner, 2013. EN4: quality controlled ocean temperature and salinity profiles and monthly objective analyses with uncertainty estimates, Journal of Geophysical Research: Oceans, doi:10.1002/2013JC009067"
Du, Y., Zhang, Y. & Shi, J. Relationship between sea surface salinity and ocean circulation and climate change. Sci. China Earth Sci. 62, 771–782 (2019). https://doi.org/10.1007/s11430-018-9276-6


