from model.TestCase import TestCase
from model.TestStep import TestStep
from model.LogManager import LogManager
from model.LogContent import LogContent
import os
import sys
import json
import subprocess
import re
import datetime


g_list_test_case = dict()
g_current_log = dict()
g_current_log_testing_path = ""


def set_test_step(name, data):
    test_step = TestStep()
    test_step.set_test_step_name(name)
    test_step.set_test_step_type(data["Type"])
    test_step.set_test_step_action(data["Action"])
    log_temp= list()
    for item in data["Log"]:
        log_temp.append(data["Log"][item])
    test_step.set_test_step_log(log_temp)
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
    with open(path, 'r') as f:
        data = json.load(f)
        test_case = set_test_case(data)

        if test_case.test_case_name not in g_list_test_case:
            g_list_test_case[test_case.test_case_name] = test_case
        else:
            print("test case exits")
    return g_list_test_case[test_case.test_case_name]


def send_sldd_command(command):
    try:
        subprocess.call(f"adb1 shell {command}", shell=True, timeout=3)
    except:
        print(f"send_sldd_command -- {command} -- Fail")
    return g_current_log_testing_path


def run_test_case(testcase):
    test_steps = testcase.test_steps
    for item in test_steps:
        if "sendcommand" in test_steps[item].test_step_type.lower():
            send_sldd_command(test_steps[item].test_step_action)
            pass
        elif "waiting" in test_steps[item].test_step_type.lower():
            # print(item, test_steps[item].test_step_action)
            pass
        else:
            pass


def get_vdc_log():
    time_now = datetime.datetime.now()
    if "log_storage" not in os.listdir():
        os.mkdir(f"log_storage")
    if "log_temp" not in os.listdir(os.path.join(os.getcwd(),"log_storage")):
        os.mkdir(os.path.join(os.path.join(os.getcwd(),"log_storage"), "log_temp"))

    g_current_log_testing_path = f".\log_storage\log_temp\{time_now.year}{time_now.month}{time_now.day}_{time_now.hour}{time_now.minute}{time_now.second}_Log.txt"
    try:
        subprocess.call(f"adb1 logcat -d > {g_current_log_testing_path}", shell=True, timeout=3)
    except:
        print("get_vdc_log - Fail")
    return g_current_log_testing_path


def set_log_manager(data):
    temp_log_list = list()
    for index, item in enumerate(data, start=1):
        matchData = re.search(r"(\d+-\d+)\s*(\d+:\d+:\d+.\d+)\s*(\d+)\s*(\d+)\s*(\w+)\s*(\w+)\s*:\s*(.*)", item)
        if matchData:
            if "rvc" in matchData.group(6).lower():
                temp_log = LogContent()
                temp_log.set_log_content_line(index)
                temp_log.set_log_content_date(matchData.group(1))
                temp_log.set_log_content_time(matchData.group(2))
                temp_log.set_log_content_log_level(matchData.group(3))
                temp_log.set_log_content_pid(matchData.group(4))
                temp_log.set_log_content_tid(matchData.group(5))
                temp_log.set_log_content_tag(matchData.group(6))
                temp_log.set_log_content_message(matchData.group(7))
                temp_log_list.append(temp_log)
            else:
                # print("ahihi")
                pass
        else:
            pass

    log_manager_temp = LogManager()
    log_manager_temp.set_log_manager_session_id("RVC")
    log_manager_temp.set_log_manager_log_content(temp_log_list)
    g_current_log[log_manager_temp.session_id] = log_manager_temp

    return g_current_log


def load_log(path):
    with open(path, 'r') as f:
        log = f.readlines()
        current_log = set_log_manager(log)
    return current_log


def clear_vdc_log():
    try:
        subprocess.call("adb1 logcat -c", shell=True)
    except:
        print("clear_vdc_log - Fail")


# def save_vdc_log():
#     os.
#     g_current_log_testing_path


def handle_compare_test_case():
    current_log_path = get_vdc_log()
    load_log(current_log_path)
    
    for item in g_list_test_case:
        test_steps = g_list_test_case[item].test_steps
        for step in test_steps:
            if "sendcommand" in test_steps[step].test_step_type.lower():
                result = compare_log(test_steps[step].test_step_log)
            else:
                pass
    return result


def search_log(expected_log):
    # print(expected_log)
    index_log = 0
    for item in g_current_log["RVC"].log_content:
        if expected_log[index_log] in item.message:
            index_log += 1
            if index_log >= len(expected_log):
                break
    if index_log >= len(expected_log):
        return True
    else:
        return False

def compare_log(expected_log):
    result = search_log(expected_log)
    return result

def run():
    print("ahihi")
