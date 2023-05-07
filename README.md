## What is it?
basically it is collection of scripts that shows current COVID-19 data and RSS feed, and sends it to email

How it works?
- [it makes a chart that shows recent COVID-19 data in any EU (+ EEA) country](covid_stats.ipynb)
- [checks RSS feeds for new entries](get_feed.py)
- [sends it all to my email](send_email.py)

## How can I use it myself?
All you need to do is add few github secrets ([see yaml](.github/workflows/main.yml)), change your country in the [notebook](covid_stats.ipynb), and change your email provider in [send_email](send_email.py) 

## Acknowledgments
### Data
[this program uses data from ECDC](https://www.ecdc.europa.eu/en/publications-data/data-covid-19-vaccination-eu-eea)

### Packages
this program is using some 3rd-party packages, you can find all of them in [requirements.txt](requirements.txt). 

### Per package acknowledgments
each script/program/file may also have links to some resources.
