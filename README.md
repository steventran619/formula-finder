<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]](https://mit-license.org/)
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/steventranx/) -->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ChocolateTaco/formula-finder">
    <img src="media/bottle_search_icon.png" alt="Logo" width="80">
  </a>

<h3 align="center">Formula Finder</h3>
  <p align="center">
    Find availability of baby formula online without any hassle!
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
Purpose of this project is to help new parents find baby formula during the 2022 Baby Formula Shortage. This application scrapes several online retailers for their baby formula inventory, and sends a report to a list of email subscribers. This project has benefitted me personally and a few other moms in our circle in finding formula. The focus is primarily on [Store Brand Formula](https://www.storebrandformula.com/).
<div align="center">
  <a href="https://github.com/ChocolateTaco/formula-finder">
    <img src="https://github.com/ChocolateTaco/formula-finder/blob/main/media/formula_shortage.gif" alt="Images of low stock of baby formula in stores" width="300">
  </a>
 </div>

<!-- ### Built With

* [Selenium](https://www.selenium.dev/)
* [Python](https://www.python.org/) -->

### How it Works
<div align="center">
  <img src="https://github.com/ChocolateTaco/formula-finder/blob/main/media/ff_flow.png" alt="Flow Diagram of How Formula Finder Works" height="325">
</div>
Formula Finder can run on any OS. It just requires Python and Google Chrome to get it up and running. Formula Finder scrapes the web using Selenium, for product inventory information. Afterwards it generates an HTML report using PrettyTables. Then Formula Finder logs into an AOL email account, and sends the report out via BCC to a list of email subscribers or recipients.

### Prerequisites
* [Python](https://www.python.org/)
* [Google Chrome Browser](https://www.google.com/chrome/)
* [Chrome Driver](https://chromedriver.chromium.org/downloads/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ChocolateTaco/formula-finder.git
   ```
2. Install the requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
3. Replace the applicable [chrome driver](https://chromedriver.chromium.org/downloads/) in the /input_files/ directory, relevant to your version of Google Chrome
4. [Sign up for an AOL Email Address](https://mail.aol.com) (haha yes they still exist)
5. In AOL Account Security settings, "Generate app password" or One Time Password (OTP)
6. In /input_files/ directory, create "emailAlert.txt"
7. In "emailAlert.txt" add the AOL email address and the one time password (separated by a line break). *NOT the password of the account, but the One Time Password*
   ```bash
   emailAddress@aol.com
   emailsOneTimePassword
   ```
8.  In /input_files/emailSubscribers.txt, update the list of email recipients
9.  In the installation directory, run the run.py file
   ```sh
   python3 run.py
   ```   

<!-- ROADMAP -->
## Roadmap

- [x] Scrape StoreBrand Formula Online Retailers
    - [x] Costco.com
      - [ ] Optimize search speed
    - [x] Target.com
    - [x] Amazon.com
    - 🛑 Kroger.com (Anti-Robot Friendly)
    - 🛑 SamsClub.com (Anti-Robot Friendly)
    - 🛑 Walmart.com (Anti-Robot Friendly)
- [x] Generate Report
  - [x] Gather Product Name, Availability, Price, URL
  - [ ] Gather Last In Stock Date
  - [ ] Shorten URL
- [ ] Email Results to list of email subscribers
    - [x] BCC emails to an email list using AOL SMTP 
    - [ ] Unsubscribe Feature
- [x] Create Virtual Environment
- [ ] Automatic Scheduling 

## Design FAQs

#### Why Selenium over BeautifulSoup or Scrapy?

I wanted to learn a new stack such as Selenium. I will also be creating other web applications in the future. I liked that Selenium has options to perform web based GUI automation and testing.

#### Okay, what about Google Chrome over Firefox and Safari?
One of the goals was to have it be cross compatible with operating systems such as Windows, Mac, and Linux. Firefox also requires additional driver (Gecko Driver) resource that would take an extra step. 

#### Why are you using AOL Email?

As of June 2022, Gmail removed the "less secure" mail settings now making python's SMTPLIB incompatible (or more challenging). Went with AOL for the nostalgia and wide range of available email addresses.

#### Will you be re-working Kroger, Walmart, and Sams Club?

Maybe. For the time being those domains have strong capchas and bot protection, making it more challenging for projects like Formula Finder to scrape.


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [JimSC](https://github.com/jimdevops19) for the amazing Selenium lessons!


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
