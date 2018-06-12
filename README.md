# My test website using wagtail

This is my first try of designing a website using wagtail.
Starting from the initial default website created by wagtail.
The commit history will record all the learning experience I had.
As I have limited knowledge of website design and python,
the choices I made may not always be the best ones.

# Some comments

1. The starting point of wagtail is more practical than django,
   it has a couple of templates and one simple home app, which
   is just what I need right now.  From what I read in the manual,
   wagtail is intend to be a CMS, the integrated apps are all
   very useful.

2. I add bootstrap4 from the start.  I'm learning that too.
   The examples from bootstrap4 omit the jquery js file kinda
   cause a lot troubles.  It took me many hours to find why
   the dropdown menu don't work.

3. Missing tables support is discouraging. I had to change
   tables into pictures to include them into my Richtext-fields.

4. The default slug is constructed by the page's title, which
   is not cool when my page is in Chinese.  So I just redefined
   clean function to use a timestamp as the slug.  This will
   be fine since the odds of two pages are created at the same
   time is small.

5. Paginator in django is easy to use.  However, when there
   is too many pages, the navigator seems crowed.  Thanks to
   an answer in [stackoverflow](https://stackoverflow.com/questions/30864011/display-only-some-of-the-page-numbers-by-django-pagination), a one-liner in template solves this problem.
