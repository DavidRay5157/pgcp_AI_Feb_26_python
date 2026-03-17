import scrapy
from pathlib import Path


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    async def start(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/childrens_11/index.html",
            "https://books.toscrape.com/catalogue/category/books/classics_6/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'books-{page}.html'
        # saving the file
        #Path(filename).write_bytes(response.body)
        #self.log(f"saved file {filename}")
        #a = response.css(".product_pod").get()  # one data
        #print(a)

        # select all the data
        books = response.css(".product_pod")

        for book in books:
            yield {
                # title
                'name' : book.css("h3 a::attr(title)").get(),

                # price
                'price' : book.css(".price_color::text").get(),

                # rating
                'stars' : book.css(".star-rating::attr(class)").get().replace("star-rating",""),

                # stock
                'stock' : book.css(".instock.availability::text").getall()[-1].strip(),

                'url' : response.urljoin(book.css("h3 a::attr(href)").get()),
            }









