############################ code via html for no. of citations, h-index, i10-index  for all ############################


# import BeautifulSoup

# html_content = """
# <tbody><tr><td class="gsc_rsb_sc1"><a href="javascript:void(0)" class="gsc_rsb_f gs_ibl" title="This is the number of citations to all publications. The second column has the &quot;recent&quot; version of this metric which is the number of new citations in the last 5 years to all publications.">Citations</a></td><td class="gsc_rsb_std">93059</td><td class="gsc_rsb_std">59683</td></tr><tr><td class="gsc_rsb_sc1"><a href="javascript:void(0)" class="gsc_rsb_f gs_ibl" title="h-index is the largest number h such that h publications have at least h citations. The second column has the &quot;recent&quot; version of this metric which is the largest number h such that h publications have at least h new citations in the last 5 years.">h-index</a></td><td class="gsc_rsb_std">146</td><td class="gsc_rsb_std">102</td></tr><tr><td class="gsc_rsb_sc1"><a href="javascript:void(0)" class="gsc_rsb_f gs_ibl" title="i10-index is the number of publications with at least 10 citations. The second column has the &quot;recent&quot; version of this metric which is the number of publications that have received at least 10 new citations in the last 5 years.">i10-index</a></td><td class="gsc_rsb_std">669</td><td class="gsc_rsb_std">549</td></tr></tbody>
# """

# soup = BeautifulSoup(html_content, 'html.parser')

# # Finding all table rows
# table_rows = soup.find_all('tr')

# result_dict = {}
# for row in table_rows:
#     # Extracting text from the row
#     columns = row.find_all(['td', 'th'])
#     if columns:
#         key = columns[0].text.strip()
#         value = columns[1].text.strip()
#         result_dict[key] = value


# print("Result Dictionary:", result_dict)





