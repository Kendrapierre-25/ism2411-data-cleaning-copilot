What Copilot generated
Which functions or code blocks came primarily from Copilot’s suggestions? How did you prompt it (comments, partial code, etc.)?

# To generate function code, I wrote comments above each function describing what it should do. After typing a function signature such as `def clean_column_names(df):`, Copilot suggested code that converted column names to lowercase and replaced spaces. I used Copilot again for the rest of the functions.

What you modified
What changes did you make to Copilot’s code (renaming variables, changing logic, simplifying steps)? Why were those changes needed?
# For each Copilot suggestion, I changed parts of the logic so the code would align with the specific requirements of the assignment. For example, Copilot originally suggested dropping missing values, but I modified it to fill them with zero instead to keep the dataset consistent. I renamed the variable names of "Price" and "Qty".

What you learned
What did you learn about data cleaning in Python and about using Copilot as a tool (strengths and limitations)? Include at least one specific example.
# This project helped me understand how data cleaning pipelines work in Python. I learned that breaking steps into functions makes the workflow easier to test and reuse. I also learned that Copilot is useful for generating logic quickly, but it often needs modification to meet exact specifications. For example, Copilot suggested removing negative values , which would hide errors instead of removing them. By reviewing and editing the suggestion, I ensured the cleaning logic stayed accurate and transparent.