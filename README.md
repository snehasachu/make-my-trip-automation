# MakeMyTrip - Test Automation

## Overview

This project involves creating and automating test cases for a new feature introduced by MakeMyTrip for planning international trips from India. The goal is to ensure the feature functions correctly and meets user expectations through comprehensive test case development and automation.

## Objectives

- Write automated test cases for the international trip planning feature.
- Identify, document, and create additional smoke test cases.
- Ensure the functionality works correctly and meets specified requirements.
- Identify and document any errors or issues in the feature flow.
- Provide detailed documentation and clear test reports.

## Key Features

- **Feature Navigation and Interaction:** Testing navigation to the "Flights" page and interaction with elements like dropdowns and buttons.
- **Test Case Development:**
  - **Functional Test Cases:** Validate the core functionality of selecting cities, travel dates, and searching for flights.
  - **Smoke Test Cases:** Basic scenarios to verify core functionality.
- **Automation Flow:**
  - **Navigation and Selection:** Automate the process of selecting departure and destination cities, setting travel dates, and searching for flights.
  - **Flight Search and Validation:** Validate search results and availability based on predefined criteria.
- **Performance:** Ensure efficient execution of automation scripts.
- **Documentation and Reporting:**
  - **Setup Instructions:** Clear documentation for setting up and executing tests.
  - **Test Reports:** Detailed HTML reports for test results.

## Framework and Tools

- **Cucumber BDD:** Write test scenarios in Gherkin syntax for clarity and collaboration.
- **Selenium:** Automate browser interactions.
- **Pytest:** Manage and execute test cases, including generating HTML reports.

## Getting Started

### Prerequisites

- Python 3.x
- [Selenium](https://www.selenium.dev/)
- [Pytest](https://docs.pytest.org/en/latest/)
- Web Driver (e.g., ChromeDriver for Chrome)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/snehasachu/make-my-trip-automation/
   ```
2. **Move to the folder**
3. Install the Pipfile, create environment and activate the environment.
   ```bash
   init.bat
   ```
   
3. **Run test suite**
   ```bash
   py execute_test.py --browser chrome --scenario dashboard
   ```
4. Reports will be available in `reports/report.html`

## Architecture 

![Architecture Diagram](/docs/architecture_diagram.jpg)
