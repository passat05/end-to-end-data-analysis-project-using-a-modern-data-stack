# Introduction
The project aimed to create a robust yet simple data analytics platform with airflow for orchestration, dbt for modelling and transformation, Gitlab for continuous integration and development and Power BI for visualization backed by development pipelines in Power BI service.  
![data_pipeline.png](images%2Fdata_pipeline.png)
# Understanding the components
## Check quality
### Scope
Tests are assertions you make about models and other resources in dbt project (e.g. sources, seeds and snapshots). Data testing through dbt explains how to declare test cases to validate data quality and compliance with expectations.  
There are two type of check quality including check quality at source data level and check quality at transformation data level.
Both are defined and evaluated based on five key dimensions of data quality: accuracy, completeness, consistency, validity, and uniqueness.  
### Tool
dbt Great Expectation is a powerful package in dbt to expand the testing capabilities and enhance data quality assurance within dbt projects. It allows to define, document, and validate expectations about data, providing a comprehensive approach to data testing.
Example, If you expect the specified column to exist, you can add test case with following content:
```yaml
version: 2

models:
  - name: dim_address
    columns:
      - name: addressid
        description: The natural key
        tests:
          - dbt_expectations.expect_column_to_exist # this test is powered by great-expectation library
```
## Data modelling
### Scope
Data modeling is a fundamental step in the process of designing and organizing data structures to meet specific business requirements. It serves as blueprints for how data will be stored, organized, and accessed within a database or data warehouse.  
The Dimensional Data Model is one of the modeling techniques which primarily used for data warehousing and analytics. It focuses on simplifying complex data into a structure that is optimized for querying and reporting.  
In this model, data is organized into two types of tables: dimension tables (containing descriptive attributes) and fact tables (containing numerical performance measures). These tables are connected through keys, enabling efficient multidimensional analysis.
### Tool
dbt, which stands for Data Build Tool, is a command-line tool that revolutionizes the way data transformations and modeling are done. Here's a deeper dive into dbt's capabilities:
- **Modular Data Transformations**: dbt uses SQL and YAML files to define data transformations and models. This modular approach allows to break down complex transformations into smaller, more manageable pieces, enhancing mantainability and version control.
- **Custom Macros**: dbt allow to create custom macros to encapsulate reusable SQL logic that can be shared across multiple models. This helps enhance modularity and maintainability in dbt project.
- **Jinja template**: dbt develop this templating engine to allow for dynamic SQL generation, then improve SQL code.
- **Incremental Builds**: dbt supports incremental builds, meaning it only processes data that has changed since the last run. This feature saves time and resources when working with large datasets.
- **Documentation**: dbt provides a built-in documentation system that allows to document data models, tests, and columns.
## Visualization
### Scope
The transformed data would then be used to generate visualizations which transforms complex data into easily interpretable charts, graphs, and dashboards for analysis and reporting.
### Tool
Power BI is a business intelligence tool developed by Microsoft that empowers users to visualize and share insights from data. It offers a wide range of capabilities for data preparation, analysis, and visualization. Notably, it integrates development pipelines in the Power BI service and seamlessly connects with Azure DevOps and Git Ops for efficient version control and collaborative workflows.  
RLS Row Level Security is also a valuable and practical feature that ensures data security by restricting access to specific rows of data based on user roles, enabling precise control over information visibility.
## Orchestration and CI/CD
### Scope
Job scheduling and orchestration allows for the automation of data workflows, ensuring data is processed and delivered at the right time.  
Regularly reviewing and iterating on models, tests, and workflows helps keep data assets up-to-date and aligned with business needs.
### Tool
Apache Airflow is an open-source platform designed to programmatically author, schedule, and monitor workflows.  
GitLab is a web-based DevOps lifecycle tool that provides a platform for source code management, continuous integration/continuous deployment (CI/CD), and collaboration.
