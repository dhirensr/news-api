import news_scraper
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! Welcome to news scraper'

@app.route("/stock-market", methods=["GET"])
def get_stock_market_news():
    page = request.args.get('page', 1, type=int)
    livemint_news = news_scraper.get_livemint_news("https://www.livemint.com/listing/subsection/market~stock-market-news/"+str(page))
    economic_times_news = news_scraper.get_economic_times_news("https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=2146843&img=0&curpg="+str(page))
    business_standard_news = news_scraper.get_business_standard_news("https://www.business-standard.com/category/markets-news-1060101.htm/"+str(page))
    ndtv_business_news = news_scraper.get_ndtv_business_news("https://www.ndtv.com/business/stocks/page-"+str(page))
    moneycontrol_stock_news = news_scraper.get_moneycontrol_news("https://www.moneycontrol.com/news/business/stocks/")
    moneycontrol_market_news = news_scraper.get_moneycontrol_news("https://www.moneycontrol.com/news/business/markets/")
    combined_news = {**livemint_news, **economic_times_news,**business_standard_news, **ndtv_business_news, **moneycontrol_market_news, **moneycontrol_stock_news}
    return jsonify(combined_news)

@app.route("/commodities", methods=["GET"])
def get_commodities_news():
    page = request.args.get('page', 1, type=int)
    livemint_news = news_scraper.get_livemint_news("https://www.livemint.com/market/commodities/page-"+str(page))
    economic_times_news = news_scraper.get_economic_times_news("https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=50991753&img=0&curpg="+str(page))
    business_standard_news = news_scraper.get_business_standard_news("https://www.business-standard.com/category/markets-commodities-precious-metals-1060801.htm/"+str(page))
    ndtv_business_news = news_scraper.get_ndtv_business_news("https://www.ndtv.com/business/commodities/page-"+str(page))
    combined_news = {**livemint_news, **economic_times_news,**business_standard_news, **ndtv_business_news}
    return jsonify(combined_news)


@app.route("/ipo-fpo", methods=["GET"])
def get_ipo_fpo_news():
    page = request.args.get('page', 1, type=int)
    livemint_news = news_scraper.get_livemint_news("https://www.livemint.com/market/ipo/page-"+str(page))
    economic_times_news = news_scraper.get_economic_times_news("https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=14655708&img=0&curpg="+str(page))
    business_standard_news = news_scraper.get_business_standard_news("https://www.business-standard.com/category/markets-ipos-news-1061101.htm/"+str(page))
    moneycontrol_ipo_news =  news_scraper.get_moneycontrol_news('https://www.moneycontrol.com/news/business/ipo/')
    combined_news = {**livemint_news, **economic_times_news,**business_standard_news, **moneycontrol_ipo_news}
    return jsonify(combined_news)


@app.route("/mutual-funds", methods=["GET"])
def get_mutual_fund_news():
    page = request.args.get('page', 1, type=int)
    livemint_news = news_scraper.get_livemint_news("https://www.livemint.com/mutual-fund/mf-news/page-"+str(page))
    moneycontrol_mf_news = news_scraper.get_moneycontrol_news("https://www.moneycontrol.com/news/business/mutual-funds/")
    #business_standard_news = news_scraper.get_business_standard_news("https://www.business-standard.com/category/markets-news-1060101.htm")
    combined_news = {**livemint_news, **moneycontrol_mf_news}
    return jsonify(combined_news)



@app.route("/top-news", methods=["GET"])
def get_top_news():
    page = request.args.get('page', 1, type=int)
    livemint_news = news_scraper.get_livemint_news("https://www.livemint.com/latest-news/page-"+str(page))
    business_standard_news = news_scraper.get_business_standard_news("https://www.business-standard.com/category/economy-policy-news-10201.htm/page-"+str(page))
    # economic_times_news = news_scraper.get_economic_times_news("https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=2146843&img=0&curpg=1")
    moneycontrol_top_news = news_scraper.get_moneycontrol_news("https://www.moneycontrol.com/news/news-all/")
    ndtv_business_news = news_scraper.get_ndtv_business_news("https://www.ndtv.com/business/latest/page-" + str(page))
    combined_news = {**livemint_news, **business_standard_news, **ndtv_business_news, **moneycontrol_top_news}
    return jsonify(combined_news)




#  main thread of execution to start the server
if __name__=='__main__':
    app.run(threaded = True, port = 5000)
