{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "##### **A Quick Look on COVID19 Situation of US and Your Neighborhood**\n",
    "-----------------------"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Table of Contents\n",
    "[1. Motivation](#motivation)<br> \n",
    "[2. Data](#DATA)<br> \n",
    ">   [2.1. Data Stucture](#DATA)<br>\n",
    ">   [2.2. Data Acquisition](#Dataacquisition)<br>\n",
    "    \n",
    "[3. Hypothesis Testing](#hypo)\n",
    "> [3 i. Set-Up](#setup)<br>\n",
    "> [3 ii. Welch Test Statistic & Student t- test](#welch)<br>\n",
    "> [3 iii. P-value](#pval)<br>\n",
    "\n",
    "[4. Conclusion](#conclude)\n",
    "\n",
    "[5. Appendix](#Appendix)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Motivation\n",
    "<a id=\"motivation\"> </a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-09T16:59:11.484095Z",
     "start_time": "2020-04-09T16:59:11.482090Z"
    }
   },
   "source": [
    "## Background"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **\"The death of one man is a tragedy. The death of millions is a statistic.\"**    - Original by Kurt Tucholsky as a Joke"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "On Apr 4th 2020, there are more than 1 **million** COVID19 case worldwide and more than 300,000 cases in US and keep surging. 2/3 of Americans were under lockdown. \n",
    "\n",
    "On one side, people don't know what happens around their neighborhood. On the other side, politicians has been making conflict and chaos statement about the situation. \n",
    "\n",
    "The rationale behind this project is that we want to awake people before they are getting numb with the situation. As a future Data Scientist, what can we do to help people?\n",
    "\n",
    "Providing **relevant and precise** information to people."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Goal"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There are two main objectives of this project, one is to provide an easy access method for people getting correct information of their neighborhood. \n",
    "\n",
    "The second is to test one of the scary statement made by Mayor of Los Angeles that LA was 5 days behind NYC on few days ago.\n",
    "\n",
    "\n",
    "What's more, we will try exploring what can we learned from South Korea which is treated as the most successful country in controlling the COVID-19.\n",
    "\n",
    "----------------"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "# Where do we get data?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "One of the barriar of people getting infomation they need is various information source. We choosed most creditable and widely cited data source from Johns Hopkins. Additional, we will webstrap text content from press releases and transform into data we need.\n",
    "\n",
    "**Source** See [Appendix - Data Source](#DataSource)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Structure\n",
    "\n",
    "<a id=\"DATA\"> </a>\n",
    "\n",
    "We obtain two types of data representing the COVID-19 situation.\n",
    "* **Test Data**\n",
    "\n",
    "    * Date\n",
    "    * Country (Only for US and Korea)\n",
    "    * States (Only for US)\n",
    "    * Number of Test Perform\n",
    "    * Number of Test Positive\n",
    "    * Number of Test Negative    \n",
    "    \n",
    "    \n",
    "* **Case Data**\n",
    "\n",
    "    * Date\n",
    "    * Country \n",
    "    * States (Only for US)\n",
    "    * Community (Only for LA County)\n",
    "    * Number of Confirmed Case\n",
    "    * Number of Death Case\n",
    "    * Number of Recovered Case   \n",
    "    * Number of Active Case   \n",
    "    \n",
    "Jump to [EDA](#EDA) if you are not interested in web straping and data cleaning.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data acquisition\n",
    "<a id=\"Dataacquisition\"> </a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Beside the data were well organized and available for download, one most important technique for obtaining data is **web scraping**."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Web Scraping"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here is a demonstration of web straping for sample page of a press release of the Department of Public Health of Los Angeles County.\n",
    "<img src=\"images/sample_data_LA1.png\" />\n",
    "\n",
    "Every page would generate one single record through web straping. We could obtain the Date of a single record from the top left of page. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<img src=\"images/sample_data_LA2.png\" />\n",
    "From the bottom, we could get confirmed cases and its infective density for each community in LA county."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The process is implement by a pre-define webscrap class `webscrape` including functions for getting tables, get text and get urls. The class definition is stored as `./src/web_scraping`.\n",
    "Sample data as below."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "| city | April 08, 2020 | \n",
    "|--------------------------|----|\n",
    "| City of Agoura Hills     | 19 | \n",
    "| City of Alhambra\t     | 26 | \t\n",
    "| City of Arcadia     | 17 | \t\t\t\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Pipeline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-09T21:14:07.182517Z",
     "start_time": "2020-04-09T21:14:07.177179Z"
    }
   },
   "source": [
    "Before merge everyday data, we need to double check data on consistency. Figure out some data were build on inconsist city name.\n",
    "\n",
    "| city | March 26, 2020 | \n",
    "|--------------------------|----|\n",
    "| Agoura Hills     | 5 | \n",
    "| Alhambra\t     | 8 | \t\n",
    "| Arcadia     | 6 | \t\t\t\n",
    "\n",
    "We create rules to transform city name in a same scale and merge into a ready dataset.\n",
    "<a id=\"communitylevel\"> </a>\n",
    "\n",
    "| city | April 08, 2020 | April 07, 2020 | April 06, 2020 | ... | March 26, 2020 |... |\n",
    "|--------------------------|-------|-------|-------|-------|-------|------|\n",
    "| City of Agoura Hills     | 19 |  19 | 18 | ... | 5 |... |\n",
    "| City of Alhambra\t     | 26 |  24 | 22 | ... | 8 |  ... | \t\t\t\t\n",
    "| City of Arcadia     | 17 |  17 | 16 | ... | 6 |... | \t\t\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "------------------------\n",
    "\n",
    "# EDA<a id=\"EDA\"> </a>\n",
    "\n",
    "-------------------"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## EDA on Case Data\n",
    "\n",
    "There are two types of case data, one is cross-section data describe a single day all kind of record of different area. The other one is a panel data focused on one attribute of different area over time.\n",
    "\n",
    "\n",
    "### Cross-section data\n",
    "\n",
    "First, we takes a look at the schema of the dataset.\n",
    "\n",
    "|  #  | Column        |  Non-Null | Count | Dtype  | \n",
    "| --- |  ------        |   --------| ------ |  -----  | \n",
    "| 0  | FIPS           | 2603 | non-null |  float64| \n",
    "| 1  | Admin2         | 2614 | non-null |  object | \n",
    "| 2  | Province_State | 2703 | non-null |  object | \n",
    "| 3  | Country_Region | 2883 | non-null |  object | \n",
    "| 4  | Last_Update    | 2883 | non-null |  object | \n",
    "| 5  | Lat            | 2823 | non-null |  float64 | \n",
    "| 6  | Long_          | 2823 | non-null |  float64 | \n",
    "| 7  | Confirmed      | 2883 | non-null |  int64  | \n",
    "| 8  | Deaths         | 2883 | non-null |  int64  | \n",
    "| 9  | Recovered      | 2883 | non-null |  int64  | \n",
    "| 10 | Active         | 2883 | non-null |  int64  |\n",
    "| 11 | Combined_Key   | 2883 | non-null |  object | \n",
    "\n",
    "The variables we most care about are `Confirmed, Deaths, Recovered, Active` 4 columns. \n",
    "\n",
    "Hence, we will explore the inner relationship among them through a pairwise scatter plot through `seaborn`.\n",
    "\n",
    "image\n",
    "\n",
    "As we can see from the plots, **all the death, recovered and active case has a positive relationship on confirmed case.** So if we want to see a small number in death, we need to see a low level of confirm case.\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Panel Data\n",
    "\n",
    "We takes a look at the schema of panel.\n",
    "\n",
    "First, we takes a look at the schema of the dataset.\n",
    "\n",
    "|  #  | Column        |  Non-Null | Count | Dtype  | \n",
    "| --- |  ------        |   --------| ------ |  -----  | \n",
    "| 0  | Province/State | 82 | non-null |  object | \n",
    "| 1  | Country_Region | 263 | non-null |  object | \n",
    "| 2  | Lat            | 263 | non-null |  float64 | \n",
    "| 3  | Long          | 263 | non-null |  float64 | \n",
    "| 4  | 1/22/20 | 263 | non-null |  int64 | \n",
    "| ...  | ...    | 263 | non-null |  int64 | \n",
    "| 81  | 4/8/20    | 263 | non-null |  int64 | \n",
    "\n",
    "For time series data, trend is much more important. As we can see below, **the increasing trend of confirmed cases has been acclarating since Early March** without a clear sign for slowing down.\n",
    "\n",
    "image"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The recent growth of confirmed cases were contributed by US and West Euro countries. And US has shown the most worried sign in term of the most case without a slowing down trend.\n",
    "\n",
    "image\n",
    "\n",
    "Another takeaway from this plot, there are two coutries, China and South Korea were considered well controlled the COVID-19 while South Korea's example were repeatable which means massive test, quick tracking and quarantine.\n",
    "\n",
    "Next step, we will try to explore the relationship between Korean testing and cases."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## EDA on Tesing Data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's take a flight to seoul CDC and robbed their press release drafts and type into our computer.\n",
    "\n",
    "As usual, we first check on the data structure.\n",
    "\n",
    "\n",
    "|  #  | Column        |  Non-Null | Count | Dtype  | \n",
    "| --- |  ------        |   --------| ------ |  -----  | \n",
    "| 0  | Total | 59 | non-null |  int64 | \n",
    "| 1  | PCR_Confirmed | 59 | non-null |  int64 | \n",
    "| 2  | PCR_Discharged            | 59 | non-null |  int64 | \n",
    "| 3  | PCR_Isolated          | 59 | non-null |  int64 | \n",
    "| 4  | PCR_Deceased | 59 | non-null |  int64 | \n",
    "| 5  | Being_tested | 59 | non-null |  int64 | \n",
    "| 6  | Tested_negative | 59 | non-null |  int64 | \n",
    "\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The `PCR_Confirmed` means the number of patient tested positive on the coronavirus through PCR method which is equivalent to confirmed case we talked before.\n",
    "\n",
    "Since all variables was in a accumulated scale, we made a differentiate of the data on a one day lag. For instance, `new_testing` \n",
    "\n",
    "$$new testing(Day n)  =  Total(Day n)  -  Total(Day n - 1)$$\n",
    "\n",
    "and calulate the positive_rate by\n",
    "\n",
    "$$positive rate(Day n)  =  \\frac{PCR Confirmed(Day n)}{new testing(Day n)}$$\n",
    "\n",
    "We use similar method as before that creating pairwise scatter plot.\n",
    "\n",
    "image\n",
    "\n",
    "We did not observe a clear pattern between `new_testing` and `positive_rate`. "
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Back to LA\n",
    "\n",
    "Let travel back to Los Angeles, California, US on a time which seems not a good time for international travel.\n",
    "\n",
    "Although california has the most population among the states, california is not even the top 3 and has a relative flatten curve.\n",
    "\n",
    "image\n",
    "\n",
    "However, state is to large for us to perceive how is things going around. In order to fix the problem, we create two maps."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Map"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## US Map\n",
    "Since the case data includes the geographic information, we could plot all the point onto a map by `folium` library.\n",
    "\n",
    "* Radius: Larger indicates larger number of case\n",
    "\n",
    "* Color: Sharper color indicates larger number of case\n",
    "\n",
    "image\n",
    "\n",
    "We could easily identify some epicenter of US, most serious in NY, and then Florida and California.\n",
    "\n",
    "To show more, we integrate a line chart showing the 7 days trend by using `altair` library and passing `JSON Graph` on the marker.\n",
    "\n",
    "image\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## LA Map\n",
    "\n",
    "To learn more on local, we want a map on community level. However, [the community level data](#communitylevel) that we web-straped were not integrated with geographic information. Fortunately, we find the `GeoJSON` of LA community file from data.gov.\n",
    "\n",
    "In this case, we use **choropleth map** to present the boundaries in the communities and also cluster the marker to show some clearer. In following map, the color shows the infective density which is calculated by number of confirmed case per 100,000 population.\n",
    "\n",
    "image\n",
    "\n",
    "We can tell that WeHo and BH have the most difficult situation in LA.\n",
    "\n",
    "Similarly, we provide community related information on the marker. \n",
    "\n",
    "image\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Hypotheses Test\n",
    "\n",
    "Another reason people getting numb with this situation is that politicians sometimes governors making overstated or downplaying statements which confused a lot of people.\n",
    "\n",
    "One of scary story was told by LA Mayor Eric Garcetti.\n",
    "\n",
    "image\n",
    "\n",
    "We will exam his hypotheses through a **Hypotheses test**.\n",
    "\n",
    "To be more specific, we rewrite his statement as the null hypothesis.\n",
    "\n",
    "> Null hypothesis H0: From now till Apr 1st (5 days after) LA county has same case level or even higher than NYC in Mar 23rd to Mar 27th. \n",
    "\n",
    "> Alternative hypothesis H1: From now till Apr 1st (5 days after) LA county has less case level than NYC in Mar 23rd to Mar 27th. \n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "For such small sample size, the best option right now is Mann-Whitney U test. Mathmatically,\n",
    "\n",
    ">$$H_0 = P(NY case > LA case)=0.5$$\n",
    ">$$H_1 = P(NY case > LA case)>0.5$$\n",
    "\n",
    "By `scipy.stats` module, we could easily calculated the P-value and see original statement is valid or not under a signficant level 0.05.\n",
    "\n",
    "> P-value of the U-test is 0.006. \n",
    "We **reject the null hypotheses** on a signficant level 0.05.\n",
    "\n",
    "It would be seen in another way of plotting.\n",
    "\n",
    "image\n",
    "\n",
    "NYC cases is much serious in terms of quantity and growth rate."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Summary\n",
    "\n",
    "## Takeaway"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Real takeaway\n",
    "\n",
    "* Stay at home.\n",
    "* Wear a mask and bring a hand sanitizer if you must go out.\n",
    "* Avoid close contact.\n",
    "\n",
    "Most important:\n",
    "\n",
    "**Share information to people you love. Talk to people who ever share their love with you.**\n",
    "\n",
    "Learn more on data science.\n",
    "\n",
    "> **\"It is only a tiny dust of this era, but to an ordinary family, is too much they can take.\"**\n",
    "\n",
    "> From a Chinese Poet lives in Wuhan the original epicenter in China.\n",
    "\n",
    "Don't let the one you loved be the dust of the era."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Appendix\n",
    "<a id=\"Appendix\"> </a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Data Source**\n",
    "<a id=\"DataSource\"> </a>\n",
    "- **Getting CSSE data on github**\n",
    "\n",
    "    source: https://github.com/CSSEGISandData/COVID-19 by Johns Hopkins CSSE\n",
    "\n",
    "\n",
    "- **Gather state testing data thru API**\n",
    "\n",
    "    source: https://covidtracking.com/data \n",
    "    - US Testing in Time Series https://covidtracking.com/api/us/daily.csv\n",
    "    - States Historical Data https://covidtracking.com/api/states/daily.csv\n",
    "\n",
    "\n",
    "- **Webscrap korean testing data**\n",
    "\n",
    "    Source: CDC of South Korean\n",
    "    - sample data https://www.cdc.go.kr/board/board.es?mid=&bid=0030&act=view&list_no=366735\n",
    "    \n",
    "    \n",
    "- **Webscrap LA community level data**\n",
    "\n",
    "    Source: The Department of Public Health of Los Angeles County\n",
    "    - sample data http://publichealth.lacounty.gov/phcommon/public/media/mediapubhpdetail.cfm?prid=2298\n",
    "    \n",
    "    \n",
    "- **GeoJSON of LA community**\n",
    "\n",
    "    Source: Data.gov\n",
    "    https://catalog.data.gov/harvest/los-angeles-data-json\n",
    "---------------------------------"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**GitHub Links**\n",
    "\n",
    "* Repository: https://github.com/constiny/COVID19\n",
    "\n",
    "* Jupyter Notebook: https://github.com/constiny/COVID19/blob/master/covid19.ipynb"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.6.5"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": true
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
