import requests
from bs4 import BeautifulSoup
from Course import Course


class Scraper:

    def get_page(self):
        return BeautifulSoup(
            requests.get(
                "http://learn-co-curriculum.github.io/site-for-scraping/courses"
            ).text,
            "html.parser"
        )

    def get_courses(self):
        return self.get_page().select('.post')

    def make_courses(self):
        courses = []

        for course in self.get_courses():
            title_el = course.select_one('h2')
            schedule_el = course.select_one('.schedule')
            description_el = course.select_one('.description')

            title = title_el.text if title_el else ""
            schedule = schedule_el.text if schedule_el else ""
            description = description_el.text if description_el else ""

            courses.append(
                Course(
                    title=title,
                    schedule=schedule,
                    description=description
                )
            )

        return courses
