## What is it?
basically it is collection of scripts that shows current COVID-19 data and RSS feed and sends it to email

This script is doing:
- [showing current cases and share of positive test](covid_stats.ipynb)
- [checks rss feeds if any new posts](get_feed.py)
- [sends it to email](send_email.py)

## I want to use it on my own 
sure, I'm glad you like it 😄. All you need to do is add few github secrets ([see yaml](.github/workflows/main.yml)), change your country in [notebook](covid_stats.ipynb) and your email provider in [send_email](send_email.py) 

### bruh why yahoo?
I have choseen yahoo because you can make account there easly and forget about it until yahoo will eventually shut down lol

Feel free to use however it suits you ☺️

## Acknowledgements
### Data
Hannah Ritchie, Edouard Mathieu, Lucas Rodés-Guirao, Cameron Appel, Charlie Giattino, Esteban Ortiz-Ospina, Joe Hasell, Bobbie Macdonald, Diana Beltekian and Max Roser (2020) - "Coronavirus Pandemic (COVID-19)". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/coronavirus' [Online Resource]

### Packages
this program is using some packages, you can find all of them in [requirements.txt](requirements.txt)

### Per package acknowledgements
each program may also have some link to some sources, I recommend you to check them out, because they are pretty helpful (at least to me)