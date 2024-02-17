# from parsel import Selector
# from playwright.sync_api import sync_playwright
# import json, re 
# def scrape_researchgate_profile(profile: str):
#     with sync_playwright() as p:
        
#         profile_data = {
#             "basic_info": {},
#             "about": {},
#             "co_authors": [],
#             "publications": [],
#         }
        
#         browser = p.chromium.launch(headless=True, slow_mo=50)
#         page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
#         page.goto(f"https://www.researchgate.net/profile/{profile}")
#         selector = Selector(text=page.content())
        
#         profile_data["basic_info"]["name"] = selector.css(".nova-legacy-e-text.nova-legacy-e-text--size-xxl::text").get()
#         profile_data["basic_info"]["institution"] = selector.css(".nova-legacy-v-institution-item__stack-item a::text").get()
#         profile_data["basic_info"]["department"] = selector.css(".nova-legacy-e-list__item.nova-legacy-v-institution-item__meta-data-item:nth-child(1)").xpath("normalize-space()").get(
# )
#         profile_data["basic_info"]["current_position"] = selector.css(".nova-legacy-e-list__item.nova-legacy-v-institution-item__info-section-list-item").xpath("normalize-space()").get()
#         profile_data["basic_info"]["lab"] = selector.css(".nova-legacy-o-stack__item .nova-legacy-e-link--theme-bare b::text").get()
        
#         profile_data["about"]["number_of_publications"] = re.search(r"\d+", selector.css(".nova-legacy-c-card__body .nova-legacy-o-grid__column:nth-child(1)").xpath("normalize-space()").get()).group()
#         profile_data["about"]["reads"] = re.search(r"\d+", selector.css(".nova-legacy-c-card__body .nova-legacy-o-grid__column:nth-child(2)").xpath("normalize-space()").get()).group()
#         profile_data["about"]["citations"] = re.search(r"\d+", selector.css(".nova-legacy-c-card__body .nova-legacy-o-grid__column:nth-child(3)").xpath("normalize-space()").get()).group()
#         profile_data["about"]["introduction"] = selector.css(".nova-legacy-o-stack__item .Linkify").xpath("normalize-space()").get()
#         profile_data["about"]["skills"] = selector.css(".nova-legacy-l-flex__item .nova-legacy-e-badge ::text").getall()
        
#         for co_author in selector.css(".nova-legacy-c-card--spacing-xl .nova-legacy-c-card__body--spacing-inherit .nova-legacy-v-person-list-item"):
#             profile_data["co_authors"].append({
#                 "name": co_author.css(".nova-legacy-v-person-list-item__align-content .nova-legacy-e-link::text").get(),
#                 "link": co_author.css(".nova-legacy-l-flex__item a::attr(href)").get(),
#                 "avatar": co_author.css(".nova-legacy-l-flex__item .lite-page-avatar img::attr(data-src)").get(),
#                 "current_institution": co_author.css(".nova-legacy-v-person-list-item__align-content li").xpath("normalize-space()").get()
#             })
#         for publication in selector.css("#publications+ .nova-legacy-c-card--elevation-1-above .nova-legacy-o-stack__item"):
#             profile_data["publications"].append({
#                 "title": publication.css(".nova-legacy-v-publication-item__title .nova-legacy-e-link--theme-bare::text").get(),
#                 "date_published": publication.css(".nova-legacy-v-publication-item__meta-data-item span::text").get(),
#                 "authors": publication.css(".nova-legacy-v-person-inline-item__fullname::text").getall(),
#                 "publication_type": publication.css(".nova-legacy-e-badge--theme-solid::text").get(),
#                 "description": publication.css(".nova-legacy-v-publication-item__description::text").get(),
#                 "publication_link": publication.css(".nova-legacy-c-button-group__item .nova-legacy-c-button::attr(href)").get(),
#             })
            
#         file_name = f"{profile}.json"
#         with open(file_name, "w", encoding="utf-8") as json_file:
#             json.dump(profile_data, json_file, indent=2, ensure_ascii=False)
#             print(f"JSON data saved to '{file_name}'")    
#         # print(json.dumps(profile_data, indent=2, ensure_ascii=False))
#         browser.close()
        
    
# scrape_researchgate_profile(profile="Kamran-Ahmed-23")






######################## Final Code ##########################


from parsel import Selector
from playwright.sync_api import sync_playwright
import json, re

from playwright.sync_api import sync_playwright



def scrape_researchgate_profile(profile: str):
    with sync_playwright() as p:
        
        profile_data = {
            "about": {},
            "co_authors": [],
        }
        
        browser = p.chromium.launch(headless=True, slow_mo=50)
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page.goto(f"https://www.researchgate.net/profile/{profile}", timeout=60000)
        selector = Selector(text=page.content())
        
        profile_data["about"]["number_of_publications"] = re.search(r"\d{1,3}(,\d{3})*", selector.css(".nova-legacy-c-card__body .nova-legacy-o-grid__column:nth-child(1)").xpath("normalize-space()").get()).group()
        profile_data["about"]["citations"] = re.search(r"\d{1,3}(,\d{3})*", selector.css(".nova-legacy-c-card__body .nova-legacy-o-grid__column:nth-child(3)").xpath("normalize-space()").get()).group()
        profile_data["about"]["h_index"] = selector.css(".common-metric__text:contains('h-index') + .nova-legacy-l-flex__item .nova-legacy-e-text--size-m").xpath("normalize-space()").get()



        # List of co-authors
        for co_author in selector.css(".nova-legacy-c-card--spacing-xl .nova-legacy-c-card__body--spacing-inherit .nova-legacy-v-person-list-item"):
            profile_data["co_authors"].append({
                "name": co_author.css(".nova-legacy-v-person-list-item__align-content .nova-legacy-e-link::text").get(),
                "link": co_author.css(".nova-legacy-l-flex__item a::attr(href)").get(),
                "avatar": co_author.css(".nova-legacy-l-flex__item .lite-page-avatar img::attr(data-src)").get(),
                "current_institution": co_author.css(".nova-legacy-v-person-list-item__align-content li").xpath("normalize-space()").get()
            })
        
        file_name = f"{profile}_about.json"
        with open(file_name, "w", encoding="utf-8") as json_file:
            json.dump(profile_data, json_file, indent=2, ensure_ascii=False)
            print(f"JSON data saved to '{file_name}'")    
        browser.close()

