from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os


def main():
	print("Please enter your shipping carrier ('UPS' or 'USPS'): ")
	carrier = raw_input().upper()
	print("Now enter your tracking number: ")
	trackingNumber = raw_input()

	driver = webdriver.Chrome()

	if (carrier == 'UPS'):
		self.driver.get("http://www.ups.com/tracking/tracking.html")
		trackingNumID = "trackNums"
		submitXpath = "//input[@value='Track']"
		progressXpath = "//*[@id='collapse3']/h4"

		trackingFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(trackingNumID))
		submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(submitXpath))

		trackingFieldElement.clear()
		trackingFieldElement.send_keys(trackingNumber)
		submitButtonElement.click()

		WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(progressXpath))
	elif (carrier == 'USPS'):
		driver.get("https://tools.usps.com/go/TrackConfirmAction!input.action")
		trackingNumID = "tLabels"
		submitXpath = "//*[@id='trackNumFindBtn']"
		progressXpath = "//*[@id='results-multi']/div[1]/div/div[3]/div[1]/h3"

		trackingFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(trackingNumID))
		submitButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(submitXpath))

		trackingFieldElement.clear()
		trackingFieldElement.send_keys(trackingNumber)
		submitButtonElement.click()

main()