import scrapy
import json


class SeartSpider(scrapy.Spider):
    name = "seart_spider"
    allowed_domains = ["seart-ghs.si.usi.ch"]
    start_urls = [
        "https://seart-ghs.si.usi.ch/api/r/search?nameEquals=false&language=Java&starsMin=800&sort=name%2Casc&hasWiki=true&hasLicense=true&hasPulls=true&page=0"
    ]

    def parse(self, response):
        # Parse JSON response
        data = json.loads(response.text)
        current_page = data.get("page", 0)
        self.logger.info(f"Processing page: {current_page}")
        # Extract items (projects)
        items = data.get("items", [])
        for item in items:
            title = item.get("name", "").strip() if item.get("name") else None  #   Extract project name
            homepage = item.get("homepage", "").strip() if item.get("homepage") else    ""  # Homepage URL from API
            full_name = item.get("fullName", "").strip() if item.get("fullName") else   ""  # GitHub 
            # Determine the URL to use
            if homepage and homepage.startswith("https://github.com"):
                url = homepage
            elif full_name:
                url = f"https://github.com/{full_name}"
            elif title and "/" in title:
                # Attempt to construct a GitHub URL using the title
                url = f"https://github.com/{title.strip()}"
            else:
                self.logger.debug(f"Skipping project without valid URL: {title}")
                continue  # Skip projects without a valid URL

            # Validate the GitHub URL before yielding
            if "https://github.com" in url:
                self.logger.debug(f"Adding project: {title} - {url}")
                yield {
                "Title": title,
                "URL": url,
                        }
            else:
                self.logger.debug(f"Skipping non-GitHub project: {title} - {url}")
            
        # Handle pagination up to 90 pages
        total_pages = data.get("totalPages", 0)
        max_pages = 150
        if current_page < total_pages - 1 and current_page < max_pages - 1:
            next_page = current_page + 1
            next_page_url = (
                f"https://seart-ghs.si.usi.ch/api/r/search?nameEquals=false&language=Java&starsMin=800&sort=name%2Casc&hasWiki=true&hasLicense=true&hasPulls=true&page={next_page}"
            )
            self.logger.info(f"Proceeding to page {next_page}")
            yield scrapy.Request(next_page_url, callback=self.parse)