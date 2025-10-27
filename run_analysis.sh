pylint inventory_system.py > pylint_report.txt
bandit -r inventory_system.py > bandit_report.txt
flake8 inventory_system.py > flake8_report.txt
echo '\n\n===== FIX LOG =====\n' >> flake8_report.txt
cat fix_log.txt >> flake8_report.txt
pylint inventory_system.py > pylint_report.txt
bandit -r inventory_system.py > bandit_report.txt
flake8 inventory_system.py > flake8_report.txt
echo '\n\n===== FIX LOG =====\n' >> flake8_report.txt
cat fix_log.txt >> flake8_report.txt
pylint inventory_system.py > pylint_report.txt
bandit -r inventory_system.py > bandit_report.txt
flake8 inventory_system.py > flake8_report.txt
echo '\n\n===== FIX LOG =====\n' >> flake8_report.txt
cat fix_log.txt >> flake8_report.txt
