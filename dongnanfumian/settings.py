# -*- coding: utf-8 -*-

# Scrapy settings for dongnanfumian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dongnanfumian'

SPIDER_MODULES = ['dongnanfumian.spiders']
NEWSPIDER_MODULE = 'dongnanfumian.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dongnanfumian (+http://www.yourdomain.com)'

KEYWORDS = {
        '东南 四川菱威':1,
        '东南 倒下':1,
        '东南 权斗':1,
        '东南经销商 盈利':1,
        '东南 退网':1,
        '追随东南汽车10多年的四川菱威轰然倒下':1,
        '东南汽车内部权斗升级，经销商盈利无望开始退网':1,
}


#   --------------------------MongoDB configuration --------------------------
MONGO_DB_URI = 'mongodb://192.168.0.48:27017'
# MONGO_DB_URI = 'mongodb://127.0.0.1:27017'
# MONGO_DB_URI = 'mongodb://182.61.172.116:27017'
MONGO_DB_NAME = 'DongnanFumian'
# ------------------------------------------------------------------------------

#   --------------------------splash configuration --------------------------
# SPLASH_URL = 'http://127.0.0.1:8050'
SPLASH_URL = 'http://182.61.172.116:8050'
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE ='scrapy_splash.SplashAwareFSCacheStorage'
SPLASH_LOG_400 = True
# ------------------------------------------------------------------------------


#   --------------------------Redis configuration --------------------------
# REDIS_URL = 'redis://127.0.0.1:6379'
REDIS_URL = 'redis://192.168.0.48:6379'
# 增加了调度的配置,把请求对象存储到Redis数据, 从而实现请求的持久化.
SCHEDULER = "scrapy_redis_bloomfilter.scheduler.Scheduler"
# 增加了一个去重容器类的配置, 作用使用Redis的set集合来存储请求的指纹数据, 从而实现请求去重的持久化
DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
DUPEFILTER_DEBUG = False
SCHEDULER_QUEUE_CLASS = 'scrapy_redis_bloomfilter.queue.PriorityQueue'
SCHEDULER_PERSIST = True
# ------------------------------------------------------------------------------

FEED_EXPORT_ENCODING = 'utf-8'
# LOG_LEVEL = "INFO"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 8
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   # 'cctv_OpinionMonitor.middlewares.CctvOpinionmonitorSpiderMiddleware': 543,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'dongnanfumian.middlewares.DongnanfumianDownloaderMiddleware': 543,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'dongnanfumian.pipelines.DongnanfumianPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
