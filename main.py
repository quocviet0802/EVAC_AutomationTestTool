from model.TestCase import TestCase
from model.TestStep import TestStep
from model.LogManager import LogManager
from model.LogContent import LogContent
import hmi_app.HmiApplication as HMI
import os
import sys
import json
import subprocess
import re


g_list_test_case = dict()
g_log = list()


def set_test_step(name, data):
    test_step = TestStep()
    test_step.set_test_step_name(name)
    test_step.set_test_step_action(data["Action"])
    test_step.set_test_step_log(data["Log"])
    test_step.set_test_step_exceptions(data["Exceptions"])
    return test_step


def set_test_case(data):
    test_case = TestCase()

    if "TestCase" in data:
        test_case.set_test_case_name(data["TestCase"])
    else:
        print("format test case wrong - - test case")

    if "TestSteps" in data:
        test_step_dict = dict()
        for item in data["TestSteps"]:
            test_step_dict[item] = set_test_step(item, data["TestSteps"][item])
        test_case.set_test_steps(test_step_dict)
    else:
        print("format test case wrong - test steps")
    
    if "Exceptions" in data:
        test_case.set_test_exceptions(data["Exceptions"])
    else:
        print("format test case wrong - exceptions")
    # set_test_step()
    return test_case


def load_test_case(path):
    with open('config\\test.json', 'r') as f:
        data = json.load(f)
        test_case = set_test_case(data)

        if test_case.test_case_name not in g_list_test_case:
            g_list_test_case[test_case.test_case_name] = test_case
        else:
            print("test case exits")

    # for item in g_list_test_case:
    #     print(g_list_test_case[item].test_case_name)
    #     test_step = g_list_test_case[item].test_steps
    #     for i in test_step:
    #         print(test_step[i].test_step_name)
    #         print("    ", test_step[i].test_step_action)
    #         print("    ", test_step[i].test_step_log)
    #         print("    ", test_step[i].test_step_exceptions)
    #     print(g_list_test_case[item].test_exceptions)


def run_test_case(testcase):
    test_steps = testcase.test_steps
    for item in test_steps:
        if "sendcommand" in item.lower():
            # subprocess.call(f"{test_steps[item]}",shell=True)
            pass
        elif "waiting" in item.lower():
            # sleep(test_steps[item])
            pass
        else:
            pass


def compare_log(testcase, log):
    test_steps = testcase.test_steps
    for item in test_steps:
        if "sendcommand" in item.lower():
            # print(item, test_steps[item])
            pass
        elif "waiting" in item.lower():
            # print(item, test_steps[item])
            pass
        else:
            pass


def set_log_manager(data):
    for index, item in enumerate(data, start=1):
        temp_log = LogContent()
        matchData = re.search(r"(\d+-\d+)\s*(\d+:\d+:\d+.\d+)\s*(\d+)\s*(\d+)\s*(\w+)\s*(\w+)\s*:\s*(.*)", item)
        if matchData:
            temp_log.set_log_content_line(index)
            temp_log.set_log_content_date(matchData.group(1))
            temp_log.set_log_content_time(matchData.group(2))
            temp_log.set_log_content_log_level(matchData.group(3))
            temp_log.set_log_content_pid(matchData.group(4))
            temp_log.set_log_content_tid(matchData.group(5))
            temp_log.set_log_content_tag(matchData.group(6))
            temp_log.set_log_content_message(matchData.group(7))
        else:
            pass
    g_log


def load_log(path):
    log = ""
    with open('log.txt', 'r') as f:
        log = f.readlines()
        set_log_manager(log)

def run():
    HMI.run_gui()
    # load_test_case("abc")
    # run_test_case(g_list_test_case["remoteservice_app_enable"])
    # compare_log(g_list_test_case["remoteservice_app_enable"], "abc")
    # load_log("log.txt")


if __name__ == "__main__":
    run()

