import pandas as pd
import matplotlib.pyplot as plt
from bigquery import query_bigquery

sql_query = """
    SELECT 
        job_title_category,
        AVG(annual_base_pay) AS avg_salary
    FROM 
        `tech-salary-insights.tech_salaries_dataset.cleaned_salaries`
    GROUP BY 
        job_title_category
    ORDER BY 
        avg_salary DESC
"""

df = query_bigquery(sql_query)

plt.figure(figsize=(12, 8))
df.set_index("job_title_category")["avg_salary"].plot(
    kind="bar", title="Average Salary by Job Title Category", color="skyblue"
)
plt.xlabel("Job Title Category")
plt.ylabel("Average Salary")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("output/avg_salary_by_category.png")  
print("Visualization saved as 'output/avg_salary_by_category.png'")
