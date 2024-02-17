# import requests
# from bs4 import BeautifulSoup


# profile_link = "https://scholar.google.com/citations?hl=en&user=n8c9ITIAAAAJ"
# response = requests.get(profile_link)
# soup = BeautifulSoup(response.content, 'html.parser')

# # Assuming the HTML structure remains similar, use a more specific selector:
# target_element = soup.find("tbody", class_="gsc_rsb_std")  # Find the tbody with class "gsc_rsb_std"


# if target_element:
#     html_content = str(target_element)  # Convert the element to a string
#     print(html_content)  # Print the extracted HTML content
# else:
#     print("Target element not found.")











# import requests

# profile_link = "https://scholar.google.com/citations?hl=en&user=n8c9ITIAAAAJ"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
# }

# response = requests.get(profile_link, headers=headers)

# if response.status_code == 200:
#     html_content = response.content
#     # Now you can process the HTML content as needed
# else:
#     print("Failed to retrieve content")









# from bs4 import BeautifulSoup

# html_content = """
# <tbody><tr><td class="gsc_rsb_sc1"><a href="javascript:void(0)" class="gsc_rsb_f gs_ibl" title="This is the number of citations to all publications. The second column has the &quot;recent&quot; version of this metric which is the number of new citations in the last 5 years to all publications.">Citations</a></td><td class="gsc_rsb_std">93059</td><td class="gsc_rsb_std">59683</td></tr><tr><td class="gsc_rsb_sc1"><a href="javascript:void(0)" class="gsc_rsb_f gs_ibl" title="h-index is the largest number h such that h publications have at least h citations. The second column has the &quot;recent&quot; version of this metric which is the largest number h such that h publications have at least h new citations in the last 5 years.">h-index</a></td><td class="gsc_rsb_std">146</td><td class="gsc_rsb_std">102</td></tr><tr><td class="gsc_rsb_sc1"><a href="javascript:void(0)" class="gsc_rsb_f gs_ibl" title="i10-index is the number of publications with at least 10 citations. The second column has the &quot;recent&quot; version of this metric which is the number of publications that have received at least 10 new citations in the last 5 years.">i10-index</a></td><td class="gsc_rsb_std">668</td><td class="gsc_rsb_std">549</td></tr></tbody>
# """

# # Parse the HTML content
# soup = BeautifulSoup(html_content, "html.parser")

# # Find the table within the parsed HTML content
# table = soup.find("tbody")

# if table:
#     # Print or use the table HTML content as needed
#     print(table.prettify())  # This will print the HTML content of the table
# else:
#     print("Table not found or structure changed.")





























# import requests
# from bs4 import BeautifulSoup

# profile_link = "https://scholar.google.com/citations?hl=en&user=n8c9ITIAAAAJ"

# # Send a GET request to the profile link
# response = requests.get(profile_link)

# # Parse the HTML content
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all divs with class 'gsc_rsb_s'
# divs = soup.find_all("div", {"class": "gsc_rsb_s"})

# if divs:
#     result_dict = {}
#     # Extract data from the divs
#     for div in divs:
#         metric_name = div.find("div", {"class": "gsc_rsb_std"}).text.strip()
#         metric_value = div.find("span", {"class": "gsc_rsb_std"}).text.strip()
#         result_dict[metric_name] = metric_value

#     # Rearrange the dictionary to match the desired output format
#     desired_order = ['Citations', 'h-index', 'i10-index']
#     final_dict = {key: result_dict.get(key, '') for key in desired_order}

#     print("Result Dictionary:", final_dict)
# else:
#     print("Table not found or structure changed.")





















# from selenium import webdriver

# profile_link = "https://scholar.google.com/citations?hl=en&user=n8c9ITIAAAAJ"

# # Set up Chrome options
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in headless mode, without opening a browser window

# # Initialize the Chrome driver
# driver = webdriver.Chrome(options=options)
# driver.get(profile_link)

# # Get the HTML content after the page is fully loaded
# html_content = driver.page_source

# # Close the browser
# driver.quit()

# # Print or use the HTML content as needed
# print(html_content)
