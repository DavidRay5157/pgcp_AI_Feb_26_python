import scrapy
from pathlib import Path


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    async def start(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # selecting all the books
        books = response.css(".product_pod")

        for book in books:
            yield{
                # pick the title
                'name' : book.css("h3 a::attr(title)").get(),

                # pick the price
                'price' : book.css(".price_color::text").get(),

                # pick the rating
                'star' : book.css(".star-rating::attr(class)").get().replace("star-rating ", ""),

                # pick the stock value
                'stock' : book.css(".instock.availability::text").getall()[-1].strip(),

                #pick the ref url
                'url' : response.urljoin(book.css("h3 a::attr(href)").get()),


            }






'''
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        # for saving the file
        #Path(filename).write_bytes(response.body)
        #self.log(f"saved file {filename}")

        # get a product by targeting the product_pod class
        a = response.css(".product_pod").get()  # one product.
        print(a)
'''



