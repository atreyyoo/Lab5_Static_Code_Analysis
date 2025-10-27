1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were the stylistic and formatting errors flagged by Flake8 — such as missing blank lines, unused imports, and line length warnings. These only required minor formatting adjustments and didn’t affect the program’s logic.

The hardest issues were logical and security-related problems, like replacing the bare except: block with proper exception handling and fixing the mutable default argument in the add_item function. These required understanding Python’s internal behavior — how default mutable objects persist across calls and how broad exception handling can silently hide errors. The removal of eval() also demanded understanding why it was insecure rather than just removing it blindly.

2. Did the static analysis tools report any false positives? If so, describe one example.

Yes, there was one case that could be considered a false positive.
Pylint flagged the use of the global statement inside load_data() as a warning (W0603), even though it was necessary to modify the shared stock_data dictionary. While Pylint considered it bad practice, in this simple script the global variable was intentional and did not introduce bugs or security risks. The warning made sense from a large-scale software perspective, but for this small lab script, it wasn’t a real problem.

3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate static analysis tools into the CI/CD pipeline so that code is automatically checked before merging or deployment. For example:

Pylint and Flake8 can run on every commit via GitHub Actions or a pre-commit hook to maintain consistent code quality and PEP8 style.

Bandit can run during CI builds to automatically catch any security vulnerabilities before release.
Additionally, I would configure local IDE integration (like VS Code extensions) so these tools provide live feedback as I code, reducing the number of issues before committing.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying the fixes, the code became cleaner, safer, and easier to maintain:

The Pylint score improved from 5.38 to 9.85, showing measurable quality gain.

The Bandit report became completely clean, meaning all security vulnerabilities were resolved.

The code is now more readable with consistent naming, proper docstrings, and spacing.

The logic is more robust — invalid inputs are handled gracefully, file operations are safer with with open(), and exception handling is explicit and meaningful.

Overall, the code now follows Python best practices, avoids silent failures, and is structured in a way that would be acceptable in a production-grade project.