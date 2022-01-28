from selenium import webdriver
import time
import pandas as pd
import csv

# fieldsummary=['Alternative Reference','Application Received','Application Validated','Address','Proposal','Status','Appeal Status','Appeal Decision']
# with open("summary.csv", 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow(fieldsummary)
# fieldfurther=['Application Type','Expected Decision Level','Case Officer','Parish','Ward','District Reference','Applicant Name','Agent Name','Agent Company Name','Agent Address','Environmental Assessment Requested']
# with open("summary.csv", 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow(fieldfurther)
# fieldfurther=['Application Type','Expected Decision Level','Case Officer','Parish','Ward','District Reference','Applicant Name','Agent Name','Agent Company Name','Agent Address','Environmental Assessment Requested']
# with open("summary.csv", 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow(fieldfurther)
def pagesData(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for count, row in enumerate(reader):
            for i in row:
                driver = webdriver.Chrome(executable_path='chromedriver.exe')
                driver.get(i)

                time.sleep(2)
                try:
                    summary = driver.find_element_by_xpath("//a[@id = 'subtab_summary']").get_attribute("href")
                    df = pd.read_html(summary)
                    df = df[0]
                    df = df.T.drop([0])
                    df.to_csv("summary.csv", mode='a',header = False, index=False)
                except Exception as e:
                    print(e)
                    pass
                try:
                    further = driver.find_element_by_xpath("//a[@id = 'subtab_details']").get_attribute("href")
                    df = pd.read_html(further)
                    df = df[0]
                    df = df.T.drop([0])
                    df.to_csv("further.csv", mode='a', header=False, index=False)
                except Exception as e:
                    print(e)
                    pass
                try:
                    contacts = driver.find_element_by_xpath("//a[@id = 'subtab_contacts']").get_attribute("href")
                    df = pd.read_html(contacts)
                    df = df[0]
                    df = df.T.drop([0])
                    df.to_csv("contacts.csv", mode='a', header=False, index=False)
                except Exception as e:
                    pass
                try:
                    dates = driver.find_element_by_xpath("//a[@id = 'subtab_dates']").get_attribute("href")
                    df = pd.read_html(dates)
                    df = df[0]
                    df = df.T.drop([0])
                    df.to_csv("dates.csv", mode='a', header=False, index=False)
                except Exception as e:
                    pass

                try:
                    constraints = driver.find_element_by_xpath("//a[@id = 'tab_constraints']").get_attribute("href")
                    df = pd.read_html(constraints)
                    df[0].to_csv("constraints.csv", mode='a', header = False, index=False)
                except Exception as e:
                    pass
                try:
                    documents = driver.find_element_by_xpath("//a[@id = 'tab_documents']").get_attribute("href")
                    df = pd.read_html(documents)
                    df[0].to_csv("documents.csv", mode='a', header = False, index=False)

                except Exception as e:
                    pass


                driver.close()