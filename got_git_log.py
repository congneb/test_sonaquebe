import re

# git log --since=2025-02-01 --until=2025-02-09 > a.log

commit_message = """
commit fe31d506d921192c1b878cd4c99cbf1c5f996a74
Author: congneb <51370224+congneb@users.noreply.github.com>
Date:   Tue Feb 4 21:31:35 2025 +0700

    Update build.yml

commit c84e467a186cb9425362c8dbb8c9c64cd0cd9f8b
Author: congneb <51370224+congneb@users.noreply.github.com>
Date:   Tue Feb 4 21:22:08 2025 +0700

    haha build.yml
"""

# Function to parse commit message
def parse_commit_message(commit_message):
    commits = []
    commit_pattern = re.compile(r'commit (\w+)\nAuthor: (.+) <(.+)>\nDate:\s+(.+)\n\n\s{4}(.+)', re.MULTILINE)
    
    for match in commit_pattern.finditer(commit_message):
        commit_info = {
            'Commit Hash': match.group(1),
            'Author': match.group(2),
            'Author Email': match.group(3),
            'Date': match.group(4),
            'Message': match.group(5)
        }
        commits.append(commit_info)
    
    return commits

# Parse the commit message
parsed_commits = parse_commit_message(commit_message)

# Print the parsed commits
for commit in parsed_commits:
    print(f"Commit Hash: {commit['Commit Hash']}")
    print(f"Author: {commit['Author']} <{commit['Author Email']}>")
    print(f"Date: {commit['Date']}")
    print(f"Message: {commit['Message']}")
    print("\n")

