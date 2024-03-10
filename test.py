import re

content = """
=== Duplicate Post ===
Contributors: 		lopo
Donate link: 		https://duplicate-post.lopo.it/
Tags: 				duplicate post, copy, clone
Requires at least: 	3.6
Tested up to: 		5.2
Stable tag:    lalal3.2.3
Requires PHP:		5.2.4
License: 			GPLv2 or later
License URI: 		http://www.gnu.org/licenses/gpl-2.0.html

Copy posts of any type with a click!

== Description ==
"""

pattern = r"(?i)Stable.tag:\s+?([\w.]+)"
matches = re.findall(pattern, content)

if matches:
    print("Matches found:")
    for match in matches:
        print(match)
else:
    print("No matches found.")