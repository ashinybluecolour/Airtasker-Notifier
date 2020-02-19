# Airtasker Notifier

how often do you spend your time constantly refreshing Airtasker, 
waiting for that data-entry job you're over qualified for, only
to discover it was posted while you were checking Facebook and
it's already been assigned. Airtasker Notifier allows you to
browse your favourite social media and be notified of jobs
with the specified keywords in their title.

# Demo
![Airtasker Notifier Demo](demo/demo.jpg)

# Requirements

- A device running MacOS
- An internet connection
- Beautiful Soup module for Python 3

# Usage

> usage: 

> ./airtasker_notifier.py --lat &lt;latitude&gt; --lon &lt;longitude&gt; &lt;job keyword&gt;


> optional arguments: 


> --distance &lt;maximum distance from location in km&gt;


> --min &lt;minimum pay&gt; (must be &gt;= 5)


> --max &lt;maximum pay&gt; (must be &lt;= 9999)


> --type &lt;'remote', 'onsite' or 'both'&gt;


> --keywords &lt;keyword 1&gt; &lt;keyword 2&gt; ...


> --no_keywords
