# **AWS Cost and Usage Analysis**

## **Problem Statement**
A2Z POS, a leading provider of point-of-sale solutions, faced significant challenges in managing their AWS cloud infrastructure costs due to rapid business growth and increasing data complexity. The lack of clear visibility into cost drivers and usage patterns created issues such as:

- **Inadequate Financial Forecasting**: Unreliable projections affecting strategic planning and investor confidence.
- **Limited Cost Analysis**: Inability to dissect costs by services, projects, or departments.
- **Manual Reporting Processes**: Time-consuming and error-prone methods, lacking real-time insights.
- **Scalability Concerns**: Existing tools couldn’t handle increasing data volume and complexity.
- **Lack of Integration**: Disconnected data sources hindered advanced analytics and visualization.

### **Objective**
To build an automated and scalable solution that provides real-time insights into AWS cost and usage data, enabling better financial forecasting, resource optimization, and data-driven decision-making.

---

## **Solution Overview**

### **1. Automated Data Retrieval**
- Used the **AWS Cost Explorer API** to programmatically extract AWS cost and usage data.
- Data extraction automated using **Task Scheduler** in conjunction with a Python script.

### **2. Data Storage**
- Stored extracted data in a **MySQL database** for structured storage and future querying.

### **3. Data Visualization**
- Connected the MySQL database to **Power BI** for creating interactive dashboards.
- Automated dashboard updates using Power BI's refresh capabilities.

---

## **Key Features**
1. **Real-Time Insights**: Regular data updates ensure stakeholders access the latest cost and usage metrics.
2. **Interactive Dashboards**: Power BI dashboards visualize key metrics like service costs, usage trends, and blended/unblended costs.
3. **Automation**:
   - Data retrieval is automated via Task Scheduler.
   - Dashboards are updated automatically, reducing manual intervention.
4. **Scalability**: Designed to handle growing data volumes as the business expands.

---

## **Technologies Used**
| **Component**          | **Technology**              |
|-------------------------|-----------------------------|
| **Data Source**         | AWS Cost Explorer API       |
| **Data Storage**        | MySQL                       |
| **Visualization**       | Power BI                    |
| **Scheduling**          | Task Scheduler              |
| **Programming Language**| Python (Boto3, MySQL)       |

---

## **Architecture Diagram**

### **1. Data Flow Steps**
1. **Data Extraction**:
   - Python script queries AWS Cost Explorer API and retrieves data in JSON format.
   - Data includes key metrics like `BlendedCost`, `UnblendedCost`, and `UsageQuantity`.
2. **Data Storage**:
   - Extracted data is processed and stored in a MySQL database.
3. **Data Visualization**:
   - Power BI fetches data from MySQL and visualizes it in interactive dashboards.
4. **Automation**:
   - Task Scheduler triggers the Python script at predefined intervals.
   - Power BI's refresh feature ensures dashboards are always up-to-date.

---

## **Project Setup**

### **1. Prerequisites**
- Python 3.x installed.
- MySQL database set up.
- Power BI Desktop installed.
- AWS IAM user with `ce:GetCostAndUsage` permissions.
- MySQL ODBC Driver installed.

### **2. Installation Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/username/aws-cost-analysis.git
   cd aws-cost-analysis
   ```
2. Install required Python libraries:
   ```bash
   pip install boto3 mysql-connector-python
   ```
3. Set up your MySQL database and create the necessary table:
   ```sql
   CREATE TABLE aws_cost_usage (
       report_date DATE,
       service VARCHAR(255),
       blended_cost FLOAT,
       unblended_cost FLOAT,
       usage_quantity FLOAT
   );
   ```
4. Configure AWS credentials in the Python script.

---

## **Usage**

### **1. Running the Script**
- Run the Python script to extract data and store it in MySQL:
  ```bash
  python aws_cost_analysis.py
  ```

### **2. Setting Up Power BI**
1. Connect Power BI to the MySQL database.
2. Create dashboards using the `aws_cost_usage` table.
3. Publish the dashboard to Power BI Service for online sharing.

### **3. Automating with Task Scheduler**
- Add the script to Task Scheduler to run at regular intervals:
  - **Action**: Run the Python script.
  - **Trigger**: Set the desired schedule (e.g., daily or hourly).

---

## **Screenshots**
![image](https://github.com/user-attachments/assets/d44eea10-d830-4ae8-a7c8-cddab858f19a)


### **1. Power BI Dashboard**
- **Overview**:
  - Monthly cost breakdown by service.
  - Usage trends over time.
- **Example Visualizations**:
  - Pie charts for cost distribution by service.
  - Line graphs for usage trends.

### **2. Code in Action**
- Python script fetching data from AWS.
- MySQL database with populated tables.

---

## **Live Dashboard**
The live Power BI dashboard can be accessed [here](https://app.powerbi.com/groups/me/reports/56c39780-c229-4a88-bfc9-02cb70b28517/9d2c7802b254206b678b?experience=power-bi).

---

## **Contributions**
Contributions are welcome! Feel free to open an issue or submit a pull request.