scrape_researchgate_profile(profile="Kamran-Ahmed-23")







############ For all Coauthors ###########



# from parsel import Selector
# from playwright.sync_api import sync_playwright
# import json, re

# def scrape_researchgate_profile(profile: str):
#     with sync_playwright() as p:
        
#         profile_data = {
#             "about": {},
#             "co_authors": [],
#         }
        
#         browser = p.chromium.launch(headless=True, slow_mo=50)
#         page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
#         page.goto(f"https://www.researchgate.net/profile/{profile}", timeout=60000)
#         selector = Selector(text=page.content())
        
#         profile_data["about"]["number_of_publications"] = re.search(r"\d{1,3}(,\d{3})*", selector.css(".nova-legacy-c-card__body .nova-legacy-o-grid__column:nth-child(1)").xpath("normalize-space()").get()).group()
#         profile_data["about"]["citations"] = re.search(r"\d{1,3}(,\d{3})*", selector.css(".nova-legacy-c-card__body .nova-legacy-o-grid__column:nth-child(3)").xpath("normalize-space()").get()).group()
        
#         # Updated co-author selector
#         for co_author in selector.css('.nova-legacy-c-modal__body.nova-legacy-c-modal__body--spacing-inherit .nova-legacy-v-person-list-item'):
#             co_author_info = {
#                 'name': co_author.css('.nova-legacy-e-link--color-inherit::text').get(),
#                 'link': co_author.css('.nova-legacy-e-link--color-inherit::attr(href)').get(),
#                 'avatar': co_author.css('.nova-legacy-e-avatar__img::attr(src)').get(),
#                 'current_institution': co_author.css('.nova-legacy-v-person-list-item__meta span::text').get(),
#                 }
#             profile_data['co_authors'].append(co_author_info)


        
#         file_name = f"{profile}_about.json"
#         with open(file_name, "w", encoding="utf-8") as json_file:
#             json.dump(profile_data, json_file, indent=2, ensure_ascii=False)
#             print(f"JSON data saved to '{file_name}'")    
#         browser.close()

# scrape_researchgate_profile(profile="Kamran-Ahmed-23")














































































































# import requests
# from bs4 import BeautifulSoup

# url = "https://www.researchgate.net/profile/Kamran-Ahmed-23"

# # Send a GET request to the URL
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, "html.parser")

#     # Find the specific div with the class "nova-legacy-o-grid"
#     stats_div = soup.find("div", class_="nova-legacy-o-grid__column nova-legacy-o-grid__column--width-4/12@s-up")  
# # <div class="nova-legacy-o-grid__column nova-legacy-o-grid__column--width-4/12@s-up"><div class="nova-legacy-e-text nova-legacy-e-text--size-xl nova-legacy-e-text--family-display nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit" data-testid="publicProfileStatsPublications">248</div><div class="nova-legacy-e-text nova-legacy-e-text--size-m nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit">Publications</div></div>
#     # Print the entire div content
#     print(stats_div.prettify())

#     # Or, if you want to extract specific parts within this div
#     # For example, getting the number of publications, reads, and citations
#     publications = stats_div.find("div", {"data-testid": "publicProfileStatsPublications"}).text.strip()
#     reads = stats_div.find("div", {"data-testid": "publicProfileStatsReads"}).text.strip()
#     citations = stats_div.find("div", {"data-testid": "publicProfileStatsCitations"}).text.strip()

#     print("Publications:", publications)
#     print("Reads:", reads)
#     print("Citations:", citations)

# else:
#     print("Failed to retrieve the page")


















# import requests
# from bs4 import BeautifulSoup

# url = "https://www.researchgate.net/profile/Kamran-Ahmed-23"

# try:
#     # Send a GET request to the URL
#     response = requests.get(url)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(response.content, "html.parser")

#         # Find the statistics based on their unique data-testid attributes
#         publications = soup.find("div", {"data-testid": "publicProfileStatsPublications"}).text.strip()
#         reads = soup.find("div", {"data-testid": "publicProfileStatsReads"}).text.strip()
#         citations = soup.find("div", {"data-testid": "publicProfileStatsCitations"}).text.strip()

#         print("Publications:", publications)
#         print("Reads:", reads)
#         print("Citations:", citations)

#     else:
#         print("Failed to retrieve the page. Status code:", response.status_code)

# except Exception as e:
#     print("An error occurred:", str(e))

# # Print the response content for debugging purposes
# print(response.content)
