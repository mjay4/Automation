import bs4, requests

def getPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
    return elems[0].text.strip()


price = getPrice('https://www.flipkart.com/start-with-why/p/itmf6cfuqktyggpp?pid=9780241958223&lid=LSTBOK9780241958223KF6TEJ&marketplace=FLIPKART&srno=b_1_1&otracker=pp_reco_You%2Bmight%2Bbe%2Binterested%2Bin_1_31.dealCard.OMU_You%2Bmight%2Bbe%2Binterested%2Bin_cid%3AS_F_N_bks_rbc_aza__d_60-100__eaf_eas_ALL%3Bnid%3Abks_rbc_aza_%3Bmp%3AF%3Bct%3Ad%3B&otracker1=pp_reco_PINNED_productRecommendation%2FAugmentSelling_You%2Bmight%2Bbe%2Binterested%2Bin_BANNER_HORIZONTAL_dealCard_cc_1_NA_view-all&fm=SEARCH&iid=7e85a4ac-b379-4dfe-ae93-1ceef6d51785.9780241958223.SEARCH&ppt=browse&ppn=browse&ssid=qc5u02jec00000001588746549440')
print('The price is : ' + price)
