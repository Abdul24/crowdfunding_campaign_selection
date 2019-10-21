# Finding the Probability of Success for Crowdfunding Campaigns [Machine Learning]

#### -- Project Status: [Completed]

## Project Intro/Objective
Kickstarter is a US based global crowd funding platform focused on bringing funding to creative projects. Since the platform’s launch in 2009, the site has hosted over 159,000 successfully funded projects with over 15 million unique backers. Kickstarter uses an “all-or-nothing” funding system. This means that funds are only dispersed for projects that meet the original goal set by the creator.

Kickstarter earns 5% commission on projects that are successfully funded. Currently, less than 40% of projects on the platform succeed. The objective is to build a model that can take in a campaign description (campaign duration, category, fundraising amount, etc.) and produce a probability of success. Kickstarter would then use this information - along with other factors such as cost of promotion, promotion budget, etc. - to determine which campaigns to promote with the end goal of increasing the percentage of successful campaigns.

### Collaborators
|Name     |  Github Page   |  Personal Website  |
|---------|-----------------|--------------------|
|Misha Berrien | [mishaberrien](https://github.com/mishaberrien)| [www.mishaberrien.com](https://mishaberrien.com/)  |

### Methods Used
* Machine Learning
* Data Visualization
* Predictive Modeling

### Technologies
* Python
* Pandas, jupyter

## Project Description
In order to increase the number of successful campaigns, we propose two related solutions:
* Predict Successful Campaigns and promote those with the lowest predicted probability of being successful.
* Contact creators from those campaigns that are just below the “success” margin and give them insights that will help them succeed.

## Getting Started

1. Clone this repo.
2. The dataset can be found in the data folder [here](https://github.com/mishaberrien/crowdfunding_campaign_selection/tree/master/data/02_intermediate).
3. In order to reproduce results, run the notebook found in the "results" located [here](https://github.com/mishaberrien/crowdfunding_campaign_selection/tree/master/results).
4. The data processing/transformation scripts are being kept in the src folder [here](https://github.com/mishaberrien/crowdfunding_campaign_selection/tree/master/src)

5. A data dictionary can be found in the references folder [here](#)


## Featured Notebooks/Analysis/Deliverables
* [Technical Results Notebook](#)

---

This file structure is based on the [DSSG machine learning pipeline](https://github.com/dssg/hitchhikers-guide/tree/master/sources/curriculum/0_before_you_start/pipelines-and-project-workflow).
