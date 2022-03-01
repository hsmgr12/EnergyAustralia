1. Structure
 |_ README
 |_ Util 
     |_ resources.py (Setting REST API endpoint and headers.) 
 |_ FestivalsBody.py (Testing response body.)
 |_ FestivalsHeaders.py (Testing response headers.)
 |_ FestivalStress.py (Stress testing.)
 
 2. Command:
    2.1 Run test file manually via PyCharm.
    2.2 On terminal under "EnergyAustralia" directory, run a single test file.
        py.test -v -s test_body.py
    2.3 On terminal under "EnergyAustralia" directory, generate report.
        pip install pytest-html
        py.test --html report.html
        Run above commands under PyCharm Terminal, it will run all the four test cases and generate report.html.
		
3. Questions
No "Available authorizations", so security is not testable.
"No parameters", so user has no control of what data to get.
 
 Author: Sandy He
 Email: hsmgr12@hotmail.com
 Cellphone: 0430496556
