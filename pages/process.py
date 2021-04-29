# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            # Process
            
            I obtained my dataset from the Kaggle competition website.  
            It was scrapped by vgchartz.com.  The script for the data scrape
            is available at 
            [BeautifulSoup](https://github.com/GregorUT/vgchartzScrape).
            The link to my dataset is on
            [Kaggle](https://www.kaggle.com/gregorut/videogamesales).

            I have always enjoyed playing 2d and 3d platform type games: 
            (Super Mario Bros, Sonic the Hedghog and Spyro the Dragon).
            When I saw this dataset I wondered, it would be good for a company to
            to see if sales could be determined by a video games platform,
            publisher and genre.  My goal for this build was to see if there/-
            was a way to predict sales from a video game's platform, publisher and genre.

            The approach I took was to first clean up my data by getting rid of
            columns not intial to this analysis.  I split my data into a feature
            matrix and target vector using the sales column.  I further split the
            data into a training and validation set.  Then, I established my baseline
            by using the mean of the sales data.  However, I realized that my 
            data was heavy skewed to the right, so had to use a log transformation
            to get a better result. My baseline mean absolute error(MAE)
            was 510,627 thousand or 0.51 million copies sold.

            After establishing the baseline, I used a couple of models to get a
            better MAE.  I used ridge regression and XGBoost regression.  The model
            I chose, which gave me the better error, was XGBoost at a MAE of 485,433
            copies sold.    

            I chose to communicate my results using permutation importance, but 
            because there were only three categories it was really necessary.  Platform
            and genre were the strongest predictors of sales.  

            The limitations of my set were that it was massive in terms of data with 
            a range from 1980 to 2020.  Thats huge considering many of the platforms
            are not making games anymore.  It was disappointing to me that producer 
            information was not added to the features because that would have probably
            had a impact on the prediction.  Also there was continous information such
            as cost to manufactor, produce or market, number of years from conception 
            to shelf, or country released.

            Some of the thinking I had with this project was along the lines of how relevant
            is the sales data in the 1980's, when console games were in their infancy, to todays.
            Making the log transformation evened that out I am sure.  I would expect as video
            games progressed through the years and more people were given access to them, that
            more would be sold.  I am also not sure if this website is tracking sales of these 
            vintage games today.  Many are sold in pawn shops and auctions to video game enthusiasts.
            That would boost some of the sales numbers.  


            In conclusion, given the hundreds of millions of copies of games were sold
            I am satisfied with my MAE.  They are not that bad but more information on 
            these video games could vastly improve the predictions. It was really enjoyable
            to work on this project and consider all of the questions that needed to answered
            and a suprise that not all those questions were answered.  The build only resulted
            in giving my more questions than I orginally started with.
            """
        ),

    ],
)


layout = dbc.Row([column1])