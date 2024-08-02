import argparse
import os
import sys
import pytest
import conftest


def main(args):

    browser = args.browser
    scenario = args.scenario
    reruns = args.reruns
    os.environ['SCENARIO'] = scenario
    driver_path = conftest.get_chromedriver_path()
    report_name = conftest.report
    headless = args.headless
    pytest.main([
        '--browser={}'.format(browser),
        '--driver-path={}'.format(driver_path),
        '--reruns={}'.format(reruns),
        '-m={}'.format(scenario),
        '--html={}'.format(report_name),
        '--self-contained-html',
        '--headless'
    ])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', required=True, help='Please enter browser name, Example: --browser chrome/firefox')
    parser.add_argument('--scenario', required=False, default="",
                        help='This is a optional parameter to run specific scenario, Example --scenario scenario_name')
    parser.add_argument('--reruns', required=False, default=1, help='This is a optional parameter to rerun the failures')
    parser.add_argument("--headless", default=False, action="store_true", help='This flag triggers automation on headless browser')
    main(args=parser.parse_args())
