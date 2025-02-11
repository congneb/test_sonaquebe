import requests
import json

# SonarQube API URL and credentials
# api_url_measures = "https://sonarcloud.io/api/measures/component?component=your_project_key&metricKeys=ncloc,bugs,code_smells,vulnerabilities,coverage,duplicated_lines_density"
# api_url_issues = "https://sonarcloud.io/api/issues/search?componentKeys=your_project_key&resolved=false&ps=500"
# headers = {
#     "Authorization": "Basic your_base64_encoded_credentials"
# }


api_url_measures = "https://sonarcloud.io/api/measures/component?component=congneb_test_sonaquebe&metricKeys=ncloc,bugs,code_smells,vulnerabilities,coverage,duplicated_lines_density"
api_url_issues = "https://sonarcloud.io/api/issues/search?componentKeys=congneb_test_sonaquebe&resolved=false&ps=500"
headers = {
    "Authorization": "f10607a8740ce90881d8fab11e2baff57g5746"
}


# Fetch measures from SonarQube API
response_measures = requests.get(api_url_measures, headers=headers)
data_measures = response_measures.json()

# Fetch issues from SonarQube API
response_issues = requests.get(api_url_issues, headers=headers)
data_issues = response_issues.json()

# Extract measures
measures = {measure['metric']: measure['value'] for measure in data_measures['component']['measures']}

# Extract issues
issues = data_issues['issues']

# Generate HTML report
html_report = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SonarQube Detailed Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1, h2, h3 {{ color: #333; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .issue {{ margin-bottom: 10px; }}
    </style>
</head>
<body>
    <h1>SonarQube Detailed Report</h1>
    <h2>Summary</h2>
    <table>
        <tr>
            <th>Metric</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>NCLOC</td>
            <td>{ncloc}</td>
        </tr>
        <tr>
            <td>Bugs</td>
            <td>{bugs}</td>
        </tr>
        <tr>
            <td>Code Smells</td>
            <td>{code_smells}</td>
        </tr>
        <tr>
            <td>Vulnerabilities</td>
            <td>{vulnerabilities}</td>
        </tr>
        <tr>
            <td>Coverage</td>
            <td>{coverage}%</td>
        </tr>
        <tr>
            <td>Duplicated Lines Density</td>
            <td>{duplicated_lines_density}%</td>
        </tr>
    </table>
    <h2>Issues</h2>
    <table>
        <tr>
            <th>Type</th>
            <th>Severity</th>
            <th>Message</th>
            <th>File</th>
            <th>Line</th>
        </tr>
""".format(
    ncloc=measures.get('ncloc', 'N/A'),
    bugs=measures.get('bugs', 'N/A'),
    code_smells=measures.get('code_smells', 'N/A'),
    vulnerabilities=measures.get('vulnerabilities', 'N/A'),
    coverage=measures.get('coverage', 'N/A'),
    duplicated_lines_density=measures.get('duplicated_lines_density', 'N/A')
)

# Append issues to HTML report
for issue in issues:
    html_report += """
        <tr>
            <td>{type}</td>
            <td>{severity}</td>
            <td>{message}</td>
            <td>{file}</td>
            <td>{line}</td>
        </tr>
    """.format(
        type=issue.get('type', 'N/A'),
        severity=issue.get('severity', 'N/A'),
        message=issue.get('message', 'N/A'),
        file=issue.get('component', 'N/A').split(':')[-1],
        line=issue.get('line', 'N/A') if 'line' in issue else 'N/A'
    )

html_report += """
    </table>
</body>
</html>
"""

# Save HTML report to a file
with open('sonarqube_detailed_report.html', 'w') as file:
    file.write(html_report)

print("Detailed HTML report generated successfully!")
