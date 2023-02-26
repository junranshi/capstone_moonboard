# Capstone Project: MoonBoard Route Generation and Grade Classification Using Machine Learning Models

Project description: Building on existing published attempts, this project sources data from the standard indoor climbing wall (the MoonBoard) and uses the 25,000 existing routes for training generative and classification models. Variational Autoencoders are explored for route generation and new routes are evaluated qualitatively by experienced climbers. Using generated routes, we were also able to improve classification accuracy for routes of higher difficulties.

This is the project repository for Junran's Capstone project for Minerva Univeristy.

## Dataset
The raw data can be found in the `raw_data` folder, the dataset is `moonGen_scrape_2016_final`. The `data` folder contains the cleaned dataset in csv and pickle format, as well as a notebook of exploratory data analysis steps.

## Machine Learning Models
The models are in Colab notebooks. You can simply go to the `models` folder and run the `Generation_Finalized` and `Classification_Finalized` notebooks. The notebooks include texts and comments to help you navigate the code.

Routes generated for classification and website display purposes respectively can be found in the `generated data` folder.

## Website:
A static website found at https://junranshi.github.io/moonboard_website/ is created to display the results of this project. Users can view generated routes of their desired grade and find the classifiers' prediction of the route's grade.

This website is modified using the code from https://github.com/andrew-houghton/moon-board-climbing.

To run the website locally, set the `website` folder as the working directory and execute `python -m SimpleHTTPServer` (Python2) or `python3 -m http.server` (Python3). Website will be hosted on http://localhost:8000.