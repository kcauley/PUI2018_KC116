# Assignment 2 Review:
 ## 1. Hypothesis evaluation:
 Having read the Idea for analysis, it is clear to me that the author wants to 
Alternative Hypothesis: During the weekends there will be more 'Customers'(non-subscribers who purchase 24hr passes) using Citibike than regular subscribers.
Null Hypothesis: Weekend activity has the same or less users described as 'customers.'
 However, it lacks certain specifications that would make the hypothesis testable, despite giving the significance level. 

 Please note that despite the fact that all citibike data is provided, I assume we only compare two samples without population knowledge. This is assumption I decide to follow, however given we actually can calculate the population data, it could be restated accordingly.
 ## 2. Data 
 The data for two genders and durations for a specific time period has been identified. I would suggest in addition to separate the two samples into two df objects (for male and female separately) and normalizing, since we are looking at the mean. At a first glance the distribution for both genders resembles Gaussian. 
 





{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Populating the interactive namespace from numpy and matplotlib\n"
     ]
    }
   ],
   "source": [
    "from __future__  import print_function, division\n",
    "import pylab as pl\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os\n",
    "\n",
    "get_ipython().run_line_magic('pylab', 'inline')\n",
    "\n",
    "if os.getenv ('PUI2016') is None:\n",
    "    print (\"Must set env variable PUI2016\")\n",
    "if os.getenv ('PUIDATA') is None:\n",
    "    print (\"Must set env variable PUI2016\")\n",
    "\n",
    "import os\n",
    "import json\n",
    "#s = json.load( open(os.getenv('PUI2016') + \"/fbb_matplotlibrc.json\") )\n",
    "#pl.rcParams.update(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "os.environ['PUIDATA'] = '/nfshome/kc116/PUIDATA'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/nfshome/kc116/PUIDATA'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getenv('PUIDATA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def getCitiBikeCSV(datestring):\n",
    "    print (\"Downloading\", datestring)\n",
    "    \n",
    "    ### First I will check that it is not already there\n",
    "    if not os.path.isfile(os.getenv(\"PUIDATA\") + \"/\" + datestring + \"-citibike-tripdata.csv\"):\n",
    "        if os.path.isfile(datestring + \"-citibike-tripdata.csv\"):\n",
    "            # if in the current dir just move it\n",
    "            if os.system(\"mv \" + datestring + \"-citibike-tripdata.csv \" + os.getenv(\"PUIDATA\")):\n",
    "                print (\"Error moving file!, Please check!\")\n",
    "        #otherwise start looking for the zip file\n",
    "        else:\n",
    "            if not os.path.isfile(os.getenv(\"PUIDATA\") + \"/\" + datestring + \"-citibike-tripdata.zip\"):\n",
    "                if not os.path.isfile(datestring + \"-citibike-tripdata.zip\"):\n",
    "                    os.system(\"curl -O https://s3.amazonaws.com/tripdata/\" + datestring + \"-citibike-tripdata.zip\")\n",
    "                    print('zip downloaded')\n",
    "                ###  To move it I use the os.system() functions to run bash commands with arguments\n",
    "                os.system(\"mv \" + datestring + \"-citibike-tripdata.zip \" + os.getenv(\"PUIDATA\"))\n",
    "            ### unzip the csv \n",
    "            os.system(\"unzip \" + os.getenv(\"PUIDATA\") + \"/\" + datestring + \"-citibike-tripdata.zip\")\n",
    "            ## NOTE: old csv citibike data had a different name structure. \n",
    "            if '2014' in datestring:\n",
    "                os.system(\"mv \" + datestring[:4] + '-' +  datestring[4:] + \n",
    "                          \"\\ -\\ Citi\\ Bike\\ trip\\ data.csv \" + datestring + \"-citibike-tripdata.csv\")\n",
    "            os.system(\"mv \" + datestring + \"-citibike-tripdata.csv \" + os.getenv(\"PUIDATA\"))\n",
    "    ### One final check:\n",
    "    if not os.path.isfile(os.getenv(\"PUIDATA\") + \"/\" + datestring + \"-citibike-tripdata.csv\"):\n",
    "        print (\"WARNING!!! something is wrong: the file is not there!\")\n",
    "\n",
    "    else:\n",
    "        print (\"file in place, you can continue\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Downloading 201610\n",
      "file in place, you can continue\n"
     ]
    }
   ],
   "source": [
    "datestring = '201610'\n",
    "getCitiBikeCSV(datestring)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/nfshome/kc116/PUIDATA'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getenv('PUIDATA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(os.getenv(\"PUIDATA\") + \"/\" + datestring + '-citibike-tripdata.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Trip Duration</th>\n",
       "      <th>Start Time</th>\n",
       "      <th>Stop Time</th>\n",
       "      <th>Start Station ID</th>\n",
       "      <th>Start Station Name</th>\n",
       "      <th>Start Station Latitude</th>\n",
       "      <th>Start Station Longitude</th>\n",
       "      <th>End Station ID</th>\n",
       "      <th>End Station Name</th>\n",
       "      <th>End Station Latitude</th>\n",
       "      <th>End Station Longitude</th>\n",
       "      <th>Bike ID</th>\n",
       "      <th>User Type</th>\n",
       "      <th>Birth Year</th>\n",
       "      <th>Gender</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>328</td>\n",
       "      <td>2016-10-01 00:00:07</td>\n",
       "      <td>2016-10-01 00:05:35</td>\n",
       "      <td>471</td>\n",
       "      <td>Grand St &amp; Havemeyer St</td>\n",
       "      <td>40.712868</td>\n",
       "      <td>-73.956981</td>\n",
       "      <td>3077</td>\n",
       "      <td>Stagg St &amp; Union Ave</td>\n",
       "      <td>40.708771</td>\n",
       "      <td>-73.950953</td>\n",
       "      <td>25254</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1992.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>398</td>\n",
       "      <td>2016-10-01 00:00:11</td>\n",
       "      <td>2016-10-01 00:06:49</td>\n",
       "      <td>3147</td>\n",
       "      <td>E 85 St &amp; 3 Ave</td>\n",
       "      <td>40.778012</td>\n",
       "      <td>-73.954071</td>\n",
       "      <td>3140</td>\n",
       "      <td>1 Ave &amp; E 78 St</td>\n",
       "      <td>40.771404</td>\n",
       "      <td>-73.953517</td>\n",
       "      <td>17810</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1988.0</td>\n",
       "      <td>2</td>\n",
       "      <td>2016-10-01 00:00:11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>430</td>\n",
       "      <td>2016-10-01 00:00:14</td>\n",
       "      <td>2016-10-01 00:07:25</td>\n",
       "      <td>345</td>\n",
       "      <td>W 13 St &amp; 6 Ave</td>\n",
       "      <td>40.736494</td>\n",
       "      <td>-73.997044</td>\n",
       "      <td>470</td>\n",
       "      <td>W 20 St &amp; 8 Ave</td>\n",
       "      <td>40.743453</td>\n",
       "      <td>-74.000040</td>\n",
       "      <td>20940</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1965.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>351</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "      <td>2016-10-01 00:06:12</td>\n",
       "      <td>3307</td>\n",
       "      <td>West End Ave &amp; W 94 St</td>\n",
       "      <td>40.794165</td>\n",
       "      <td>-73.974124</td>\n",
       "      <td>3357</td>\n",
       "      <td>W 106 St &amp; Amsterdam Ave</td>\n",
       "      <td>40.800836</td>\n",
       "      <td>-73.966449</td>\n",
       "      <td>19086</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1993.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2693</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "      <td>2016-10-01 00:45:15</td>\n",
       "      <td>3428</td>\n",
       "      <td>8 Ave &amp; W 16 St</td>\n",
       "      <td>40.740983</td>\n",
       "      <td>-74.001702</td>\n",
       "      <td>3323</td>\n",
       "      <td>W 106 St &amp; Central Park West</td>\n",
       "      <td>40.798186</td>\n",
       "      <td>-73.960591</td>\n",
       "      <td>26502</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1991.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Trip Duration           Start Time            Stop Time  Start Station ID  \\\n",
       "0            328  2016-10-01 00:00:07  2016-10-01 00:05:35               471   \n",
       "1            398  2016-10-01 00:00:11  2016-10-01 00:06:49              3147   \n",
       "2            430  2016-10-01 00:00:14  2016-10-01 00:07:25               345   \n",
       "3            351  2016-10-01 00:00:21  2016-10-01 00:06:12              3307   \n",
       "4           2693  2016-10-01 00:00:21  2016-10-01 00:45:15              3428   \n",
       "\n",
       "        Start Station Name  Start Station Latitude  Start Station Longitude  \\\n",
       "0  Grand St & Havemeyer St               40.712868               -73.956981   \n",
       "1          E 85 St & 3 Ave               40.778012               -73.954071   \n",
       "2          W 13 St & 6 Ave               40.736494               -73.997044   \n",
       "3   West End Ave & W 94 St               40.794165               -73.974124   \n",
       "4          8 Ave & W 16 St               40.740983               -74.001702   \n",
       "\n",
       "   End Station ID              End Station Name  End Station Latitude  \\\n",
       "0            3077          Stagg St & Union Ave             40.708771   \n",
       "1            3140               1 Ave & E 78 St             40.771404   \n",
       "2             470               W 20 St & 8 Ave             40.743453   \n",
       "3            3357      W 106 St & Amsterdam Ave             40.800836   \n",
       "4            3323  W 106 St & Central Park West             40.798186   \n",
       "\n",
       "   End Station Longitude  Bike ID   User Type  Birth Year  Gender  \\\n",
       "0             -73.950953    25254  Subscriber      1992.0       1   \n",
       "1             -73.953517    17810  Subscriber      1988.0       2   \n",
       "2             -74.000040    20940  Subscriber      1965.0       1   \n",
       "3             -73.966449    19086  Subscriber      1993.0       1   \n",
       "4             -73.960591    26502  Subscriber      1991.0       1   \n",
       "\n",
       "                 date  \n",
       "0 2016-10-01 00:00:07  \n",
       "1 2016-10-01 00:00:11  \n",
       "2 2016-10-01 00:00:14  \n",
       "3 2016-10-01 00:00:21  \n",
       "4 2016-10-01 00:00:21  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# df is the dataframe where the content of the csv file is stored\n",
    "df['date'] = pd.to_datetime(df['Start Time'])\n",
    "\n",
    "# note that with dataframes I can refer to variables as dictionary keys, \n",
    "# i.e. df['starttime'] or as attributes: df.starttime. \n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Trip Duration', 'Start Time', 'Stop Time', 'Start Station ID',\n",
       "       'Start Station Name', 'Start Station Latitude',\n",
       "       'Start Station Longitude', 'End Station ID', 'End Station Name',\n",
       "       'End Station Latitude', 'End Station Longitude', 'Bike ID', 'User Type',\n",
       "       'Birth Year', 'Gender', 'date'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Trip Duration</th>\n",
       "      <th>Start Time</th>\n",
       "      <th>Stop Time</th>\n",
       "      <th>Start Station ID</th>\n",
       "      <th>Start Station Name</th>\n",
       "      <th>Start Station Latitude</th>\n",
       "      <th>Start Station Longitude</th>\n",
       "      <th>End Station ID</th>\n",
       "      <th>End Station Name</th>\n",
       "      <th>End Station Latitude</th>\n",
       "      <th>End Station Longitude</th>\n",
       "      <th>Bike ID</th>\n",
       "      <th>User Type</th>\n",
       "      <th>Birth Year</th>\n",
       "      <th>Gender</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>328</td>\n",
       "      <td>2016-10-01 00:00:07</td>\n",
       "      <td>2016-10-01 00:05:35</td>\n",
       "      <td>471</td>\n",
       "      <td>Grand St &amp; Havemeyer St</td>\n",
       "      <td>40.712868</td>\n",
       "      <td>-73.956981</td>\n",
       "      <td>3077</td>\n",
       "      <td>Stagg St &amp; Union Ave</td>\n",
       "      <td>40.708771</td>\n",
       "      <td>-73.950953</td>\n",
       "      <td>25254</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1992.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>398</td>\n",
       "      <td>2016-10-01 00:00:11</td>\n",
       "      <td>2016-10-01 00:06:49</td>\n",
       "      <td>3147</td>\n",
       "      <td>E 85 St &amp; 3 Ave</td>\n",
       "      <td>40.778012</td>\n",
       "      <td>-73.954071</td>\n",
       "      <td>3140</td>\n",
       "      <td>1 Ave &amp; E 78 St</td>\n",
       "      <td>40.771404</td>\n",
       "      <td>-73.953517</td>\n",
       "      <td>17810</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1988.0</td>\n",
       "      <td>2</td>\n",
       "      <td>2016-10-01 00:00:11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>430</td>\n",
       "      <td>2016-10-01 00:00:14</td>\n",
       "      <td>2016-10-01 00:07:25</td>\n",
       "      <td>345</td>\n",
       "      <td>W 13 St &amp; 6 Ave</td>\n",
       "      <td>40.736494</td>\n",
       "      <td>-73.997044</td>\n",
       "      <td>470</td>\n",
       "      <td>W 20 St &amp; 8 Ave</td>\n",
       "      <td>40.743453</td>\n",
       "      <td>-74.000040</td>\n",
       "      <td>20940</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1965.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>351</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "      <td>2016-10-01 00:06:12</td>\n",
       "      <td>3307</td>\n",
       "      <td>West End Ave &amp; W 94 St</td>\n",
       "      <td>40.794165</td>\n",
       "      <td>-73.974124</td>\n",
       "      <td>3357</td>\n",
       "      <td>W 106 St &amp; Amsterdam Ave</td>\n",
       "      <td>40.800836</td>\n",
       "      <td>-73.966449</td>\n",
       "      <td>19086</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1993.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2693</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "      <td>2016-10-01 00:45:15</td>\n",
       "      <td>3428</td>\n",
       "      <td>8 Ave &amp; W 16 St</td>\n",
       "      <td>40.740983</td>\n",
       "      <td>-74.001702</td>\n",
       "      <td>3323</td>\n",
       "      <td>W 106 St &amp; Central Park West</td>\n",
       "      <td>40.798186</td>\n",
       "      <td>-73.960591</td>\n",
       "      <td>26502</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1991.0</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Trip Duration           Start Time            Stop Time  Start Station ID  \\\n",
       "0            328  2016-10-01 00:00:07  2016-10-01 00:05:35               471   \n",
       "1            398  2016-10-01 00:00:11  2016-10-01 00:06:49              3147   \n",
       "2            430  2016-10-01 00:00:14  2016-10-01 00:07:25               345   \n",
       "3            351  2016-10-01 00:00:21  2016-10-01 00:06:12              3307   \n",
       "4           2693  2016-10-01 00:00:21  2016-10-01 00:45:15              3428   \n",
       "\n",
       "        Start Station Name  Start Station Latitude  Start Station Longitude  \\\n",
       "0  Grand St & Havemeyer St               40.712868               -73.956981   \n",
       "1          E 85 St & 3 Ave               40.778012               -73.954071   \n",
       "2          W 13 St & 6 Ave               40.736494               -73.997044   \n",
       "3   West End Ave & W 94 St               40.794165               -73.974124   \n",
       "4          8 Ave & W 16 St               40.740983               -74.001702   \n",
       "\n",
       "   End Station ID              End Station Name  End Station Latitude  \\\n",
       "0            3077          Stagg St & Union Ave             40.708771   \n",
       "1            3140               1 Ave & E 78 St             40.771404   \n",
       "2             470               W 20 St & 8 Ave             40.743453   \n",
       "3            3357      W 106 St & Amsterdam Ave             40.800836   \n",
       "4            3323  W 106 St & Central Park West             40.798186   \n",
       "\n",
       "   End Station Longitude  Bike ID   User Type  Birth Year  Gender  \\\n",
       "0             -73.950953    25254  Subscriber      1992.0       1   \n",
       "1             -73.953517    17810  Subscriber      1988.0       2   \n",
       "2             -74.000040    20940  Subscriber      1965.0       1   \n",
       "3             -73.966449    19086  Subscriber      1993.0       1   \n",
       "4             -73.960591    26502  Subscriber      1991.0       1   \n",
       "\n",
       "                 date  \n",
       "0 2016-10-01 00:00:07  \n",
       "1 2016-10-01 00:00:11  \n",
       "2 2016-10-01 00:00:14  \n",
       "3 2016-10-01 00:00:21  \n",
       "4 2016-10-01 00:00:21  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_1 = df.drop([ 'Start Station ID',\n",
    "       'Start Station Name', 'Start Station Latitude',\n",
    "       'Start Station Longitude', 'End Station ID', 'End Station Name',\n",
    "       'End Station Latitude', 'End Station Longitude', 'Bike ID',\n",
    "       'Birth Year'],\n",
    "      axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Trip Duration</th>\n",
       "      <th>Start Time</th>\n",
       "      <th>Stop Time</th>\n",
       "      <th>User Type</th>\n",
       "      <th>Gender</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>328</td>\n",
       "      <td>2016-10-01 00:00:07</td>\n",
       "      <td>2016-10-01 00:05:35</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>398</td>\n",
       "      <td>2016-10-01 00:00:11</td>\n",
       "      <td>2016-10-01 00:06:49</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>2</td>\n",
       "      <td>2016-10-01 00:00:11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>430</td>\n",
       "      <td>2016-10-01 00:00:14</td>\n",
       "      <td>2016-10-01 00:07:25</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>351</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "      <td>2016-10-01 00:06:12</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2693</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "      <td>2016-10-01 00:45:15</td>\n",
       "      <td>Subscriber</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-10-01 00:00:21</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Trip Duration           Start Time            Stop Time   User Type  \\\n",
       "0            328  2016-10-01 00:00:07  2016-10-01 00:05:35  Subscriber   \n",
       "1            398  2016-10-01 00:00:11  2016-10-01 00:06:49  Subscriber   \n",
       "2            430  2016-10-01 00:00:14  2016-10-01 00:07:25  Subscriber   \n",
       "3            351  2016-10-01 00:00:21  2016-10-01 00:06:12  Subscriber   \n",
       "4           2693  2016-10-01 00:00:21  2016-10-01 00:45:15  Subscriber   \n",
       "\n",
       "   Gender                date  \n",
       "0       1 2016-10-01 00:00:07  \n",
       "1       2 2016-10-01 00:00:11  \n",
       "2       1 2016-10-01 00:00:14  \n",
       "3       1 2016-10-01 00:00:21  \n",
       "4       1 2016-10-01 00:00:21  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x7f13b92bd9e8>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA4MAAAODCAYAAAAGl9T6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzs3X+wXWV97/HPYxIJIyoIwQtECGKc\nIfwwxPDDtoNUOoDAELCl4p0JmZbyo9V67bROsbXFWm1xaKtlis7AFQnRig4WYVoqUgSBFoGEpgjk\nUlJFiVJ+JEBBGpTw3D/OCj3g4STkJBzM9/Wa2XP2efZaz3rOnkxm3rPWXrv13gMAAEAtr5jsBQAA\nAPDSE4MAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAVN\nnewFbG477bRTnzVr1mQvAwAAYFIsW7bs4d77jA1tt9XF4KxZs7J06dLJXgYAAMCkaK19b2O2c5ko\nAABAQWIQAACgIDEIAABQ0Fb3mUEAAODl4Sc/+UlWrVqVtWvXTvZStkrTp0/PzJkzM23atE3aXwwC\nAABbxKpVq/LqV786s2bNSmttspezVem9Z/Xq1Vm1alX23HPPTZrDZaIAAMAWsXbt2uy4445CcAto\nrWXHHXec0FlXMQgAAGwxQnDLmeh7KwYBAICt1sc//vHss88+2X///TN37tzcfPPNL7jtRz7ykfzF\nX/zFZj3+0qVL8/73v3+LzT8RPjMIAAC8JG5buHCzzjdvyZJxX7/pppvy93//97ntttuyzTbb5OGH\nH86Pf/zjzbqG8Tz99NOZP39+5s+fP+G5eu/pvecVr9h85/OcGQQAALZK999/f3baaadss802SZKd\ndtopu+66a2bNmpWHH344yciZu8MOO+zZff7t3/4t73jHOzJ79uxccMEFz85z6KGHZu7cudl3331z\nww03JEm+9rWvZd68eXnLW96Sww8/PMnI2b/TTjstRxxxRE4++eRcd911OfbYY8edP0nOOeecHHjg\ngdl///1z1llnJUnuvffe7L333vmt3/qtzJs3L/fdd99mfX+cGQQAALZKRxxxRD760Y/mzW9+c37p\nl34p7373u/P2t7993H1uv/32fOtb38qPfvSjHHDAATnmmGPyxS9+MUceeWT+8A//MOvWrcuTTz6Z\nhx56KKeeemquv/767LnnnlmzZs2zcyxbtiw33nhjtt1221x33XUbnP+OO+7IPffck1tuuSW99xx3\n3HG5/vrrs/vuu+fuu+/O5z73uXz605/e7O+PGAQAALZK2223XZYtW5Ybbrgh1157bd797nfn7LPP\nHnefBQsWZNttt822226bX/zFX8wtt9ySAw88ML/+67+en/zkJzn++OMzd+7cXHfddTn00EOf/VqH\n173udc/Ocdxxx2Xbbbfd6PlvvPHGfP3rX88BBxyQJHniiSdyzz33ZPfdd88ee+yRQw45ZDO9I88l\nBgEAgK3WlClTcthhh+Wwww7Lfvvtl8WLF2fq1Kl55plnkuSnvprh+XfobK3l0EMPzfXXX59/+Id/\nyMKFC/PBD34w22+//QvezfNVr3rVC65nrPl77/nQhz6U008//Tmv3XvvvePONVE+MwgAAGyV7r77\n7txzzz3P/r58+fLssccemTVrVpYtW5Yk+cpXvvKcfS6//PKsXbs2q1evznXXXZcDDzww3/ve97Lz\nzjvn1FNPzSmnnJLbbrstb3vb2/LNb34z3/3ud5PkOZeJjmes+Y888shceOGFeeKJJ5IkP/jBD/Lg\ngw9ujrdgXM4MAgAAW6Unnngiv/3bv51HH300U6dOzZve9Kacf/75WbFiRU455ZT82Z/9WQ4++ODn\n7HPQQQflmGOOyfe///380R/9UXbdddcsXrw455xzTqZNm5btttsuF198cWbMmJHzzz8/73rXu/LM\nM89k5513ztVXX73BNY01/6677poVK1bkbW97W5KRy1s///nPZ8qUKVvkfVmv9d636AFeavPnz+9L\nly6d7GUAAEB5K1asyN577z3Zy9iqjfUet9aW9d43+H0WLhMFAAAoSAwCAAAUJAYBAAAKEoMAAAAF\niUEAAICCxCAAAEBBYhAAANhq/ed//mdOOumk7LXXXpkzZ06OPvro/Pu///uLmuOrX/1q7rrrri20\nwsnjS+cBAICXxJJvvrgI25CFb3/zuK/33nPCCSdk0aJFueSSS5Iky5cvzwMPPJA3v3n8fUf76le/\nmmOPPTZz5syZ0HpfjHXr1m3xL513ZhAAANgqXXvttZk2bVrOOOOMZ8fmzp2bdevW5dhjj3127H3v\ne18uuuiiJMmZZ56ZOXPmZP/998/v/d7v5V/+5V9yxRVX5IMf/GDmzp2b//iP/8jy5ctzyCGHZP/9\n988JJ5yQRx55JEly2GGH5Xd+53dy6KGHZu+9986tt96ad73rXZk9e3Y+/OEPP3u8z3/+8znooIMy\nd+7cnH766Vm3bl2SZLvttssf//Ef5+CDD85NN920xd8fMQgAAGyV7rjjjrz1rW/d6O3XrFmTyy67\nLHfeeWduv/32fPjDH87P/dzP5bjjjss555yT5cuXZ6+99srJJ5+cT3ziE7n99tuz33775U/+5E+e\nneOVr3xlrr/++pxxxhlZsGBBzjvvvNxxxx256KKLsnr16qxYsSJf+tKX8s///M9Zvnx5pkyZki98\n4QtJkh/96EfZd999c/PNN+cXfuEXNvv78XwuEwUAAEjymte8JtOnT89v/MZv5JhjjnnO2cP1Hnvs\nsTz66KN5+9vfniRZtGhRTjzxxGdfP+6445Ik++23X/bZZ5/ssssuSZI3vvGNue+++3LjjTdm2bJl\nOfDAA5Mk//3f/52dd945STJlypT88i//8hb9G0cTgwAAwFZpn332yaWXXvpT41OnTs0zzzzz7O9r\n1659dvyWW27JNddck0suuSR/8zd/k2984xsv6pjbbLNNkuQVr3jFs8/X//7000+n955Fixblz//8\nz39q3+nTp2/xzwmO5jJRAABgq/SOd7wjTz31VC644IJnx2699dasW7cud911V5566qk89thjueaa\na5IkTzzxRB577LEcffTR+dSnPpXly5cnSV796lfn8ccfT5K89rWvzQ477JAbbrghSbJkyZJnzxJu\njMMPPzyXXnppHnzwwSQjl6Z+73vf2yx/74vlzCAAALBVaq3lsssuywc+8IGcffbZmT59embNmpVP\nfepT+dVf/dXsv//+mT17dg444IAkyeOPP54FCxZk7dq16b3nk5/8ZJLkpJNOyqmnnppzzz03l156\naRYvXpwzzjgjTz75ZN74xjfmc5/73Eavac6cOfnYxz6WI444Is8880ymTZuW8847L3vssccWeQ/G\n03rv42/Q2huSXJzkfyV5Jsn5vfe/bq19JMmpSR4aNv2D3vuVwz4fSnJKknVJ3t97v2oYPyrJXyeZ\nkuT/9t7PHsb3THJJktcluS3Jwt77j1tr2wzHfmuS1Une3Xu/d7z1zp8/vy9duvTFvAcAAMAWsGLF\niuy9996TvYyt2ljvcWttWe99/ob23ZjLRJ9O8ru9972THJLkva219V+w8cne+9zhsT4E5yQ5Kck+\nSY5K8unW2pTW2pQk5yV5Z5I5Sd4zap5PDHPNTvJIRkIyw89Heu9vSvLJYTsAAAAmaIMx2Hu/v/d+\n2/D88SQrkuw2zi4LklzSe3+q9/7dJCuTHDQ8Vvbev9N7/3FGzgQuaK21JO9Isv6TnYuTHD9qrsXD\n80uTHD5sDwAAwAS8qBvItNZmJTkgyc3D0Ptaa7e31i5sre0wjO2W5L5Ru60axl5ofMckj/ben37e\n+HPmGl5/bNgeAACACdjoGGytbZfkK0k+0Hv/rySfSbJXkrlJ7k/yl+s3HWP3vgnj4831/LWd1lpb\n2lpb+tBDD42xCwAAMBk2dI8SNt1E39uNisHW2rSMhOAXeu9/Nxz4gd77ut77M0kuyMhloMnImb03\njNp9ZpIfjjP+cJLtW2tTnzf+nLmG11+bZM3z19d7P7/3Pr/3Pn/GjBkb8ycBAABb2PTp07N69WpB\nuAX03rN69epMnz59k+fY4FdLDJ/R+2ySFb33vxo1vkvv/f7h1xOS3DE8vyLJ37bW/irJrklmJ7kl\nI2f5Zg93Dv1BRm4y87977721dm2SX8nI5wgXJbl81FyLktw0vP6N/jL9l3TbwoWTvYSX1LwlSyZ7\nCQAAvMzNnDkzq1atiqv3tozp06dn5syZm7z/xnzP4M8nWZjk26215cPYH2TkbqBzM3LZ5r1JTk+S\n3vudrbUvJ7krI3cifW/vfV2StNbel+SqjHy1xIW99zuH+X4/ySWttY8l+deMxGeGn0taayszckbw\npE3+SwEAgJfUtGnTsueee072MngBG4zB3vuNGfuze1eOs8/Hk3x8jPErx9qv9/6d/M9lpqPH1yY5\ncUNrBAAA4MV5UXcTBQAAYOsgBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAA\nKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYB\nAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJ\nQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABA\nQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgA\nAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAAKEgM\nAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAK\nEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFDQ1MleAMBkum3hwslewktq3pIlk70EAOBlwplB\nAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBB\nYhAAAKCgqZO9AHi5u23hwslewktq3pIlk70EAABeAs4MAgAAFCQGAQAAChKDAAAABYlBAACAgsQg\nAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAg\nMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAA\nKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYB\nAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJ\nQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABA\nQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgA\nAFDQBmOwtfaG1tq1rbUVrbU7W2v/Zxh/XWvt6tbaPcPPHYbx1lo7t7W2srV2e2tt3qi5Fg3b39Na\nWzRq/K2ttW8P+5zbWmvjHQMAAICJ2Zgzg08n+d3e+95JDkny3tbanCRnJrmm9z47yTXD70nyziSz\nh8dpST6TjIRdkrOSHJzkoCRnjYq7zwzbrt/vqGH8hY4BAADABGwwBnvv9/febxueP55kRZLdkixI\nsnjYbHGS44fnC5Jc3Ed8K8n2rbVdkhyZ5Ore+5re+yNJrk5y1PDaa3rvN/Xee5KLnzfXWMcAAABg\nAl7UZwZba7OSHJDk5iSv773fn4wEY5Kdh812S3LfqN1WDWPjja8aYzzjHAMAAIAJ2OgYbK1tl+Qr\nST7Qe/+v8TYdY6xvwvhGa62d1lpb2lpb+tBDD72YXQEAAEraqBhsrU3LSAh+off+d8PwA8Mlnhl+\nPjiMr0ryhlG7z0zyww2MzxxjfLxjPEfv/fze+/ze+/wZM2ZszJ8EAABQ2sbcTbQl+WySFb33vxr1\n0hVJ1t8RdFGSy0eNnzzcVfSQJI8Nl3heleSI1toOw41jjkhy1fDa4621Q4Zjnfy8ucY6BgAAABMw\ndSO2+fkkC5N8u7W2fBj7gyRnJ/lya+2UJN9PcuLw2pVJjk6yMsmTSX4tSXrva1prf5rk1mG7j/be\n1wzPfzPJRUm2TfKPwyPjHAMAAIAJ2GAM9t5vzNif60uSw8fYvid57wvMdWGSC8cYX5pk3zHGV491\nDAAAACbmRd1NFAAAgK2DGAQAAChIDAIAABS0MTeQAYCfSbctXDjZS3jJzFuyZLKXAMDPGGcGAQAA\nChKDAAAABYlBAACAgsQgAABAQW4gAwD8zKl0c6DEDYKALcOZQQAAgILEIAAAQEFiEAAAoCAxCAAA\nUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwC\nAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoS\ngwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACA\ngsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAA\nAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAY\nBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAU\nJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAA\nAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQg\nAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAg\nMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAA\nKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYB\nAAAKEoMAAAAFTZ3sBQAAwGi3LVw42Ut4ycxbsmSyl0BhzgwCAAAUJAYBAAAKEoMAAAAFiUEAAICC\nxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAA\noCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAACpo62QsAAABquG3hwslewktq3pIlk72EcTkzCAAAUJAY\nBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgjYYg621C1trD7bW7hg19pHW2g9aa8uHx9GjXvtQ\na21la+3u1tqRo8aPGsZWttbOHDW+Z2vt5tbaPa21L7XWXjmMbzP8vnJ4fdbm+qMBAACq25gzgxcl\nOWqM8U/23ucOjyuTpLU2J8lJSfYZ9vl0a21Ka21KkvOSvDPJnCTvGbZNkk8Mc81O8kiSU4bxU5I8\n0nt/U5JPDtsBAACwGWwwBnvv1ydZs5HzLUhySe/9qd77d5OsTHLQ8FjZe/9O7/3HSS5JsqC11pK8\nI8mlw/6Lkxw/aq7Fw/NLkxw+bA8AAMAETeQzg+9rrd0+XEa6wzC2W5L7Rm2zahh7ofEdkzzae3/6\neePPmWt4/bFhewAAACZoU2PwM0n2SjI3yf1J/nIYH+vMXd+E8fHm+imttdNaa0tba0sfeuih8dYN\nAABANjEGe+8P9N7X9d6fSXJBRi4DTUbO7L1h1KYzk/xwnPGHk2zfWpv6vPHnzDW8/tq8wOWqvffz\ne+/ze+/zZ8yYsSl/EgAAQCmbFIOttV1G/XpCkvV3Gr0iyUnDnUD3TDI7yS1Jbk0ye7hz6CszcpOZ\nK3rvPcm1SX5l2H9RkstHzbVoeP4rSb4xbA8AAMAETd3QBq21LyY5LMlOrbVVSc5KclhrbW5GLtu8\nN8npSdJ7v7O19uUkdyV5Osl7e+/rhnnel+SqJFOSXNh7v3M4xO8nuaS19rEk/5rks8P4Z5Msaa2t\nzMgZwZMm/NcCAACQZCNisPf+njGGPzvG2PrtP57k42OMX5nkyjHGv5P/ucx09PjaJCduaH0AAAC8\neBO5mygAAAA/o8QgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICC\nxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAA\noCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgE\nAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQk\nBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAA\nBYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAA\nAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAx\nCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAo\nSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEA\nAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlB\nAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBB\nYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAA\nUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwC\nAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoS\ngwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACA\ngsQgAABAQWIQAACgoA3GYGvtwtbag621O0aNva61dnVr7Z7h5w7DeGutndtaW9lau721Nm/UPouG\n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\ne/9OkreMMb46yeFjjPck732BuS5McuEY40uT7LupawQAAGBsW+KrJQAAAHiZE4MAAAAFiUEAAICC\nxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAA\noCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgE\nAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQk\nBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAA\nBYlBAACAgsQgAABAQWIQAACgIDEIAABQ0NTJXgAAAFDDP+2472Qv4SU1b7IXsAHODAIAABQkBgEA\nAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoCAxCAAAUJDvGQQA4GWl0nfRvdy/h46tmzODAAAABYlB\nAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBB\nYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAAgILEIAAAQEFiEAAAoKCpk72A\nrcU/7bjvZC/hJTVvshcAAABMiDODAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwC\nAAAUJAYBAAAKEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoS\ngwAAAAWJQQAAgILEIAAAQEFiEAAAoKCpk70AgMn0TzvuO9lLeEnNm+wFAAAvG84MAgAAFCQGAQAA\nChKDAAAABYlBAACAgtxABjbADUYAXn783wwwcc4MAgAAFCQGAQAAChKDAAAABYlBAACAgtxABoCt\nVqWbjLjBCAAvljODAAAABYlBAACAgsQgAABAQWIQAACgIDEIAABQkBgEAAAoSAwCAAAUJAYBAAAK\nEoMAAAAFiUEAAICCxCAAAEBBYhAAAKAgMQgAAFCQGAQAAChIDAIAABQkBgEAAAoSgwAAAAWJQQAA\ngILEIAAAQEFiEAAAoCAxCAAAUJAYBAAAKEgMAgAAFCQGAQAAChKDAAAABYlBAACAgsQgAABAQWIQ\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7f13b92bd2b0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = pl.figure(figsize(15,15))\n",
    "\n",
    "#instad of plotting with matplotlib i.e. plot() i use the plot method in pandas\n",
    "norm_w = 1\n",
    "((df['date'][df['User Type'] == 'Subscriber'].groupby([df['date'].dt.weekday]).count()) / norm_w).plot(kind=\"bar\", \n",
    "                                                                                         color='IndianRed', \n",
    "                                                                                         label='Subscriber')\n",
    "\n",
    "norm_m = 1\n",
    "ax = ((df['date'][df['User Type'] == 'Customer'].groupby([df['date'].dt.weekday]).count()) / norm_m).plot(kind=\"bar\", \n",
    "                                                                                              color='SteelBlue', \n",
    "                                                                                              alpha=0.5,\n",
    "                                                                                              label='Customer')\n",
    "\n",
    "tmp = ax.xaxis.set_ticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], fontsize=20)\n",
    "pl.legend()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PUI2016_Python3",
   "language": "python",
   "name": "pui2016_python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
