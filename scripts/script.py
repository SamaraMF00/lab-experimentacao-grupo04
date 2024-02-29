import requests
from datetime import datetime

def calculate_age(created_at):
    created_at_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
    current_date = datetime.now()
    age = current_date - created_at_date
    return age.days

def get_repository_info(repository):
    repo_node = repository['node']
    age = calculate_age(repo_node['createdAt'])
    total_pull_requests = repo_node['pullRequests']['totalCount']
    total_releases = repo_node['releases']['totalCount']
    last_updated_at = calculate_age(repo_node['updatedAt'])
    primary_language = repo_node['primaryLanguage']['name'] if repo_node['primaryLanguage'] else "N/A"
    closed_issues = repo_node['closedIssues']['totalCount']
    total_issues = repo_node['totalIssues']['totalCount']
    issues_ratio = closed_issues / total_issues if total_issues != 0 else 0

    return {
        'Repository name': repo_node['name'],
        'RQ1 - Repository age (days)': age,
        'RQ2 - Total pull requests accepted': total_pull_requests,
        'RQ3 - Total releases': total_releases,
        'RQ4 - Time since last update (days)': last_updated_at,
        'RQ5 - Primary language': primary_language,
        'RQ6 - Issues closed percentage': issues_ratio
    }

def main():
    token = SEU_TOKEN_AQUI
    headers = {'Authorization': f'Bearer {token}'}
    endpoint = 'https://api.github.com/graphql'
    query = '''
    query ($after: String!){
      search(query: "stars:>1", type: REPOSITORY, first: 20, after: $after) {
      
        pageInfo {
          endCursor
          startCursor
          hasNextPage
          hasPreviousPage
        }

        edges {
      
          node {
          
            ... on Repository {
              name
              createdAt
              updatedAt

              pullRequests(states: MERGED) {
                totalCount
              }
              primaryLanguage {
                name
              }
              closedIssues: issues(states: CLOSED) {
                totalCount
              }
              totalIssues: issues {
                totalCount
              }
              releases {
                totalCount
              }
            }
          }
        }
      }
    }
    '''   

    repositories_info = []
    has_next_page = True
    end_cursor = ""
    variables = {}
    intCont = 0

    while has_next_page and intCont < 1000:
        if end_cursor == "":
            query_with_after = query.replace(', after: $after', "")
            query_with_after = query_with_after.replace('($after: String!)', "")
            response = requests.post(endpoint, json={'query': query_with_after}, headers=headers)
        else:
            variables['after'] = end_cursor
            response = requests.post(endpoint, json={'query': query, 'variables': variables}, headers=headers)

        data = response.json()

        for repository in data['data']['search']['edges']:           
            repository_info = get_repository_info(repository)
            repositories_info.append(repository_info)            

        if data['data']['search']['pageInfo']['hasNextPage']:
            end_cursor = data['data']['search']['pageInfo']['endCursor']
        else:
            has_next_page = False

        intCont += 20    

        

    for info in repositories_info:
        print(info)
        print()

if __name__ == "__main__":
    main()
