<!-- header -->
<div align="center">
    <p>
    <!-- Header -->
        <img width="100px" src="/static/images/readme_logo.png"  alt="mission-to-mars" />
        <h2>Mission2 Mars</h2>
        <p><i>The front page of Mars</i></p>
    </p>
    <p>
    <!-- Shields -->
        <a href="https://github.com/armck-hub/mission-to-mars/LICENSE">
            <img alt="License" src="https://img.shields.io/github/license/armck-hub/mission-to-mars.svg" />
        </a>
        <a href="https://github.com/armck-hub/mission-to-mars/actions">
            <img alt="Tests Passing" src="https://github.com/armck-hub/mission-to-mars/workflows/CI/badge.svg" />
        </a>
        <a href="https://codecov.io/gh/armck-hub/mission-to-mars">
            <img alt="Code Coverage" src="https://codecov.io/gh/armck-hub/mission-to-mars/branch/master/graph/badge.svg" />
        </a>
        <a href="https://github.com/armck-hub/mission-to-mars/issues">
            <img alt="Issues" src="https://img.shields.io/github/issues/armck-hub/mission-to-mars" />
        </a>
        <a href="https://github.com/armck-hub/mission-to-mars/pulls">
            <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/armck-hub/mission-to-mars" />
        </a>
        <a href="https://stackshare.io/armck-hub/mission-to-mars">
            <img alt="StackShare.io" src="http://img.shields.io/badge/tech-stack-0690fa.svg?label=StackShare.io">
        </a>
    </p>
    <p>
    <!-- Links -->
        <a href="https://github.com/armck-hub/mission-to-mars/issues/new/choose">Report Bug</a>
        ·
        <a href="https://github.com/armck-hub/mission-to-mars/issues/new/choose">Request Feature</a>
    </p>
</div>
<br>
<br>

<!-- Description -->
Mission To Mars is an application that displays various important and up-to-date details on your favorite Red Planet.

The application uses web-scraping and other techniques to gather information from around the internet and then display it for your consumption.

Here's why Mission To Mars is important:
* To prepare you for your trip to Mars - coming sooner than you think!

#### Some Important Notes
- A MongoDB is not included in the dev environment and requires one be set up and available locally.
- Deployment on Heroku requires a `requirements.txt` file for dependency installation. To generate a file from poetry's dev virtual environment use `poetry export -f requirements.txt -o requirements.txt --without-hashes`.
