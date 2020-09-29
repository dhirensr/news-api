import news_scraper
from flask import Flask, jsonify, request
from flask_caching import Cache


config = {
    "DEBUG": False,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

@app.route('/')
@cache.cached(timeout=300)
def hello_world():
    return 'Hello World! Welcome to news scraper'

@app.route("/stock-market", methods=["GET"])
@cache.cached(timeout=50)
def get_stock_market_news():
    page = request.args.get('page', 1, type=int)
    livemint_news = news_scraper.get_livemint_news("https://www.livemint.com/listing/subsection/market~stock-market-news/")
    economic_times_news = news_scraper.get_economic_times_news("https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=2146843&img=0&curpg="+str(page))
    business_standard_news = news_scraper.get_business_standard_news("https://www.business-standard.com/category/markets-news-1060101.htm/")
    ndtv_business_news = news_scraper.get_ndtv_business_news("https://www.ndtv.com/business/stocks/")
    moneycontrol_stock_news = news_scraper.get_moneycontrol_news("https://www.moneycontrol.com/news/business/stocks/")
    moneycontrol_market_news = news_scraper.get_moneycontrol_news("https://www.moneycontrol.com/news/business/markets/")
    combined_news = livemint_news + economic_times_news + business_standard_news + ndtv_business_news + moneycontrol_market_news + moneycontrol_stock_news
    return jsonify(combined_news)

@app.route("/commodities", methods=["GET"])
@cache.cached(timeout=300)
def get_commodities_news():
    page = request.args.get('page', 1, type=int)
    livemint_news = news_scraper.get_livemint_news("https://www.livemint.com/market/commodities/")
    economic_times_news = news_scraper.get_economic_times_news("https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=50991753&img=0&curpg="+str(page))
    business_standard_news = news_scraper.get_business_standard_news("https://www.business-standard.com/category/markets-commodities-precious-metals-1060801.htm/")
    ndtv_business_news = news_scraper.get_ndtv_business_news("https://www.ndtv.com/business/commodities/")
    combined_news = livemint_news + economic_times_news + business_standard_news + ndtv_business_news
    return jsonify(combined_news)


@app.route("/ipo-fpo", methods=["GET"])
@cache.cached(timeout=300)
def get_ipo_fpo_news():
    page = request.args.get('page', 1, type=int)
    livemint_news = news_scraper.get_livemint_news("https://www.livemint.com/market/ipo/")
    economic_times_news = news_scraper.get_economic_times_news("https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=14655708&img=0&curpg="+str(page))
    business_standard_news = news_scraper.get_business_standard_news("https://www.business-standard.com/category/markets-ipos-news-1061101.htm/")
    moneycontrol_ipo_news =  news_scraper.get_moneycontrol_news('https://www.moneycontrol.com/news/business/ipo/')
    combined_news = livemint_news + economic_times_news + business_standard_news + moneycontrol_ipo_news
    return jsonify(combined_news)


@app.route("/mutual-funds", methods=["GET"])
@cache.cached(timeout=300)
def get_mutual_fund_news():
    page = request.args.get('page', 1, type=int)
    livemint_news = news_scraper.get_livemint_news("https://www.livemint.com/mutual-fund/mf-news/")
    moneycontrol_mf_news = news_scraper.get_moneycontrol_news("https://www.moneycontrol.com/news/business/mutual-funds/")
    #business_standard_news = news_scraper.get_business_standard_news("https://www.business-standard.com/category/markets-news-1060101.htm")
    combined_news = livemint_news + moneycontrol_mf_news
    return jsonify(combined_news)



@app.route("/top-news", methods=["GET"])
@cache.cached(timeout=300)
def get_top_news():
    page = request.args.get('page', 1, type=int)
    livemint_news = news_scraper.get_livemint_news("https://www.livemint.com/latest-news/")
    business_standard_news = news_scraper.get_business_standard_news("https://www.business-standard.com/category/economy-policy-news-10201.htm/page-"+str(page))
    # economic_times_news = news_scraper.get_economic_times_news("https://economictimes.indiatimes.com/lazyloadlistnew.cms?msid=2146843&img=0&curpg=1")
    moneycontrol_top_news = news_scraper.get_moneycontrol_news("https://www.moneycontrol.com/news/news-all/")
    ndtv_business_news = news_scraper.get_ndtv_business_news("https://www.ndtv.com/business/latest/")
    combined_news = livemint_news +business_standard_news + ndtv_business_news + moneycontrol_top_news
    return jsonify(combined_news)


@app.route("/live-streams", methods=["GET"])
@cache.cached(timeout=300)
def get_live_links():
    live_stream_links  = {"ET Now Live" : "https://etnowweblive-lh.akamaihd.net/i/ETN_1@348070/index_576_av-p.m3u8" ,\
                          "NDTV Profit Live" : "https://ndtvprofitelemarchana.akamaized.net/hls/live/2003680/ndtvprofit/masterp_480p@3.m3u8" ,\
                          "CNBC Bazaar Live (Hindi)"  : "https://cnbcawaaz-lh.akamaihd.net/i/cnbcawaaz_1@174872/index_5_av-p.m3u8" , \
                          "CNBC Bajar (Gujarati)"  : "https://cnbcbazar-lh.akamaihd.net/i/cnbcbajar_1@178933/index_1_av-b.m3u8"   }
    return jsonify(live_stream_links)



#  main thread of execution to start the server
if __name__=='__main__':
    app.run(threaded = True, port = 5000)
