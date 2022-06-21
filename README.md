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
    <img src="https://github.com/ChocolateTaco/formula-finder/blob/main/media/formula_shortage.gif" alt="Logo" width="300">
  </a>
 </div>

### Built With

* [Selenium](https://www.selenium.dev/)
* [Python](https://www.python.org/)

### Prerequisites
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
3. Add the applicable [chrome driver](https://chromedriver.chromium.org/downloads/) to the /input_files/ directory, relevant to your version of Google Chrome
4. [Sign up for an AOL Email Address](https://mail.aol.com) (haha yes they still exist)
5. In AOL Account Security settings, "Generate app password" or One Time Password (OTP)
6. In /input_files/ directory, create "emailAlert.txt"
7. In "emailAlert.txt" add the AOL email address and the one time password (separated by a line space). Note NOT the email address' password, but the One Time Password
   ```
   emailAddress@aol.com
   emailsOneTimePassword
   ```
8.  In /input_files/emailSubscribers.txt, update the list of email recipients
9.  In the installation directory, run the run.py filet
   ```sh
   python3 run.py
   ```   

<!-- ROADMAP -->
## Roadmap

- [x] Scrape StoreBrand Formula Online Retailers
    - [x] Costco.com
      - [ ] Optimize Costco speed
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

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [JimSC for the Selenium lessons!](https://github.com/jimdevops19)


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
