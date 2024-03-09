import re

content = """
The above regex does not get the value of this:
ontributors: mmaunder, wfryan, wfmatt, wfmattr
Tags: security, waf, malware, 2fa, two factor, login security, firewall, brute force, scanner, scan, web application firewall, protection, stop hackers, prevent hacks, secure wordpress, wordpress security
Requires at least: 3.9
Requires PHP: 5.5
Tested up to: 6.4
Stable tag: 7.11.1
License: GPLv3
License URI: https://www.gnu.org/licenses/gpl-3.0.html

Firewall, Malware Scanner, Two Factor Auth and Comprehensive Security Features, powered by our 24 hour team. Make security a priority with Wordfence.
"""

pattern = r"(?i)Stable.tag:\s?([\w.]+)"
matches = re.findall(pattern, content)

if matches:
    print("Matches found:")
    for match in matches:
        print(match)
else:
    print("No matches found.")