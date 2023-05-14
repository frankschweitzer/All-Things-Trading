from socketserver import ThreadingUnixDatagramServer
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.styles import Font

# opening the page via request but denied - can contact 
# import requests
# url = f"https://www.tvinsider.com/network/{nework}/schedule/"
# response = requests.get(url)
# html_content = response.text
# soup = BeautifulSoup(html_content, 'html.parser')

def main():
    network = "A&E"
    map = show_data(network)
    write_to_file(map, network)
    

def write_to_file(map, network):
    # print to an excel file
    workbook = openpyxl.Workbook()
    bold_font = Font(bold=True)
    sheet = workbook.active
    sheet["A1"] = "Date"
    cell_A1 = sheet["A1"]
    cell_A1.font = bold_font
    sheet["B1"] = "Time"
    cell_B1 = sheet["B1"]
    cell_B1.font = bold_font
    sheet["C1"] = "Network"
    cell_C1 = sheet["C1"]
    cell_C1.font = bold_font
    sheet["D1"] = "Show"
    cell_D1 = sheet["D1"]
    cell_D1.font = bold_font
    row_num = 2
    for key, value in map.items():
        for subkey, subval in value.items():
            sheet[f"A{row_num}"] = key # insert day
            sheet[f"B{row_num}"] = subkey # insert time
            sheet[f"C{row_num}"] = network # insert day
            sheet[f"D{row_num}"] = subval # insert show
            row_num += 1
            
    workbook.save("tvData.xlsx")


def show_data(network):
    # open page via downloaded html file
    with open(f'{network}.html') as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    # blocking off data by day
    dates = soup.find_all(class_="date")

    days = []
    shows_by_day = [[]]
    times_by_day = [[]]

    # iterate over each date
    for i in range(len(dates)):
        date = dates[i].text
        days.append(date)

        # find the next sibling elements until the next date element
        siblings = dates[i].find_next_siblings()
        curr_block = siblings[0]
        shows_per_day = curr_block.find_all(class_="show-upcoming")
        shows = []
        times = []
        # creating lists of shows and times per day
        for show in shows_per_day:
            times.append(show.time.get_text())
            if show.find(class_="balance-text") == None:
                shows.append(show.h3.get_text()) # tends to be paid programming
            else:
                shows.append(show.find(class_="balance-text").get_text())
        times_by_day.append(times)
        shows_by_day.append(shows)

    times_by_day.pop(0)
    shows_by_day.pop(0)
    map = {}
    i = 0
    # grouping the shows and times by day
    for curr_shows in shows_by_day:
        curr_times = times_by_day[i]
        curr_map = {}
        
        for j in range(len(curr_shows)):
            curr_map.update({curr_times[j]: curr_shows[j]})
        
        if i < len(days):
            map.update({days[i]: curr_map})
        
        i += 1
    
    return map


main()